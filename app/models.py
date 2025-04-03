from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    customer_fname = Column(String(50))
    customer_lname = Column(String(50))
    username = Column(String(50))
    password = Column(String(50))
    address = Column(String)
    city = Column(String(50))
    state = Column(String(50))
    pincode = Column(String(10))
    
class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    order_date = Column(Date)
    order_customer_id = Column(Integer)
    order_status = Column(String(50))

class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    category = Column(String(50))
    price = Column(DECIMAL(10, 2))
    stock_quantity = Column(Integer)