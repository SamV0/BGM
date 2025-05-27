from flask import Blueprint, render_template
from .models import SalesOrder
from sqlalchemy.orm import joinedload

sale_read_bp = Blueprint('sale_read', __name__, template_folder='templates')

@sale_read_bp.route('/sales', methods=['GET'], endpoint='sale_read')
def sale_read():
    sales = SalesOrder.query\
        .options(joinedload(SalesOrder.works))\
        .all()
    return render_template('sale_read.html', sales=sales)