from sqlalchemy import Column, Integer, String
from app.db import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    quantity = Column(Integer)
    price = Column(Integer)

    class Config:
        orm_mode = True
        from_attributes = True 
