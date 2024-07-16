from flask import Flask, request, render_template, flash, redirect, url_for
from newmodel import Session, base, Info
from form import createform
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newdatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')

session = Session()

@app.route('/', methods=['GET'])
def index():
    forms = createform()
    try:
        info = session.query(Info).all()
        for item in info:
            print(f"Retrieved from DB: {item.id} - {item.name} - {item.age}")
        return render_template('new.html', forms=forms, info=info)
    except Exception as e:
        flash("An error occurred while fetching info. Please try again later.")
        return render_template('new.html', forms=forms, info=[])

@app.route('/register', methods=['POST'])
def create():
    forms = createform()
    if forms.validate_on_submit():
        try:
            name = forms.name.data
            age = forms.age.data
            add = Info(name=name, age=age)
            session.add(add)
            session.commit()
            flash("Info added")
            return redirect(url_for('index'))
        except Exception as e:
            flash("An error occurred while adding info. Please try again later.")
            return redirect(url_for('index'))
    else:
        flash("Form validation failed. Please check your inputs.")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
