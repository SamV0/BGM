from flask import Blueprint

bom_bp = Blueprint('bom', __name__)

from ._create import bom_create_bp
from .bom_read import bom_read_bp
from .bom_update import bom_update_bp
from .bom_delete import bom_delete_bp

bom_bp.register_blueprint(bom_create_bp)
bom_bp.register_blueprint(bom_read_bp)
bom_bp.register_blueprint(bom_update_bp)
bom_bp.register_blueprint(bom_delete_bp)