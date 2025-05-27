from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__, template_folder='templates')

@main_bp.route('/', endpoint='main')
def main():
    return render_template('main.html')

from .inventory import inventory_bp
main_bp.register_blueprint(inventory_bp)

from .work import work_bp
main_bp.register_blueprint(work_bp)

from .purchase import purchase_bp
main_bp.register_blueprint(purchase_bp)

from .sale import sale_bp
main_bp.register_blueprint(sale_bp)