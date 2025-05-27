from flask import Blueprint, render_template
from .models import Customer

customer_read_bp = Blueprint('customer_read', __name__, template_folder='templates')

@customer_read_bp.route('/', methods=['GET'])
def customer_read():
    customers = Customer.query.all()
    return render_template('customer_read.html', customers=customers)