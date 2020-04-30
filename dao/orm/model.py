from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = 'some secret salt'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:123@localhost/Diplom'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)


db.create_all()

from app import db



class Student(db.Model):
    __tablename__ = 'student'

    student_id = db.Column(db.Integer, primary_key=True)
    student_username = db.Column(db.String(80), primary_key=True)
    student_name = db.Column(db.String(20), nullable=False)
    student_lastname = db.Column(db.String(30), nullable=False)
    student_birthday =  db.Column(db.String(20), nullable=False)
    student_group = db.Column(db.String(20), nullable=False)
    student_mail = db.Column(db.String(40), nullable=False)
    student_password = db.Column(db.String(20), nullable=False)
    # student_photo = db.Column(db.text, nullable=False)
    student_grades = db.Column(db.Integer, nullable=False)
    student_proglanguage = db.Column(db.String(40), nullable=False)
    student_specialization = db.Column(db.String(40), nullable=False)


class Teacher(db.Model):
    __tablename__ = 'teacher'

    teacher_id = db.Column(db.Integer, primary_key=True)
    teacher_username = db.Column(db.Integer, primary_key=True)
    teacher_name = db.Column(db.String(20), nullable=False)
    teacher_lastname = db.Column(db.String(20), nullable=False)
    teacher_birthday = db.Column(db.String(20), nullable=False)
    teacher_position = db.Column(db.String(20), nullable=False)
    teacher_subject = db.Column(db.String(20), nullable=False)
    teacher_mail = db.Column(db.String(20), nullable=False)
    teacher_password = db.Column(db.String(20), nullable=False)
    # teacher_photo = db.Column(db.text, nullable=False)
    teacher_hobby = db.Column(db.String(20), nullable=False)
    teacher_proglanguage = db.Column(db.String(20), nullable=False)
    teacher_item = db.Column(db.String(20), nullable=False)
    teacher_works = db.Column(db.String(20), nullable=False)
    teacher_specialization = db.Column(db.String(20), nullable=False)



class diplomItem(db.Model):
    __tablename__ = 'diplomItem'

    diplomItem_id = db.Column(db.Integer, primary_key=True)
    diplomItem_name = db.Column(db.String(300), nullable=False)
    diplomItem_subject = db.Column(db.String(150), nullable=False)
    diplomItem_proglanguage=db.Column(db.String(50), nullable=False)
    diplomItem_teacher=db.Column(db.String(50), nullable=False)

class diplomWork(db.Model):
    __tablename__ = 'diplomWork'

    diplomWork_id = db.Column(db.Integer, primary_key=True)
    diplomWork_name = db.Column(db.String(300), primary_key=True)
    diplomWork_proglanguage = db.Column(db.String(50), nullable=False)
    diplomWork_subject= db.Column(db.String(100), nullable=False)
    diplomWork_specialization= db.Column(db.Integer, nullable=False)
    diplomWork_teacher= db.Column(db.String(100), nullable=False)
