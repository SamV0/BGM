from app import db
from app.models import BaseModel

class SalesOrder(BaseModel):
    __tablename__ = 'sales_orders'
    
    order_number = db.Column(db.String(50), unique=True, nullable=True)
    order_date = db.Column(db.DateTime, nullable=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=True)
    customer = db.relationship('Customer', back_populates='sales_orders')
    delivery_date = db.Column(db.DateTime)
    status = db.Column(db.String(20), nullable=True)  # e.g., 'pending', 'processing', 'completed'
    
    # Relationships
    works = db.relationship('Work', back_populates='sales_order')