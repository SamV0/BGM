from flask import Blueprint

item_bp = Blueprint('item', __name__)

from .item_create import item_create_bp
from .item_read import item_read_bp
from .item_update import item_update_bp
from .item_delete import item_delete_bp

item_bp.register_blueprint(item_create_bp, url_prefix='/item_create')
item_bp.register_blueprint(item_read_bp, url_prefix='/item_read')
item_bp.register_blueprint(item_update_bp, url_prefix='/item_update')
item_bp.register_blueprint(item_delete_bp, url_prefix='/item_delete')