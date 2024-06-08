from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class task(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(200))

    def __repr__(self): 
        return f'<Task(id={self.id}, title={self.title}, description={self.description})>'

def create_table():
    db.create_all()
