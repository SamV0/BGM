from flask import Blueprint, render_template
from app.main.purchase.models import Purchase
from sqlalchemy.orm import joinedload

purchase_read_bp = Blueprint('purchase_read', __name__, template_folder='templates')

@purchase_read_bp.route('/read')
def purchase_read():
    purchases = Purchase.query\
        .options(joinedload(Purchase.supplier))\
        .options(joinedload(Purchase.item))\
        .all()
    return render_template('purchase_read.html', purchases=purchases)