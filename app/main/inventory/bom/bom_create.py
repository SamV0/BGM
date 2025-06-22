from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from .models import Bom

bom_create_bp = Blueprint('bom_create', __name__, template_folder='templates')

@bom_create_bp.route('/bom_create', methods=['GET', 'POST'])
def bom_create():
    if request.method == 'POST':
        item_id = request.form['item_id']
        material_id = request.form['material_id']
        quantity = request.form['quantity']

        new_bom = Bom(item_id=item_id, material_id=material_id, quantity=quantity)
        db.session.add(new_bom)
        db.session.commit()
        return redirect(url_for('main.inventory.bom.bom_read.bom_read'))
    return render_template('bom_create.html')
