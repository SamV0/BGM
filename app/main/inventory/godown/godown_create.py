from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from .models import Godown
from .rack.models import Rack

godown_create_bp = Blueprint('godown_create', __name__, template_folder='templates')

@godown_create_bp.route('/create', methods=['GET', 'POST'])
def godown_create():
    if request.method == 'POST':
        name = request.form['name']
        num_racks = int(request.form.get('num_racks', 0))

        new_godown = Godown(name=name)
        db.session.add(new_godown)
        db.session.commit()

        # Create racks if specified
        for i in range(num_racks):
            rack_name = f"{name} - {i+1:03}"
            new_rack = Rack(name=rack_name, godown_id=new_godown.id)
            db.session.add(new_rack)
        
        db.session.commit()
        flash("Godown created successfully!", "success")
        return redirect(url_for('main.inventory.godown.godown_read.godown_read'))
    return render_template('godown_create.html')
