# app/crud.py
from sqlalchemy.orm import Session
from app.models import order_models
from app.schemas import order_schemas

def create_order(db: Session, order: order_schemas.OrderCreate):
    db_order = order_models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session, skip: int = 0, limit: int = 10):
    return db.query(order_models.Order).offset(skip).limit(limit).all()

def get_order(db: Session, order_id: int):
    return db.query(order_models.Order).filter(order_models.Order.id == order_id).first()

def get_total_orders_count(db: Session):
    return db.query(order_models.Order).count()
