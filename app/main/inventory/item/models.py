from app import db
from app.models import BaseModel
from sqlalchemy.types import Numeric

class Item(BaseModel):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    full_name = db.Column(db.String(200), nullable=True)
    width_m = db.Column(Numeric(10, 2), nullable=True)
    width_G = db.Column(Numeric(10, 2), nullable=True)
    length_in = db.Column(Numeric(10, 2), nullable=True)
    breadth_soot = db.Column(Numeric(10, 2), nullable=True)
    weight_gm = db.Column(Numeric(10, 2), nullable=True)
    weight_kg = db.Column(db.Numeric(10, 2), nullable=True)
    
    def generate_full_name(self):
        """Generates and updates the full_name field including only non-zero measurements"""
        measurements = []
        if float(self.width_m) > 0:
            measurements.append(f"{self.width_m}m")
        if float(self.width_G) > 0:
            measurements.append(f"{self.width_G}G")
        if float(self.length_in) > 0:
            measurements.append(f"{self.length_in}in")
        if float(self.breadth_soot) > 0:
            measurements.append(f"{self.breadth_soot}soot")
            
        self.full_name = f"{self.name} {' '.join(measurements)}" if measurements else self.name