from app import db

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=True)
    item = db.relationship('Item', backref=db.backref('inventories', lazy=True))
    godown_id = db.Column(db.Integer, db.ForeignKey('godowns.id'), nullable=True)
    godown = db.relationship('Godown', backref=db.backref('inventories', lazy=True))
    rack_id = db.Column(db.Integer, db.ForeignKey('racks.id'), nullable=True)
    rack = db.relationship('Rack', backref=db.backref('inventories', lazy=True))
    avl_qnty = db.Column(db.Integer, nullable=True)
    min_qnty = db.Column(db.Integer, nullable=True)
    rod_qnty = db.Column(db.Integer, nullable=True)