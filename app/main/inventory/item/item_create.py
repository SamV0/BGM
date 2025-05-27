from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.main.inventory.item.models import Item

item_create_bp = Blueprint('item_create', __name__, template_folder='templates', static_folder='static')

@item_create_bp.route('/create', methods=['GET', 'POST'])
def item_create():
    if request.method == 'POST':
        name = request.form.get('name')
        width_m = request.form.get('width_m')
        width_G = request.form.get('width_G')
        length_in = request.form.get('length_in')
        breadth_soot = request.form.get('breadth_soot')
        weight_gm = request.form.get('weight_gm')
        weight_kg = request.form.get('weight_kg')

        new_item = Item(name=name, width_m=width_m, 
                        width_G=width_G, length_in=length_in, breadth_soot=breadth_soot, 
                        weight_gm=weight_gm, weight_kg=weight_kg)
        
        new_item.generate_full_name()  # Generate the full_name before saving

        db.session.add(new_item)
        db.session.commit()
        flash("Item created successfully!", "success")
        return redirect(url_for('main.inventory.item.item_read.item_read'))
    return render_template('item_create.html')
