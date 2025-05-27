from flask import Blueprint

work_bp = Blueprint('work', __name__, url_prefix='/work')

from .work_create import work_create_bp
from .work_read import work_read_bp
from .work_update import work_update_bp
from .work_delete import work_delete_bp

work_bp.register_blueprint(work_create_bp)
work_bp.register_blueprint(work_read_bp)
work_bp.register_blueprint(work_update_bp)
work_bp.register_blueprint(work_delete_bp)

from .maker import maker_bp
work_bp.register_blueprint(maker_bp, url_prefix='/maker')

from .process import process_bp
work_bp.register_blueprint(process_bp, url_prefix='/process')