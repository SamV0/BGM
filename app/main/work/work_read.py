from flask import Blueprint, render_template
from .models import Work
from sqlalchemy.orm import joinedload

work_read_bp = Blueprint('work_read', __name__, template_folder='templates')

@work_read_bp.route('/work_read')
def work_read():
    works = Work.query\
        .options(joinedload(Work.sales_order))\
        .options(joinedload(Work.maker))\
        .options(joinedload(Work.process))\
        .options(joinedload(Work.assigned_item))\
        .options(joinedload(Work.received_item))\
        .all()
    return render_template('work_read.html', works=works)