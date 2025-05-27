from flask import Blueprint, render_template
from app.main.inventory.item.models import Item
from app import db

item_read_bp = Blueprint('item_read', __name__, template_folder='templates')

@item_read_bp.route('/read', methods=['GET'])
def item_read():
    items = Item.query.order_by(Item.name).all()  # Sort items alphabetically by name
    return render_template('item_read.html', items=items)
