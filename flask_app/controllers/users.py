from flask_app import app
from flask import render_template, redirect, session, request

@app.route('/lists')
def render_lists():

    names_info = [
        {'first_name' : 'Michael', 'last_name' : 'Choi','full_name': 'Michael Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin', 'full_name':'John Supsupin' },
        {'first_name' : 'Mark', 'last_name' : 'Guillen', 'full_name': 'Mark Guillen'}
    ]
    return render_template("dashboard.html",names=names_info)