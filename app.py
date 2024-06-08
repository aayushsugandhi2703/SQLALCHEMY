from flask import Flask, request, jsonify, url_for, redirect, render_template, flash
from model import db, task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    tasks= tasks.query.all()
    return render_template('index.html',tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    description = request.form.get('description')

    added =task(title=title,descriptoin=description)
    db.session.add(added)
    db.session.commit()
    flash("task added ")
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    remove = task.query.get(id)
    if remove:
        db.session.delete(remove)
        db.session.commit()
        flash("task deleted")
    else:
        flash("task not found")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=False)