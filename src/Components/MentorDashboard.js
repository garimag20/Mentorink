import React from 'react';
import { Link } from 'react-router-dom';
import { c,d } from '../UI/Login';
export var e = {}; 

const MentorDashboard = props => {

    const clickHandler = async() => {
        if(c == 200) {
          fetch(`/dashboard/mentor/${d.username}`, {
            method : 'GET',
            headers: {
                'Content-Type': 'application/json',
    
            }
        })
        .then(x => x.json())
          .then(res => {
              e = res;
          })
        }
      }

    return (
        <>
            <div className="d-flex justify-content-center align-items-center" style={{flexDirection: "column",  height: "80vh"}}>
                <h1 className="mb-4">Dashboard</h1>
                <Link to='/dashboard/mentees'><button className= "btn btn-primary" onClick={clickHandler}>View Mentees</button></Link>
            </div>
        </>
    )
}

export default MentorDashboard;
