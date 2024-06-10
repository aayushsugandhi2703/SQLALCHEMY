from flask import Flask, request, jsonify, url_for, redirect, render_template, flash
from model import db, Task 
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'                          #creted and linked the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False                                 #to suppress the warning
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')             #to implement the secret key

db.init_app(app)

#this is for displaying the index page with all the tasks
@app.route('/')
def index():
    try:
        tasks = Task.query.all()
        return render_template('index.html', tasks=tasks)                           #returning the tasks to the index.html if no error occurs
    except Exception as e:
        flash("An error occurred while fetching tasks. Please try again later.")
        return render_template('index.html', tasks=[])                              # return empty list if error occurs

# this is for creating the task
@app.route('/create', methods=['POST'])
def create():
    try:
        title = request.form.get('title')
        description = request.form.get('description')

        added = Task(title=title, description=description)  

        db.session.add(added)
        db.session.commit()
        flash("Task added")
        return redirect(url_for('index'))                                          # adding the task and returning to the index page if no error occurs
    except Exception as e:
        flash("An error occurred while adding task. Please try again later.")
        return redirect(url_for('index'))                                          #returning to the index page if error occurs

#this is for deleting the task
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    try:
        remove = Task.query.get(id) 
        if remove:
            db.session.delete(remove)
            db.session.commit()
            flash("Task deleted")
        else:
            flash("Task not found")
        return redirect(url_for('index'))                                          # deletes the task and returning to the index page if no error occurs
    except Exception as e:
        flash("An error occurred while deleting task. Please try again later.")
        return redirect(url_for('index'))                                          #returning to the index page if error occurs

#this is for updating the task
@app.route('/update/<int:id>', methods=['POST'])
def updatee(id):
    change = Task.query.get(id)
    if change:
        change.title = request.form.get('title')
        change.description = request.form.get('description')
        db.session.commit()
        flash("Task updated")
    else:
        flash("Task not found")
    return redirect(url_for('index'))

#
if __name__ == '__main__':
     with app.app_context():                #to create the table in the database this is important to write else tablke will not be cretaed and issue arrises
        db.create_all()                      
     app.run(debug=True)
