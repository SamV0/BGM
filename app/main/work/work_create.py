from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from .models import Work
from .maker.models import Maker
from .process.models import Process
from ..inventory.item.models import Item
from ..sale.models import SalesOrder
from datetime import datetime

work_create_bp = Blueprint('work_create', __name__, template_folder='templates')

@work_create_bp.route('/work_create', methods=['GET', 'POST'])
def work_create():
    if request.method == 'POST':
        try:
            assigned_date = datetime.strptime(request.form['assigned_date'], '%Y-%m-%d')
            received_date = datetime.strptime(request.form['received_date'], '%Y-%m-%d') if request.form.get('received_date') else None
            
            new_work = Work(
                maker_id=request.form['maker_id'],
                process_id=request.form['process_id'],
                sales_order_id=request.form['sales_order_id'],
                assigned_date=assigned_date,
                assigned_quantity=request.form['assigned_quantity'],
                assigned_items=request.form['assigned_items'],
                work_to_do=request.form['work_to_do'],
                received_date=received_date,
                received_quantity=request.form['received_quantity'] if request.form.get('received_quantity') else None,
                received_items=request.form['received_items'] if request.form.get('received_items') else None,
                work_done=request.form['work_done'] if request.form.get('work_done') else None,
                status=request.form['status'],
                remarks=request.form['remarks']
            )
            
            db.session.add(new_work)
            db.session.commit()
            flash("work created successfully!", "success")
            return redirect(url_for('main.work.work_read.work_read'))
        except Exception as e:
            db.session.rollback()
            flash(f"Error creating work: {str(e)}", "error")
            return redirect(url_for('main.work.work_create.work_create'))

    makers = Maker.query.all()
    processes = Process.query.all()
    items = Item.query.all()
    sales_orders = SalesOrder.query.all()
    
    return render_template('work_create.html', 
                         makers=makers,
                         processes=processes, 
                         items=items,
                         sales_orders=sales_orders)