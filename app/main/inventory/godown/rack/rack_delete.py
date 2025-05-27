from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from .models import Rack
from app.main.inventory.godown.models import Godown

rack_delete_bp = Blueprint('rack_delete', __name__, template_folder='templates')

@rack_delete_bp.route('/rack_delete', methods=['GET', 'POST'])
def rack_delete():
    godown_id = request.args.get('godown_id')
    godown = Godown.query.get(godown_id)

    if request.method == 'POST':
        num_racks_to_delete = int(request.form.get('num_racks_to_delete'))
        if num_racks_to_delete <= 0:
            flash("Number of racks to delete must be positive.", "danger")
            return redirect(url_for('main.inventory.godown.rack.rack_read.rack_read', godown_id=godown_id))

        racks_to_delete = Rack.query.filter_by(godown_id=godown_id).order_by(Rack.id.desc()).limit(num_racks_to_delete).all()

        if not racks_to_delete:
            flash('No racks found to delete.', 'danger')
            return redirect(url_for('main.inventory.godown.rack.rack_read.rack_read', godown_id=godown_id))
        
        deleted_count = 0
        for rack in racks_to_delete:
            db.session.delete(rack)
            deleted_count += 1
        db.session.commit()

        flash(f'{deleted_count} racks deleted successfully!', 'success')
        return redirect(url_for('main.inventory.godown.rack.rack_read.rack_read', godown_id=godown_id))

    return render_template('rack_delete.html', godown=godown)
