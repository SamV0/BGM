from flask import Blueprint, redirect, url_for, flash
from app import db
from .models import Godown
from app.main.inventory.godown.rack.models import Rack

godown_delete_bp = Blueprint('godown_delete', __name__, template_folder='templates')

@godown_delete_bp.route('/delete/<int:godown_id>', methods=['POST'])
def godown_delete(godown_id):
    godown = Godown.query.get_or_404(godown_id)
    
    racks = Rack.query.filter_by(godown_id=godown.id).all()
    for rack in racks:
        db.session.delete(rack)
    
    db.session.delete(godown)
    db.session.commit()
    flash("Godown and its associated racks deleted successfully!", "success")
    return redirect(url_for('main.inventory.godown.godown_read.godown_read'))
