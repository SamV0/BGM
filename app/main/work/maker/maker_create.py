from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from .models import Maker

maker_create_bp = Blueprint('maker_create', __name__, template_folder='templates')

@maker_create_bp.route('/maker_create', methods=['GET', 'POST'])
def maker_create():
    if request.method == 'POST':
        try:
            name = request.form['name']
            address = request.form['address']
            phone = request.form['phone']
            alt_phone = request.form.get('alt_phone')
            remarks = request.form.get('remarks')

            new_maker = Maker(
                name=name,
                address=address,
                phone=phone,
                alt_phone=alt_phone,
                remarks=remarks
            )
            
            db.session.add(new_maker)
            db.session.commit()
            flash("Maker created successfully!", "success")
            return redirect(url_for('main.work.maker.maker_read.maker_read'))
        except Exception as e:
            db.session.rollback()
            flash(f"Error creating maker: {str(e)}", "error")
            return redirect(url_for('main.work.maker.maker_create.maker_create'))

    return render_template('maker_create.html')