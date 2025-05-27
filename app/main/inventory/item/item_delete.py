from flask import Blueprint, redirect, url_for, flash
from app.main.inventory.item.models import Item
from app import db

item_delete_bp = Blueprint('item_delete', __name__)

@item_delete_bp.route('/delete/<int:id>', methods=['POST'])
def item_delete(id):
    item = Item.query.get_or_404(id)
    full_name = item.full_name
    db.session.delete(item)
    db.session.commit()
    flash(f'"{full_name}" - Removed from items', 'success')
    return redirect(url_for('main.inventory.item.item_read.item_read'))
