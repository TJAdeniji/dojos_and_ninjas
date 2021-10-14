from flask_app import app   
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojoPage():
    dojos = Dojo.getDojo()
    return render_template('dojos.html', dojos = dojos)

@app.route('/dojos/addDojos', methods = ['POST'])
def addDojos():
    dojo = Dojo.addDojo(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def showDojo(dojo_id):
    data = {
        'id' : dojo_id
    }
    dojo = Dojo.getDojosWithNinjas(data)
    return render_template('show_dojos.html', dojo = dojo) 




