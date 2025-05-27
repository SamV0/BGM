from flask import Blueprint, render_template
from app import db
from .models import Inventory

inventory_read_bp = Blueprint('inventory_read', __name__, url_prefix='/inventory', template_folder='templates')

@inventory_read_bp.route('/read')
def inventory_read():
    inventories = Inventory.query.all()
    return render_template('inventory_read.html', inventories=inventories)
