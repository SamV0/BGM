from flask import Blueprint

maker_bp = Blueprint('maker', __name__, template_folder='templates')

from .maker_create import maker_create_bp
from .maker_read import maker_read_bp
from .maker_update import maker_update_bp
from .maker_delete import maker_delete_bp

maker_bp.register_blueprint(maker_create_bp)
maker_bp.register_blueprint(maker_read_bp)
maker_bp.register_blueprint(maker_update_bp)
maker_bp.register_blueprint(maker_delete_bp)
