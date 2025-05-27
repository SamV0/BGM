from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.main.inventory.godown.rack.models import Rack
from app.main.inventory.item.models import Item  # Import Item model
from sqlalchemy.exc import IntegrityError

rack_create_bp = Blueprint('rack_create', __name__, template_folder='templates')

@rack_create_bp.route('/rack_create', methods=['GET', 'POST'])
def rack_create():
    from app.main.inventory.godown.models import Godown
    godown_id = request.args.get('godown_id')
    if request.method == 'POST':
        num_racks = int(request.form.get('num_racks'))
        godown_id = request.form.get('godown_id')
        item_ids = request.form.getlist('item_ids')  # Get list of selected item IDs

        existing_racks = Rack.query.filter_by(godown_id=godown_id).all()
        if existing_racks:
            max_rack_number = max(int(rack.name.split()[-1]) for rack in existing_racks if rack.name.split()[-1].isdigit())
        else:
            max_rack_number = 0

        for i in range(num_racks):
            new_rack_number = max_rack_number + i + 1
            godown = Godown.query.get(godown_id)
            new_rack_name = f"{godown.name} - {new_rack_number:03}"
            new_rack = Rack(name=new_rack_name, godown_id=godown_id)

            # Associate selected items with the rack
            for item_id in item_ids:
                item = Item.query.get(item_id)
                if item:
                    new_rack.items.append(item)

            try:
                db.session.add(new_rack)
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                flash(f"Error: Rack {new_rack_name} already exists.", "danger")
                continue

        flash("Racks added successfully!", "success")
        return redirect(url_for('main.inventory.godown.rack.rack_read.rack_read', godown_id=godown_id))

    godown = Godown.query.get(godown_id)
    # Fetch all items for the select field
    items = Item.query.all()
    return render_template('rack_create.html', godown=godown, items=items)
