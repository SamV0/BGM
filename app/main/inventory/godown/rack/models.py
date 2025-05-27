from app import db
from app.models import BaseModel

class Rack(BaseModel):
    __tablename__ = "racks"
    name = db.Column(db.String(50), nullable=True)
    godown_id = db.Column(db.Integer, db.ForeignKey('godowns.id'), nullable=True)
    godown = db.relationship('Godown', backref=db.backref('rack_list', lazy='dynamic'))
