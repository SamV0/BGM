from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.main.inventory.models import Inventory
from app.main.inventory.item.models import Item
from app.main.inventory.godown.models import Godown
from app.main.inventory.godown.rack.models import Rack

inventory_create_bp = Blueprint('inventory_create', __name__, template_folder='templates')

@inventory_create_bp.route('/create', methods=['GET', 'POST'])
def inventory_create():
    if request.method == 'POST':
        item_id = request.form['item_id']
        godown_id = request.form['godown_id']
        rack_id = request.form['rack_id']
        avl_qnty = request.form['avl_qnty']
        min_qnty = request.form['min_qnty']
        rod_qnty = request.form['rod_qnty']

        new_inventory = Inventory(item_id=item_id, godown_id=godown_id, rack_id=rack_id, avl_qnty=avl_qnty, min_qnty=min_qnty, rod_qnty=rod_qnty)
        db.session.add(new_inventory)
        db.session.commit()
        flash('Inventory created successfully.', 'success')
        return redirect(url_for('main.inventory.inventory_read.inventory_read'))

    items = Item.query.all()
    godowns = Godown.query.all()
    racks = Rack.query.all()
    return render_template('inventory_create.html', items=items, godowns=godowns, racks=racks)
