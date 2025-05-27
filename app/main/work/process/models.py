from app import db
from app.models import BaseModel
from sqlalchemy.types import Numeric

class Process(BaseModel):
    __tablename__ = 'processes'
    name = db.Column(db.String(50), nullable=True)
    description = db.Column(db.Text, nullable=True)
    duration_in_days = db.Column(db.Integer, nullable=True)
    cost_in_inr = db.Column(Numeric(10, 2), nullable=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=True)
    maker_id = db.Column(db.Integer, db.ForeignKey('makers.id'), nullable=True)
    is_active = db.Column(db.Boolean, default=True, nullable=True)

    # Relationships
    item = db.relationship('Item', backref=db.backref('processes', lazy='dynamic'))
    maker = db.relationship('Maker', back_populates='processes')
    works = db.relationship('Work', back_populates='process')
