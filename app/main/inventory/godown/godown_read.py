from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from .models import Godown

godown_read_bp = Blueprint('godown_read', __name__, template_folder='templates')

@godown_read_bp.route('/read', methods=['GET'])
def godown_read():
    godowns = Godown.query.all()
    return render_template('godown_read.html', godowns=godowns)
