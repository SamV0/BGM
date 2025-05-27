from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from .models import Work
from .maker.models import Maker
from .process.models import Process
from ..inventory.item.models import Item
from ..sale.models import SalesOrder
from datetime import datetime

work_update_bp = Blueprint('work_update', __name__, template_folder='templates')

@work_update_bp.route('/work_update/<int:work_id>', methods=['GET', 'POST'])
def work_update(work_id):
    work = Work.query.get_or_404(work_id)
    
    if request.method == 'POST':
        try:
            assigned_date = datetime.strptime(request.form['assigned_date'], '%Y-%m-%d')
            received_date = datetime.strptime(request.form['received_date'], '%Y-%m-%d') if request.form.get('received_date') else None
            
            work.sales_order_id = request.form['sales_order_id']
            work.maker_id = request.form['maker_id']
            work.process_id = request.form['process_id']
            work.assigned_date = assigned_date
            work.assigned_quantity = request.form['assigned_quantity']
            work.assigned_items = request.form['assigned_items']
            work.work_to_do = request.form['work_to_do']
            work.received_date = received_date
            work.received_quantity = request.form['received_quantity'] if request.form.get('received_quantity') else None
            work.received_items = request.form['received_items'] if request.form.get('received_items') else None
            work.work_done = request.form['work_done'] if request.form.get('work_done') else None
            work.status = request.form['status']
            work.remarks = request.form['remarks']
            
            db.session.commit()
            flash("work updated successfully!", "success")
            return redirect(url_for('main.work.work_read.work_read'))
        except Exception as e:
            db.session.rollback()
            flash(f"Error updating work: {str(e)}", "error")
            return redirect(url_for('main.work.work_update.work_update', work_id=work_id))

    makers = Maker.query.all()
    processes = Process.query.all()
    items = Item.query.all()
    sales_orders = SalesOrder.query.all()
    
    return render_template('work_update.html',
                         work=work,
                         makers=makers,
                         processes=processes,
                         items=items,
                         sales_orders=sales_orders)