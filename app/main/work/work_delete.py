from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from .models import Work

work_delete_bp = Blueprint('work_delete', __name__)

@work_delete_bp.route('/work_delete/<int:work_id>', methods=['GET', 'POST'])
def work_delete(work_id):
    work_item = Work.query.get_or_404(work_id)
    db.session.delete(work_item)
    db.session.commit()
    flash("Work deleted successfully!", "success")
    return redirect(url_for('main.work.work_read.work_read'))