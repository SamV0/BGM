from flask import Blueprint, render_template, request, abort
from .models import Rack
from app.main.inventory.godown.models import Godown

rack_read_bp = Blueprint('rack_read', __name__, template_folder='templates', static_folder='static')

@rack_read_bp.route('/read', methods=['GET'])
def rack_read():
    godown_id = request.args.get('godown_id', type=int)
    if not godown_id:
        abort(400, description="Godown ID is required.")
        
    godown = Godown.query.get_or_404(godown_id)
    
    racks = Rack.query.filter_by(
        godown_id=godown_id
    ).order_by(Rack.name).all()

    return render_template('rack_read.html', racks=racks, godown=godown)
