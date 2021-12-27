from flask import Blueprint, Response, request, jsonify
from database.models import MenteeSignup, MentorSignup, db, ma , MentorMentee
import bcrypt
import json

loginblue = Blueprint("loginblue", __name__) 

# login
@loginblue.route('/login/mentee', methods=['POST'])
def login_mentee():
    username = request.json['username']
    password = request.json['password']

    signup_mentee = MenteeSignup.query.get(username)

    if signup_mentee:
    	if bcrypt.checkpw(password.encode('utf-8'), signup_mentee.password):
    		return jsonify({'code': 200})
    	else:
    		return jsonify({'code': 405})
    else:
    	return jsonify({'code':403})

# login
@loginblue.route('/login/mentor', methods=['POST'])
def login_mentor():
    username = request.json['username']
    password = request.json['password']

    signup_mentor = MentorSignup.query.get(username)

    if signup_mentor:
    	if bcrypt.checkpw(password.encode('utf-8'), signup_mentor.password):
    		return jsonify({'code': 200})
    	else:
    		return jsonify({'code': 405})
    else:
    	return jsonify({'code':403})

#to add too mentorMentee table for testing
@loginblue.route('/mm', methods=['POST'])
def mm():
    mentor_user = request.json["mentor_user"]
    mentee_user = request.json["mentee_user"]

    if not mentor_user:
        return jsonify({"code": 404})
    elif not mentee_user:
        return jsonify({"code": 404})

    entry = MentorMentee(mentor_user, mentee_user)
    db.session.add(entry)
    db.session.commit()

    return jsonify({"code": 200})
