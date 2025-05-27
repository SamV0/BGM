from app import db
from app.models import BaseModel

class Work(BaseModel):
    __tablename__ = 'works'
    maker_id = db.Column(db.Integer, db.ForeignKey('makers.id'), nullable=True)
    process_id = db.Column(db.Integer, db.ForeignKey('processes.id'), nullable=True)
    sales_order_id = db.Column(db.Integer, db.ForeignKey('sales_orders.id'), nullable=True)
    assigned_date = db.Column(db.DateTime, nullable=True)
    assigned_quantity = db.Column(db.Numeric(10, 2), nullable=True)
    assigned_items = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=True)
    work_to_do = db.Column(db.Integer, nullable=True)
    received_date = db.Column(db.DateTime, nullable=True)
    received_quantity = db.Column(db.Numeric(10, 2), nullable=True)
    received_items = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=True)
    work_done = db.Column(db.Integer, nullable=True)
    status = db.Column(db.String(20), nullable=True)  # e.g., 'assigned', 'in_progress', 'completed'
    remarks = db.Column(db.String(200), nullable=True)

    # Relationships
    maker = db.relationship('Maker', back_populates='works')
    process = db.relationship('Process', back_populates='works')
    sales_order = db.relationship('SalesOrder', back_populates='works')
    assigned_item = db.relationship('Item', foreign_keys=[assigned_items], backref='assigned_works')
    received_item = db.relationship('Item', foreign_keys=[received_items], backref='received_works')