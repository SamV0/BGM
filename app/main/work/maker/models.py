from app import db
from app.models import BaseModel

class Maker(BaseModel):
    __tablename__ = "makers"
    name = db.Column(db.String(50), nullable=True)
    address = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(10), nullable=True)
    alt_phone = db.Column(db.String(10), nullable=True)
    is_active = db.Column(db.Boolean, default=True, nullable=True)
    remarks = db.Column(db.String(200), nullable=True)

    # Relationships
    works = db.relationship('Work', back_populates='maker')
    processes = db.relationship('Process', back_populates='maker')