from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.main.purchase.models import Purchase
from app.main.purchase.supplier.models import Supplier
from app.main.inventory.item.models import Item
from datetime import datetime

purchase_create_bp = Blueprint('purchase_create', __name__, template_folder='templates')

@purchase_create_bp.route('/create', methods=['GET', 'POST'])
def purchase_create():
    if request.method == 'POST':
        try:
            new_purchase = Purchase(
                supplier_id=request.form['supplier_id'],
                ordered_date=datetime.now().date(),
                ordered_weight=float(request.form['ordered_weight']),
                item_id=request.form['item_id'],
                expected_date=datetime.strptime(request.form['expected_date'], '%Y-%m-%d').date(),
                remarks=request.form.get('remarks'),
                status='draft'
            )
            
            db.session.add(new_purchase)
            db.session.commit()
            flash('Purchase order created successfully!', 'success')
            return redirect(url_for('main.purchase.purchase_read.purchase_read'))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating purchase: {str(e)}', 'error')
            return redirect(url_for('main.purchase.purchase_create.purchase_create'))

    suppliers = Supplier.query.filter_by(is_active=True).all()
    items = Item.query.all()
    return render_template('purchase_create.html', suppliers=suppliers, items=items)