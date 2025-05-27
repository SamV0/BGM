from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.main.inventory.godown.rack.models import Rack
from app.main.inventory.item.models import Item  # Import Item model

rack_update_bp = Blueprint('rack_update', __name__, template_folder='templates')

@rack_update_bp.route('/rack_update/<int:id>', methods=['GET', 'POST'])
def rack_update(id):
    rack = Rack.query.get_or_404(id)
    from app.main.inventory.godown.models import Godown
    godown = Godown.query.get(rack.godown_id)

    if request.method == 'POST':
        rack.name = request.form.get('name')
        item_ids = request.form.getlist('item_ids')  # Get list of selected item IDs

        # Clear existing item associations
        rack.items = []

        # Associate selected items with the rack
        for item_id in item_ids:
            item = Item.query.get(item_id)
            if item:
                rack.items.append(item)

        try:
            db.session.commit()
            flash("Rack updated successfully!", "success")
            return redirect(url_for('main.inventory.godown.rack.rack_read.rack_read', godown_id=rack.godown_id))
        except Exception as e:
            db.session.rollback()
            flash(f"Error updating rack: {e}", "danger")

    # Fetch all items for the select field
    items = Item.query.all()
    return render_template('rack_update.html', rack=rack, godown=godown, items=items)
