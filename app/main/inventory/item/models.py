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
        measurements = {
            'width_m': 'm',
            'width_G': 'G',
            'length_in': 'in',
            'breadth_soot': 'soot'
        }
        
        def safe_float(value):
            """Convert value to float safely, return 0 if value is None or empty string"""
            if value is None or value == '':
                return 0
            return float(value)
        
        parts = [f"{getattr(self, attr)}{unit}" 
                for attr, unit in measurements.items() 
                if safe_float(getattr(self, attr)) > 0]
        
        self.full_name = f"{self.name} {' '.join(parts)}" if parts else self.name