from app import db

class Bom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=True)
    material_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=True)
    
    # Specify foreign_keys for both relationships to resolve ambiguity
    item = db.relationship('Item', foreign_keys=[item_id], backref=db.backref('boms', lazy=True))
    material = db.relationship('Item', foreign_keys=[material_id], backref=db.backref('material_for_boms', lazy=True))
    quantity = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"<Bom item_id={self.item_id} material_id={self.material_id}>"
