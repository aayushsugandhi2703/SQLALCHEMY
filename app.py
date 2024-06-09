from flask import Flask, request, jsonify, url_for, redirect, render_template, flash
from model import db, Task 
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')

db.init_app(app)

@app.route('/')
def index():
    tasks = Task.query.all()  
    return render_template('index.html', tasks=tasks)

@app.route('/create', methods=['POST'])
def create():
    title = request.form.get('title')
    description = request.form.get('description')

    added = Task(title=title, description=description)  
    db.session.add(added)
    db.session.commit()
    flash("Task added")
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    remove = Task.query.get(id) 
    if remove:
        db.session.delete(remove)
        db.session.commit()
        flash("Task deleted")
    else:
        flash("Task not found")
    return redirect(url_for('index'))

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

if __name__ == '__main__':
     with app.app_context():
        db.create_all() 
     app.run(debug=True)
