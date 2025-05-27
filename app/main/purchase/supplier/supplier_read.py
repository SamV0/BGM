from flask import Blueprint, render_template
from app.main.purchase.supplier.models import Supplier

supplier_read_bp = Blueprint('supplier_read', __name__, template_folder='templates')

@supplier_read_bp.route('/read')
def supplier_read():
    suppliers = Supplier.query.all()
    return render_template('supplier_read.html', suppliers=suppliers)