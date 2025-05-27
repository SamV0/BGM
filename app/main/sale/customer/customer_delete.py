from flask import Blueprint, redirect, url_for, flash
from app import db
from .models import Customer

customer_delete_bp = Blueprint('customer_delete', __name__, template_folder='templates')

@customer_delete_bp.route('/delete/<int:id>', methods=['POST'])
def customer_delete(id):
    customer = Customer.query.get_or_404(id)
    customer.is_active = False
    db.session.commit()
    
    flash('Customer deactivated successfully.', 'success')
    return redirect(url_for('main.sale.customer.customer_read.customer_read'))