from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from sqlalchemy.orm import backref



db = SQLAlchemy()
ma = Marshmallow()


class MenteeSignup(db.Model):
    username = db.Column(db.String(100), primary_key = True)
    password = db.Column(db.String(100),nullable=False )   
    name = db.Column(db.String(100),nullable=False )
    phonenumber = db.Column(db.Integer,nullable=False )
    state = db.Column(db.String(50),nullable=False )
    interest1 = db.Column(db.String(30),nullable=False )
    interest2 = db.Column(db.String(30),nullable=False )
    interest3 = db.Column(db.String(30),nullable=False )
    career = db.Column(db.String(40),nullable=False )
    gender_preference = db.Column(db.String(10),nullable=False )
    language = db.Column(db.String(10),nullable=False )

    def __init__(self, username, password, name, phonenumber, state,
    	interest1,interest2,interest3,career,gender_preference,language):
        self.username = username
        self.password =password
        self.name = name
        self.phonenumber = phonenumber
        self.state = state
        self.interest1 = interest1
        self.interest2 = interest2
        self.interest3 = interest3
        self.career = career
        self.gender_preference= gender_preference
        self.language = language

    
class MenteeSchema(ma.Schema):
    class Meta:
        fields = ("username", "password","name", "phonenumber", "state","interest1","interest2","interest3","career", "gender_preference","language")

class MentorSignup(db.Model):
    username = db.Column(db.String(100), primary_key = True)
    password = db.Column(db.String(100),nullable=False )   
    name = db.Column(db.String(100),nullable=False )
    phonenumber = db.Column(db.Integer,nullable=False )
    state = db.Column(db.String(50),nullable=False )
    interest1 = db.Column(db.String(30),nullable=False )
    interest2 = db.Column(db.String(30),nullable=False )
    interest3 = db.Column(db.String(30),nullable=False )
    gender = db.Column(db.String(10),nullable=False )
    career = db.Column(db.String(40),nullable=False )
    no_of_students = db.Column(db.Integer,nullable=False )
    language = db.Column(db.String(10),nullable=False )

    def __init__(self, username, password,  name, phonenumber, state,
    	interest1,interest2,interest3,career,gender,no_of_students,language):
        self.username = username
        self.password =password
        self.name = name
        self.phonenumber = phonenumber
        self.state = state
        self.interest1 = interest1
        self.interest2 = interest2
        self.interest3 = interest3
        self.gender = gender
        self.career = career
        self.no_of_students= no_of_students
        self.language = language

    
class MentorSchema(ma.Schema):
    class Meta:
        fields = ("username", "password", "name","phonenumber", "state","interest1","interest2",
        	"interest3","gender","career","no_of_students","language")


class MentorMentee(db.Model):
    mentor_username = db.Column(db.String(100), primary_key = True)
    mentee_username = db.Column(db.String(100), primary_key = True)

    def __init__(self, mentor_username, mentee_username):
        self.mentor_username = mentor_username
        self.mentee_username = mentee_username

class MentorMenteeSchema(ma.Schema):
    class Meta:
        fields = ("mentor_username", "mentee_username")


#Init Schema
mentee_schema = MenteeSchema()
mentee_schemas = MenteeSchema(many=True)

mentor_schema = MentorSchema()
mentor_schemas = MentorSchema(many=True)

mentormentee_schema = MentorMenteeSchema()
mentormentee_schemas = MentorMenteeSchema(many=True)

def db_initialiser(app):
    db.init_app(app)
    ma.init_app(app)
    with app.app_context():
        pass
        # db.drop_all()
        # db.create_all()
