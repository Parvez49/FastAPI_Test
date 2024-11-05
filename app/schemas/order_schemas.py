from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class OrderBase(BaseModel):
    product_name: str
    quantity: int
    price: int

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True

class PaginatedOrderResponse(BaseModel):
    total: int
    page: int
    page_size: int
    next: Optional[HttpUrl] = None
    previous: Optional[HttpUrl] = None
    orders: List[Order]
