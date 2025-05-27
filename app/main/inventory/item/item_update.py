from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.main.inventory.item.models import Item
from app import db
from decimal import Decimal

item_update_bp = Blueprint('item_update', __name__, template_folder='templates')

@item_update_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def item_update(id):
    item = Item.query.get_or_404(id)
    if request.method == 'POST':
        item.name = request.form['name']
        item.width_m = Decimal(request.form['width_m'])
        item.width_G = Decimal(request.form['width_G'])
        item.length_in = Decimal(request.form['length_in'])
        item.breadth_soot = Decimal(request.form['breadth_soot'])
        item.weight_gm = Decimal(request.form['weight_gm'])
        item.weight_kg = Decimal(request.form['weight_kg'])

        item.generate_full_name()  # Regenerate the full_name after updating values
        
        db.session.commit()
        flash('Item updated successfully!', 'success')
        return redirect(url_for('main.inventory.item.item_read.item_read'))

    return render_template('item_update.html', item=item)
