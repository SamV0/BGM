from flask import Blueprint

purchase_bp = Blueprint('purchase', __name__)

from .purchase_create import purchase_create_bp
from .purchase_read import purchase_read_bp
from .purchase_update import purchase_update_bp
from .purchase_delete import purchase_delete_bp

purchase_bp.register_blueprint(purchase_create_bp)
purchase_bp.register_blueprint(purchase_read_bp)
purchase_bp.register_blueprint(purchase_update_bp)
purchase_bp.register_blueprint(purchase_delete_bp)

from .supplier import supplier_bp
purchase_bp.register_blueprint(supplier_bp, url_prefix='/supplier')