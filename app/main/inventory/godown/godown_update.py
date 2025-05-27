from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from .models import Godown

godown_update_bp = Blueprint('godown_update', __name__, template_folder='templates')

@godown_update_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def godown_update(id):
    godown = Godown.query.get_or_404(id)
    if request.method == 'POST':
        name = request.form.get('name')
        if not name:
            flash("Godown name is required!", "danger")
            return redirect(url_for('main.inventory.godown.godown_update.godown_update', id=id))
        godown.name = name
        db.session.commit()
        flash("Godown updated successfully!", "success")
        return redirect(url_for('main.inventory.godown.godown_read.godown_read'))
    return render_template('godown_update.html', godown=godown)
