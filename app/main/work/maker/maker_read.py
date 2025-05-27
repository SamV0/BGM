from flask import Blueprint, render_template
from .models import Maker

maker_read_bp = Blueprint('maker_read', __name__, template_folder='templates')

@maker_read_bp.route('/maker_read')
def maker_read():
    makers = Maker.query.all()
    return render_template('maker_read.html', makers=makers)
