from flask import Blueprint

rack_bp = Blueprint('rack', __name__)

from .rack_create import rack_create_bp
from .rack_read import rack_read_bp
from .rack_delete import rack_delete_bp

rack_bp.register_blueprint(rack_create_bp, url_prefix='/rack_create')
rack_bp.register_blueprint(rack_read_bp, url_prefix='/rack_read')
rack_bp.register_blueprint(rack_delete_bp, url_prefix='/rack_delete')
