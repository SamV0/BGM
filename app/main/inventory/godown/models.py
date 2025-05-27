from app import db
from app.models import BaseModel

class Godown(BaseModel):
    __tablename__ = "godowns"
    name = db.Column(db.String(50), nullable=True)
    racks = db.relationship('Rack', backref='godown_rack', lazy='subquery')
