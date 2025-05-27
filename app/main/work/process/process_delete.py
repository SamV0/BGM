from flask import Blueprint, redirect, url_for, flash
from app import db
from .models import Process

process_delete_bp = Blueprint('process_delete', __name__)

@process_delete_bp.route('/process_delete/<int:id>', methods=['POST'])
def process_delete(id):
    process = Process.query.get_or_404(id)
    try:
        db.session.delete(process)
        db.session.commit()
        flash("Process deleted successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting process: {str(e)}", "error")
    
    return redirect(url_for('main.work.process.process_read.process_read'))
