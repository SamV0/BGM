from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from .models import Inventory
from ..inventory.item.models import Item
from ..inventory.godown.models import Godown
from ..inventory.godown.rack.models import Rack

inventory_update_bp = Blueprint('inventory_update', __name__, url_prefix='/inventory')

@inventory_update_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def inventory_update(id):
    inventory = Inventory.query.get_or_404(id)
    if request.method == 'POST':
        inventory.item_id = request.form['item_id']
        inventory.godown_id = request.form['godown_id']
        inventory.rack_id = request.form['rack_id']
        inventory.avl_qnty = request.form['avl_qnty']
        inventory.min_qnty = request.form['min_qnty']
        inventory.rod_qnty = request.form['rod_qnty']
        db.session.commit()
        return redirect(url_for('main.inventory.inventory_read.inventory_read'))
    
    items = Item.query.all()
    godowns = Godown.query.all()
    racks = Rack.query.all()
    
    return render_template('inventory_update.html', 
                         inventory=inventory,
                         items=items,
                         godowns=godowns,
                         racks=racks)
