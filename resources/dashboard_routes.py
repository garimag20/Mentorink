from flask import Blueprint, Response, request, jsonify
from database.models import MenteeSignup, MentorSignup, db, ma , MentorMentee, mentormentee_schemas
from .ML.model import machine_learning


dashblue = Blueprint("dashblue", __name__)

#to send data of mentees to mentor
@dashblue.route('/dashboard/mentor/<username>', methods=['GET'])
def dash_mentor(username):
    mentor_info = MentorSignup.query.get(username)

    if not mentor_info:
        return jsonify({"code": 406})
    
    mentor_mentees = MentorMentee.query.filter(MentorMentee.mentor_username.like(username)).all()

    mentor_mentees = list(mentor_mentees)

    if len(mentor_mentees) == 0:
        return jsonify({"code" : 403})

    final_mentee = []

    for i in mentor_mentees:

        mentee_stuff = i.mentee_username
        mentee_row = MenteeSignup.query.get(mentee_stuff)
        response1 = {"name" : mentee_row.name, "phonenumber" : mentee_row.phonenumber, "state" : mentee_row.state, "interest1" : mentee_row.interest1, "interest2" : mentee_row.interest2,"interest3" : mentee_row.interest3, "career" : mentee_row.career, "lanuage" : mentee_row.language}

        final_mentee.append(response1)
    
    return jsonify(final_mentee)

# to send data of mentor to mentees
@dashblue.route("/dashboard/mentee/<username>", methods=['GET'])
def dash_mentee(username):

    mentee_info = MenteeSignup.query.get(username)

    if not mentee_info:
        return jsonify({"code": 406})

    mentee_mentor = MentorMentee.query.filter(MentorMentee.mentee_username.like(username)).first()

    # mentee_mentor = list(mentee_mentor)

    if mentee_mentor    :
        
        mentor_data = MentorSignup.query.get(mentee_mentor.mentor_username)

        response1 = {"name" : mentor_data.name, "phonenumber" : mentor_data.phonenumber, "state" : mentor_data.state, "interest1" : mentor_data.interest1, "interest2" : mentor_data.interest2,"interest3" : mentor_data.interest3, "gender" : mentor_data.gender, "career" : mentor_data.career, "lanuage" : mentor_data.language}

        return jsonify(response1)

    # if no mentor for mentee, run the ML model done
    # TO BE CODED
    #NEED TO CALL THE ML FUNCTION WITH THE PARAMETERS done
    # WILL BE RETURNED WITH A LIST done
    # NEED TO CHECK THAT LIST FOR THRESHHOLD OF MENTOR WITH THE MENTORMENTEE TABLE 
    #FIND THE RESPECTIVE MENTOR IN THE MENTORSIGNUP TABLE
    #RETURN THEIR DATA
    list_of_mentors = machine_learning(mentee_info.username, mentee_info.state, mentee_info.interest1, mentee_info.interest2, mentee_info.interest3, mentee_info.gender_preference, mentee_info.career, mentee_info.language)

    for i in range(len(list_of_mentors)):

        mentor_user = str(list_of_mentors[i])
        # print(mentor_user)

        mentor_instance = MentorMentee.query.filter(MentorMentee.mentor_username.like(mentor_user)).all()
        mentor_instance_count = len(list(mentor_instance))
        mentor_info = MentorSignup.query.get(mentor_user)

        if(mentor_instance_count>mentor_info.no_of_students):
            continue

        mentor_mentee_connect = MentorMentee(mentor_user, username)
        db.session.add(mentor_mentee_connect)
        db.session.commit()

        response1 = {"name" :mentor_info.name, "phonenumber" :mentor_info.phonenumber, "state" :mentor_info.state, "interest1" :mentor_info.interest1, "interest2" :mentor_info.interest2,"interest3" :mentor_info.interest3, "gender" :mentor_info.gender, "career" :mentor_info.career, "lanuage" :mentor_info.language}

        return jsonify(response1)



    return jsonify({"code": 404})






    

        



    


        

