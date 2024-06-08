from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class task(db.Model):
    id = db.column(db.integer, primary_key =True)
    title = db.column(db.string(100))
    description = db.column(db.string(200))
    done = db.column(db.boolean)

def __repr__(self):
    return f'<Task({self.title}:{self.description})>'
