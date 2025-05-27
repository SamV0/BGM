from app import db
from app.models import BaseModel

class Supplier(BaseModel):
    __tablename__ = 'suppliers'
    name = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(200), nullable=True)
    phone = db.Column(db.String(10), nullable=True)
    alt_phone = db.Column(db.String(10), nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    remarks = db.Column(db.Text)
    
    # Relationships
    purchases = db.relationship('Purchase', back_populates='supplier')
