from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.main.purchase.supplier.models import Supplier

supplier_update_bp = Blueprint('supplier_update', __name__, template_folder='templates')

@supplier_update_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def supplier_update(id):
    supplier = Supplier.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            supplier.name = request.form['name']
            supplier.address = request.form['address']
            supplier.phone = request.form['phone']
            supplier.alt_phone = request.form.get('alt_phone')
            supplier.email = request.form.get('email')
            supplier.gst_number = request.form.get('gst_number')
            supplier.is_active = 'is_active' in request.form
            supplier.remarks = request.form.get('remarks')
            
            db.session.commit()
            flash('Supplier updated successfully!', 'success')
            return redirect(url_for('main.purchase.supplier.supplier_read.supplier_read'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating supplier: {str(e)}', 'danger')
            return redirect(url_for('main.purchase.supplier.supplier_update.supplier_update', id=id))

    return render_template('supplier_update.html', supplier=supplier)