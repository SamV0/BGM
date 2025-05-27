from flask import Blueprint

customer_bp = Blueprint('customer', __name__, url_prefix='/customers')

from .customer_create import customer_create_bp
from .customer_read import customer_read_bp
from .customer_update import customer_update_bp
from .customer_delete import customer_delete_bp

customer_bp.register_blueprint(customer_create_bp)
customer_bp.register_blueprint(customer_read_bp)
customer_bp.register_blueprint(customer_update_bp)
customer_bp.register_blueprint(customer_delete_bp)