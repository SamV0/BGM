from flask import Blueprint, redirect, url_for, flash
from app import db
from app.main.purchase.supplier.models import Supplier

supplier_delete_bp = Blueprint('supplier_delete', __name__)

@supplier_delete_bp.route('/delete/<int:id>', methods=['POST'])
def supplier_delete(id):
    supplier = Supplier.query.get_or_404(id)
    try:
        db.session.delete(supplier)
        db.session.commit()
        flash('Supplier deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting supplier: {str(e)}', 'danger')
    
    return redirect(url_for('main.purchase.supplier.supplier_read.supplier_read'))