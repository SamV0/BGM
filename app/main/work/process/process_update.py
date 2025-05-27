from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from .models import Process
from app.main.inventory.item.models import Item
from app.main.work.maker.models import Maker

process_update_bp = Blueprint('process_update', __name__, template_folder='templates')

@process_update_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def process_update(id):
    process = Process.query.get_or_404(id)
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            description = request.form.get('description')
            duration_in_days = request.form.get('duration_in_days')
            cost_in_inr = request.form.get('cost_in_inr')
            item_id = request.form.get('item_id')
            maker_id = request.form.get('maker_id')
            is_active = 'is_active' in request.form

            if not all([name, duration_in_days, cost_in_inr, item_id, maker_id]):
                flash(" fields cannot be empty!", "danger")
                return redirect(url_for('main.work.process.process_update.process_update', id=id))

            process.name = name
            process.description = description
            process.duration_in_days = int(duration_in_days)
            process.cost_in_inr = float(cost_in_inr)
            process.item_id = int(item_id)
            process.maker_id = int(maker_id)
            process.is_active = is_active
            
            db.session.commit()
            flash("Process updated successfully!", "success")
            return redirect(url_for('main.work.process.process_read.process_read'))
        except Exception as e:
            db.session.rollback()
            flash(f"Error updating process: {str(e)}", "error")
            return redirect(url_for('main.work.process.process_update.process_update', id=id))

    items = Item.query.all()
    makers = Maker.query.all()
    return render_template('process_update.html', process=process, items=items, makers=makers)
