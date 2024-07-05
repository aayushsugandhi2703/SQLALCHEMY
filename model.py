from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
"""creted the schema for the database

Keyword arguments:
argument -- used constraints and data typesfor defining the table
Return: return_description
"""

class Task(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(200))

    def __repr__(self): 
        return f'<Task(id={self.id}, title={self.title}, description={self.description})>'
    
#creating the table in the database
def create_table():
    db.create_all()
