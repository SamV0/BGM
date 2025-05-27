from app import db
from app.models import BaseModel

class Customer(BaseModel):
    __tablename__ = 'customers'
    
    name = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(200), nullable=True)
    phone = db.Column(db.String(10), nullable=True)
    alt_phone = db.Column(db.String(10), nullable=True)
    
    # Relationships
    sales_orders = db.relationship('SalesOrder', back_populates='customer')