from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from .models import Customer

customer_create_bp = Blueprint('customer_create', __name__, template_folder='templates')

@customer_create_bp.route('/create', methods=['GET', 'POST'])
def customer_create():
    if request.method == 'POST':
        name = request.form.get('name')
        address = request.form.get('address')
        phone = request.form.get('phone')
        alt_phone = request.form.get('alt_phone')
        
        new_customer = Customer(
            name=name,
            address=address,
            phone=phone,
            alt_phone=alt_phone,
        )
        
        db.session.add(new_customer)
        db.session.commit()
        
        flash('Customer created successfully.', 'success')
        return redirect(url_for('main.sale.customer.customer_read.customer_read'))
        
    return render_template('customer_create.html')