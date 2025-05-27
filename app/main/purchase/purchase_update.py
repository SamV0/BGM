from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.main.purchase.models import Purchase
from app.main.purchase.supplier.models import Supplier
from app.main.inventory.item.models import Item
from datetime import datetime

purchase_update_bp = Blueprint('purchase_update', __name__, template_folder='templates')

@purchase_update_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def purchase_update(id):
    purchase = Purchase.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            # Handle status changes
            new_status = request.form.get('status')
            if new_status:
                if new_status == 'cancelled':
                    purchase.status = 'cancelled'
                elif new_status == 'ordered' and purchase.status == 'draft':
                    purchase.status = 'ordered'
                elif new_status == 'received' and purchase.status == 'ordered':
                    purchase.status = 'received'
                    purchase.received_date = datetime.strptime(request.form['received_date'], '%Y-%m-%d').date()
            
            # Only allow updates to draft orders
            if purchase.status == 'draft':
                purchase.supplier_id = request.form['supplier_id']
                purchase.item_id = request.form['item_id']
                purchase.ordered_weight = float(request.form['ordered_weight'])
                purchase.expected_date = datetime.strptime(request.form['expected_date'], '%Y-%m-%d').date()
            
            # These can be updated regardless of status
            purchase.remarks = request.form.get('remarks')
            
            db.session.commit()
            flash('Purchase order updated successfully!', 'success')
            return redirect(url_for('main.purchase.purchase_read.purchase_read'))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating purchase: {str(e)}', 'error')
            return redirect(url_for('main.purchase.purchase_update.purchase_update', id=id))

    suppliers = Supplier.query.filter_by(is_active=True).all()
    items = Item.query.all()
    return render_template('purchase_update.html', 
                         purchase=purchase,
                         suppliers=suppliers,
                         items=items)