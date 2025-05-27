from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from .models import Customer

customer_update_bp = Blueprint('customer_update', __name__, template_folder='templates')

@customer_update_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def customer_update(id):
    customer = Customer.query.get_or_404(id)
    
    if request.method == 'POST':
        customer.name = request.form.get('name')
        customer.address = request.form.get('address')
        customer.phone = request.form.get('phone')
        customer.alt_phone = request.form.get('alt_phone')
        customer.remarks = request.form.get('remarks')
        customer.is_active = request.form.get('is_active') == 'true'
        
        db.session.commit()
        flash('Customer updated successfully.', 'success')
        return redirect(url_for('main.sale.customer.customer_read.customer_read'))
        
    return render_template('customer_update.html', customer=customer)