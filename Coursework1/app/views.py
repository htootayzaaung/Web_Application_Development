from flask import render_template, flash, redirect, request
from datetime import datetime, date
from flask_sqlalchemy import SQLAlchemy
from app import app, models, db
from .models import data
from .forms import input_form


#GET - This method is used to retrieve information to the web server.
#POST - This method is used to send information to the web server. It is used to get the data from the form.

@app.route('/')
def index():


    data = models.data.query.all()
    return render_template('all_assessments.html', title='All Assessment',data = data)

@app.route('/create_assessments', methods=['GET', 'POST'])
def inputform():
    form = input_form()
    if form.is_submitted():                                                                     #checks if the form is actually submitted

           title = request.form['title']                                                        #requests title from the form
           module_code = request.form['module_code']                                            #requests module_code from the form
           deadline = request.form['deadline']                                                  #requests deadline from the form 
           deadtime = datetime.strptime(deadline,'%m-%d-%Y').date()                             #date format: month-date-year
           description = request.form['description']                                            #requests description from the form
           status = 'INCOMPLETE'                                                                #by deafult the status is INCOMPELETE
           record = data(title,module_code,deadtime,description,status)                         #each instance of a record now contains the single element of title, module_code, deadtime, descritption and status
           db.session.add(record)                                                               #adds this record tuple to the database
           db.session.commit()                                                                  #commits to the database
           return redirect('/')

    return render_template('create_assessments.html',title='Create Assessment',form=form)       #shows the contents from create_assessments.html

@app.route('/uncompleted', methods=['GET', 'POST'])                                             #records will be retrieved from the server and will be posted to the server.
def incomplete():
    result = data.query.filter_by(status='INCOMPLETE')                                          #selectively chooses the records whenever the status is marked as "INCOMPLETE"
    return render_template('uncompleted.html', title='Uncomplete Assessment', data=result)      #shows the contents from uncompleted.html

@app.route('/uncompleted/<id>', methods=['GET', 'POST'])                                        #records will be retrieved from the server and will be posted to the server.
def uncomplete(id):
    ids = int(id)

    if request.method == 'POST':                                                                #checks if the request's method is "POST"
        admin=data.query.filter_by(id = ids).first()
        admin.status = 'COMPLETED'
        db.session.commit()                                                                     #commits to the database
    return redirect('/completed')

@app.route('/completed', methods=['GET', 'POST'])                                               #records will be retrieved from the server and will be posted to the server.
def complete():

    result = data.query.filter_by(status='COMPLETED')                                           #selectively chooses the records whenever the status is marked as "COMPLETED" 

    return render_template('completed.html', title='Complete Assessment',data=result)           #shows the contents from completed.html