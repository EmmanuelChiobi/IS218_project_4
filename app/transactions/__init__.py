import csv
import logging
import os
import json

from flask import Blueprint, render_template, abort, url_for, current_app, jsonify, Response
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound

from app.db import db 
from app.db.models import Transaction
from app.transactions.forms import csv_upload
from werkzeug.utils import secure_filename, redirect

transactions = Blueprint('transactions', __name__, template_folder='templates')

@transactions.route('/transactions', methods=['GET'], defaults={"page": 1})
@transactions.route('/transactions/<int:page>', methods=['GET'])
def transaction_browse(page):
    pg = page
    per_page = 1000
    pagination = Transaction.query.paginate(pg, per_page, error_out=False)
    data = pagination.items
    try:
        return render_template('browse_transactions.html', data=data, pagination=pagination)
    except TemplateNotFound:
        abort(404)

@transactions.route('/transactions_datatables/', methods=['GET'])
def datatable_location_browse():
    transaction_data = Transaction.query.all()
    try:
        return render_template('browse_transaction_datatables.html', data=transaction_data)
    except TemplateNotFound:
        abort(404)

@transactions.route('/transactions/upload', methods=['POST', 'GET'])
@login_required
def transactions_upload():
    form = csv_upload()
    if form.validate_on_submit():
        fname = secure_filename(form.file.data.filename)
        fpath = os.path.join(current_app.config['UPLOAD_FOLDER'], fname)
        form.file.data.save(fpath)
        list_of_transactions = []
        current_user.balance = 0.00
        with open(fpath) as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                transaction = Transaction.query.filter_by(AMOUNT=row['\ufeffAMOUNT']).first()
                if transaction is None:
                    current_user.balance += row['\ufeffAMOUNT']
                    current_user.transactions.append(Transaction(row['\ufeffAMOUNT'], row['TYPE']))
                    db.session.commit()
                else:
                    current_user.transactions.append(transaction)
                    db.session.commit()
        
        current_user.transactions = list_of_transactions
        db.session.commit()

        return redirect(url_for('transactions.transactions_browse'))
    
    try:
        return render_template('upload.html', form=form)
    except TemplateNotFound:
        abort(404)