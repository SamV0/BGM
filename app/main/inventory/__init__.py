from flask import Blueprint

inventory_bp = Blueprint('inventory', __name__, url_prefix='/inventory')

from .inventory_create import inventory_create_bp
from .inventory_read import inventory_read_bp
from .inventory_update import inventory_update_bp
from .inventory_delete import inventory_delete_bp

inventory_bp.register_blueprint(inventory_create_bp)
inventory_bp.register_blueprint(inventory_read_bp)
inventory_bp.register_blueprint(inventory_update_bp)
inventory_bp.register_blueprint(inventory_delete_bp)

from .item import item_bp
inventory_bp.register_blueprint(item_bp)

from .godown import godown_bp
inventory_bp.register_blueprint(godown_bp)

from .bom import bom_bp
inventory_bp.register_blueprint(bom_bp)
