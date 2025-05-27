from flask import Blueprint, redirect, url_for, flash
from app import db
from .models import SalesOrder

sale_delete_bp = Blueprint('sale_delete', __name__)

@sale_delete_bp.route('/delete/<int:id>', methods=['POST'])
def sale_delete(id):
    sale = SalesOrder.query.get_or_404(id)
    # TODO: Implement sales order deletion logic
    flash('Delete functionality not yet implemented.', 'info')
    return redirect(url_for('main.sale.sale_read.sale_read'))