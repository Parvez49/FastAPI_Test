from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from app.schemas import order_schemas
from app.db import get_db 
from app.crud import order_crud
from app.redis import get_redis_client
import json

router = APIRouter()


@router.post("/orders/", response_model=order_schemas.OrderCreate)
async def create_order_endpoint(order: order_schemas.OrderCreate, db: Session = Depends(get_db)):
    db_order = order_crud.create_order(db=db, order=order)
    return db_order


@router.get("/orders/", response_model=order_schemas.PaginatedOrderResponse)
def read_orders(
    request: Request, 
    skip: int = 0, 
    limit: int = 2, 
    db: Session = Depends(get_db),
    redis_client = Depends(get_redis_client)
    ):

    total_count = redis_client.get('total_orders_count')
    if total_count is None:
        total_count = order_crud.get_total_orders_count(db)
        redis_client.set('total_orders_count',total_count, ex=3600)

    cache_key = f'orders:{skip}:{limit}'
    cached_orders = redis_client.get(cache_key)

    if cached_orders is None:
        print('Without cache')
        orders = order_crud.get_orders(db, skip=skip, limit=limit)
        orders = [order_schemas.Order.from_orm(order).dict() for order in orders]
        redis_client.set(cache_key,json.dumps(orders), ex=3600)
    else:
        print('With cache')
        orders = json.loads(cached_orders)
    
    # Calculate the current page
    page = (skip // limit) + 1 if limit > 0 else 1

    # Calculate next and previous skip values
    next_skip = skip + limit
    prev_skip = skip - limit if skip - limit >= 0 else None

    # Construct URLs for next and previous pages
    next_url = (
        str(request.url.replace_query_params(skip=next_skip, limit=limit))
        if next_skip < total_count
        else None
    )
    previous_url = (
        str(request.url.replace_query_params(skip=prev_skip, limit=limit))
        if prev_skip is not None
        else None
    )


    return {
        "total": total_count,
        "page": page,
        "page_size": limit,
        "next": next_url,
        "previous": previous_url,
        "orders": orders,
    }


@router.get("/orders/{order_id}", response_model=order_schemas.Order)
async def get_order_endpoint(order_id: int, db: Session = Depends(get_db)):
    db_order = order_crud.get_order(db, order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order
