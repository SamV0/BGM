from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from .models import SalesOrder
from ..sale.customer.models import Customer
from datetime import datetime

sale_create_bp = Blueprint('sale_create', __name__, template_folder='templates')

@sale_create_bp.route('/sale_create', methods=['GET', 'POST'])
def sale_create():
    if request.method == 'POST':
        order_number = request.form.get('order_number')
        order_date_str = request.form.get('order_date')
        customer_id = request.form.get('customer_id')
        delivery_date_str = request.form.get('delivery_date')
        status = request.form.get('status')
        
        # Convert string dates to datetime objects
        order_date = datetime.strptime(order_date_str, '%Y-%m-%d') if order_date_str else None
        delivery_date = datetime.strptime(delivery_date_str, '%Y-%m-%d') if delivery_date_str else None
        
        new_sales_order = SalesOrder(
            order_number=order_number,
            order_date=order_date,
            customer_id=customer_id,
            delivery_date=delivery_date,
            status=status
        )

        db.session.add(new_sales_order)
        db.session.commit()

        flash('Sales order created successfully.', 'success')
        return redirect(url_for('main.sale.sale_read.sale_read'))

    customers = Customer.query.all()
    return render_template('sale_create.html', customers=customers)