from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from .models import Maker

maker_update_bp = Blueprint('maker_update', __name__, template_folder='templates')

@maker_update_bp.route('/maker_update/<int:maker_id>', methods=['GET', 'POST'])
def maker_update(maker_id):
    maker = Maker.query.get_or_404(maker_id)
    
    if request.method == 'POST':
        try:
            maker.name = request.form['name']
            maker.address = request.form['address']
            maker.phone = request.form['phone']
            maker.alt_phone = request.form.get('alt_phone')
            maker.is_active = 'is_active' in request.form
            maker.remarks = request.form.get('remarks')
            
            db.session.commit()
            flash("Maker updated successfully!", "success")
            return redirect(url_for('main.work.maker.maker_read.maker_read'))
        except Exception as e:
            db.session.rollback()
            flash(f"Error updating maker: {str(e)}", "error")
            return redirect(url_for('main.work.maker.maker_update.maker_update', maker_id=maker_id))

    return render_template('maker_update.html', maker=maker)
