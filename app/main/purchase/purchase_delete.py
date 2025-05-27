from flask import Blueprint, redirect, url_for, flash
from app import db
from app.main.purchase.models import Purchase

purchase_delete_bp = Blueprint('purchase_delete', __name__)

@purchase_delete_bp.route('/delete/<int:id>', methods=['POST'])
def purchase_delete(id):
    purchase = Purchase.query.get_or_404(id)
    try:
        # The cascade='all, delete-orphan' in the model will handle related items
        db.session.delete(purchase)
        db.session.commit()
        flash('Purchase order deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting purchase order: {str(e)}', 'danger')
    
    return redirect(url_for('main.purchase.purchase_read.purchase_read'))