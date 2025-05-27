from flask import Blueprint

process_bp = Blueprint('process', __name__)

from .process_create import process_create_bp
from .process_read import process_read_bp
from .process_update import process_update_bp
from .process_delete import process_delete_bp

process_bp.register_blueprint(process_create_bp)
process_bp.register_blueprint(process_read_bp)
process_bp.register_blueprint(process_update_bp)
process_bp.register_blueprint(process_delete_bp)
