from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from .models import Bom

bom_update_bp = Blueprint('bom_update', __name__, template_folder='templates')

@bom_update_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def bom_update(id):
    bom = Bom.query.get_or_404(id)
    if request.method == 'POST':
        bom.item_id = request.form['item_id']
        bom.material_id = request.form['material_id']
        bom.quantity = request.form['quantity']
        db.session.commit()
        return redirect(url_for('main.inventory.bom.bom_read.bom_read'))
    return render_template('bom_update.html', bom=bom)
