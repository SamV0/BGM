from flask import Blueprint

godown_bp = Blueprint('godown', __name__)

from .godown_create import godown_create_bp
from .godown_read import godown_read_bp
from .godown_update import godown_update_bp
from .godown_delete import godown_delete_bp

godown_bp.register_blueprint(godown_create_bp, url_prefix='/godown_create')
godown_bp.register_blueprint(godown_read_bp, url_prefix='/godown_read')
godown_bp.register_blueprint(godown_update_bp, url_prefix='/godown_update')
godown_bp.register_blueprint(godown_delete_bp, url_prefix='/godown_delete')

from .rack import rack_bp
godown_bp.register_blueprint(rack_bp, url_prefix='/rack')