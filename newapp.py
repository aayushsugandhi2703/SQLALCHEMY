from flask import Flask, request, render_template, flash, redirect, url_for
from newmodel import Session, Info
from form import createform
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newdatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')

session = Session()

@app.route('/', methods=['GET'])
def index():
    form = createform()
    try:
        info = session.query(Info).all()
        return render_template('new.html', form=form, info=info)
    except Exception as e:
        flash("An error occurred while fetching info. Please try again later.")
        return render_template('new.html', form=form, info=[])

@app.route('/create', methods=['POST'])
def create():
    form = createform()
    if form.validate_on_submit():
        try:
            id = form.id.data
            name = form.name.data
            age = form.age.data
            add = Info(id=id, name=name, age=age)
            session.add(add)
            session.commit()
            flash("Info added")
            return redirect(url_for('index'))  # Redirect to index after adding info
        except Exception as e:
            flash("An error occurred while adding info. Please try again later.")
            return redirect(url_for('index'))  # Redirect to index if database operation fails
    else:
        flash("Form validation failed. Please check your inputs.")
        return redirect(url_for('index'))  # Redirect to index if form validation fails

if __name__ == '__main__':
    app.run(debug=True)
