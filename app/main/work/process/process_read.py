from flask import Blueprint, render_template
from .models import Process
from sqlalchemy.orm import joinedload

process_read_bp = Blueprint('process_read', __name__, template_folder='templates')

@process_read_bp.route('/process_read')
def process_read():
    processes = Process.query\
        .options(joinedload(Process.item))\
        .options(joinedload(Process.maker))\
        .all()
    return render_template('process_read.html', processes=processes)
