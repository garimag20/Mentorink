from flask import Blueprint, Response, request, jsonify
from database.models import MenteeSignup, MentorSignup, db, ma 
import bcrypt
import json
from csv import writer
import os 

signblue = Blueprint("signblue", __name__)

# adding mentee sign up data to db
@signblue.route("/signup/mentee", methods=['POST'])
def mentee_signup():
    username = request.json["username"]
    password = request.json["password"]
    name = request.json["name"]
    phonenumber = request.json["phonenumber"]
    state = request.json["state"]
    interest1 = request.json["interest1"]
    interest2 = request.json["interest2"]
    interest3 = request.json["interest3"]
    career = request.json["career"]
    gender_preference = request.json["gender_preference"]
    language = request.json["language"]

    # to check if they already exist in  mentee signup
    mentee_in_signup = MenteeSignup.query.get(username)
    if mentee_in_signup:
        
        #username already exists in mentee signup
        return jsonify({'code':402})

    hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    #creating row for menteeSignup Table
    new_mentee_signup = MenteeSignup(username, hashed_pwd, name, phonenumber, state, interest1, interest2, interest3, career, gender_preference, language)

    # adding to MenteeSignup Table
    db.session.add(new_mentee_signup)
    db.session.commit()

    #return confirmation
    return jsonify({'code':200})

# adding mentor sign up data to db
@signblue.route("/signup/mentor", methods=['POST'])
def mentor_signup():
    username = request.json["username"]
    password = request.json["password"]
    name = request.json["name"]
    phonenumber = request.json["phonenumber"]
    state = request.json["state"]
    interest1 = request.json["interest1"]
    interest2 = request.json["interest2"]
    interest3 = request.json["interest3"]
    gender = request.json["gender"]
    career = request.json["career"]
    no_of_students = request.json["no_of_students"]
    language = request.json["language"]

    # to check if they already exist in mentor signup
    mentor_in_signup = MentorSignup.query.get(username)
    if mentor_in_signup:
        
        #username already exists in  mentor signup
        return jsonify({'code':402})

    hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    #creating row for menteeSignup Table
    new_mentor_signup = MentorSignup(username, hashed_pwd, name, phonenumber, state, interest1, interest2, interest3, gender, career, no_of_students, language)

    # adding to MenteeSignup Table
    db.session.add(new_mentor_signup)
    db.session.commit()

    #adding to csv file in ML folder
    mentor_data = [username, state, interest1, interest2, interest3, gender, career, language]

    basedir = os.path.abspath(os.path.dirname(__file__))
    csv_addr = os.path.join(basedir, 'ML/mentor_data.csv')

    with open(str(csv_addr), 'a+', newline='') as f:

        writer_object = writer(f)
        writer_object.writerow(mentor_data)
        f.close()

    #return confirmation
    return jsonify({'code':200})

# delete account in mentee
@signblue.route('/delete/mentee/<username>', methods=['DELETE'])
def delete_mentee_signup(username):
    mentee_signup_info = MenteeSignup.query.get(username)

    #check if the mentee username exists
    if not mentee_signup_info:
        return jsonify({'code':403})

    db.sesssion.delete(mentee_signup_info)
    db.session.commit()

    return jsonify({'code':200})

# delete account in mentor
@signblue.route('/delete/mentor/<username>', methods=['DELETE'])
def delete_mentor_signup(username):
    mentor_signup_info = MentorSignup.query.get(username)

    #check if the mentor username exists
    if not mentor_signup_info:
        return jsonify({'code':403})

    db.sesssion.delete(mentor_signup_info)
    db.session.commit()

    return jsonify({'code':200})


@signblue.route('/username/check', methods=['POST'])
def check_username():
    username = request.json["username"]
    mentor_signup_info = MentorSignup.query.get(username)
    mentee_signup_info = MenteeSignup.query.get(username)

    if not mentor_signup_info:
        if not mentee_signup_info:
            return jsonify({"code": 200})
        else:
            return jsonify({"code":403})
    else:
        return jsonify({"code" : 403})



# MAYBE CODING "CHANGE PASSWORD" FOR BOTH MENTOR AND MENTEE