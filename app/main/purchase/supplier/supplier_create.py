from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.main.purchase.supplier.models import Supplier

supplier_create_bp = Blueprint('supplier_create', __name__, template_folder='templates')

@supplier_create_bp.route('/create', methods=['GET', 'POST'])
def supplier_create():
    if request.method == 'POST':
        try:
            new_supplier = Supplier(
                name=request.form['name'],
                address=request.form['address'],
                phone=request.form['phone'],
                alt_phone=request.form.get('alt_phone'),
                is_active=True,
                remarks=request.form.get('remarks')
            )
            
            db.session.add(new_supplier)
            db.session.commit()
            flash('Supplier created successfully!', 'success')
            return redirect(url_for('main.purchase.supplier.supplier_read.supplier_read'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating supplier: {str(e)}', 'danger')
            return redirect(url_for('main.purchase.supplier.supplier_create.supplier_create'))

    return render_template('supplier_create.html')