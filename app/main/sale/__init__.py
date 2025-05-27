from flask import Blueprint

sale_bp = Blueprint('sale', __name__)

from .sale_create import sale_create_bp
from .sale_read import sale_read_bp
from .sale_update import sale_update_bp
from .sale_delete import sale_delete_bp

sale_bp.register_blueprint(sale_create_bp)
sale_bp.register_blueprint(sale_read_bp)
sale_bp.register_blueprint(sale_update_bp)
sale_bp.register_blueprint(sale_delete_bp)

from .customer import customer_bp
sale_bp.register_blueprint(customer_bp)