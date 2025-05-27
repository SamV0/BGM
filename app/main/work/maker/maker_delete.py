from flask import Blueprint, redirect, url_for, flash
from app import db
from .models import Maker

maker_delete_bp = Blueprint('maker_delete', __name__)

@maker_delete_bp.route('/maker_delete/<int:maker_id>', methods=['POST'])
def maker_delete(maker_id):
    maker = Maker.query.get_or_404(maker_id)
    try:
        db.session.delete(maker)
        db.session.commit()
        flash("Maker deleted successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting maker: {str(e)}", "error")
    
    return redirect(url_for('main.work.maker.maker_read.maker_read'))
