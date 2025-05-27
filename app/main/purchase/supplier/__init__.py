from flask import Blueprint

supplier_bp = Blueprint('supplier', __name__)

from .supplier_create import supplier_create_bp
from .supplier_read import supplier_read_bp
from .supplier_update import supplier_update_bp
from .supplier_delete import supplier_delete_bp

supplier_bp.register_blueprint(supplier_create_bp)
supplier_bp.register_blueprint(supplier_read_bp)
supplier_bp.register_blueprint(supplier_update_bp)
supplier_bp.register_blueprint(supplier_delete_bp)