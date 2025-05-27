from flask import Blueprint, redirect, url_for, flash
from app import db
from .models import Inventory

inventory_delete_bp = Blueprint('inventory_delete', __name__, url_prefix='/inventory')

@inventory_delete_bp.route('/delete/<int:id>', methods=['POST'])
def inventory_delete(id):
    inventory = Inventory.query.get_or_404(id)
    try:
        db.session.delete(inventory)
        db.session.commit()
        flash(' deleted successfully.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting inventory record: {str(e)}', 'danger')
    
    return redirect(url_for('main.inventory.inventory_read.inventory_read'))
