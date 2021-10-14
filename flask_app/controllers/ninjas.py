from flask_app import app   
from flask import render_template, redirect, request, session, templating
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask_app.models import ninja, dojo


@app.route('/ninjas')
def ninjaPage():
    dojos = Dojo.getDojo()
    return render_template('ninjas.html', dojos = dojos)

@app.route('/ninjas/new', methods = ['POST'])
def addNinjas():
    ninja.Ninja.addNinja(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")

