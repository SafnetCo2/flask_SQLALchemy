import os
from flask import Flask ,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Employee(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    firstname=db.Column(db.String)
    lastname=db.Column(db.String)
    email=db.Column(db.String)
    age=db.Column(db.Integer)
    hire_date=db.Column(db.Date)
    active=db.Column(db.Boolean)

def __repr__(self):
        return f'<Employee {self.firstname} {self.lastname}>'
if __name__=="__main__":
    app.run()