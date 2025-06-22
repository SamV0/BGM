from flask import Blueprint, render_template
from app import db
from .models import Bom

bom_read_bp = Blueprint('bom_read', __name__, template_folder='templates')

@bom_read_bp.route('/read')
def bom_read():
    boms = Bom.query.all()
    return render_template('bom_read.html', boms=boms)
