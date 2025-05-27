from app import db
from app.models import BaseModel
from sqlalchemy.types import Numeric

class Purchase(BaseModel):
    __tablename__ = 'purchases'
    
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'), nullable=True)
    supplier = db.relationship('Supplier', back_populates='purchases')
    ordered_date = db.Column(db.Date, nullable=True)
    ordered_weight = db.Column(Numeric(10, 2), nullable=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=True)
    item = db.relationship('Item', backref=db.backref('purchases', lazy=True))
    status = db.Column(db.String(20), nullable=True, default='draft')  # draft, ordered, received, cancelled
    expected_date = db.Column(db.Date, nullable=True)
    received_date = db.Column(db.Date)
    remarks = db.Column(db.Text)