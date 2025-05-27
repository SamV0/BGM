from flask import Blueprint, request, redirect, url_for, render_template, flash
from app import db
from .models import Process
from ..maker.models import Maker
from app.main.inventory.item.models import Item

process_create_bp = Blueprint('process_create', __name__, template_folder='templates')

@process_create_bp.route('/process_create', methods=['GET', 'POST'])
def process_create():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            description = request.form.get('description')
            duration_in_days = request.form.get('duration_in_days')
            cost_in_inr = request.form.get('cost_in_inr')
            item_id = request.form.get('item_id')
            maker_id = request.form.get('maker_id')

            if not all([name, duration_in_days, cost_in_inr, item_id, maker_id]):
                flash(" fields cannot be empty!", "danger")
                return redirect(url_for('process_create.process_create'))

            new_process = Process(
                name=name,
                description=description,
                duration_in_days=int(duration_in_days),
                cost_in_inr=float(cost_in_inr),
                item_id=int(item_id),
                maker_id=int(maker_id)
            )
            
            db.session.add(new_process)
            db.session.commit()
            flash("Process created successfully!", "success")
            return redirect(url_for('main.work.process.process_read.process_read'))
        except Exception as e:
            db.session.rollback()
            flash(f"Error creating process: {str(e)}", "error")
            return redirect(url_for('main.work.process.process_create.process_create'))

    items = Item.query.all()
    makers = Maker.query.all()
    return render_template('process_create.html', items=items, makers=makers)
