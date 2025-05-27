from flask import Blueprint, redirect, url_for
from app import db
from .models import Bom

bom_delete_bp = Blueprint('bom_delete', __name__, template_folder='templates')

@bom_delete_bp.route('/delete/<int:id>')
def bom_delete(id):
    bom = Bom.query.get_or_404(id)
    db.session.delete(bom)
    db.session.commit()
    return redirect(url_for('main.inventory.bom.bom_read.bom_read'))
