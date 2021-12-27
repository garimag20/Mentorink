import React from 'react';
import {e} from './MentorDashboard';

const MenteeDetails = props => {

    // const mentee = {name: 'Peter Parker', phonenumber: 9763726263, state: 'Maharshtra', language: 'English', career: 'Engineering', interest1: 'Dancing', interest2: 'Singing', interest3: 'Sports'};

    return (
      <div className="d-flex justify-content-center align-items-center" style={{flexDirection: "column",  height: "90vh"}}>
        <h2> <b>Mentee Details</b></h2>
        <br/>
        <div className="card shadow text-dark content-center" style={{margin: "10px", borderRadius: "20px", backgroundColor: "white"}}>
            <div className="card-body float-bottom my-3 mx-5">
                <h3 className="card-title" style={{fontSize: "24px", textTransform: "capitalize"}}>{e.name}</h3>
                <hr className="my-4" />
                <p className="card-title mb-3" style={{fontSize: "18px", textTransform: "capitalize"}}><h4 style={{fontSize: "18px", textTransform: "capitalize", display: 'inline'}}>Contact Number:  </h4>{e.phonenumber}</p>
                <p className="card-title mb-3" style={{fontSize: "18px", textTransform: "capitalize"}}><h4 style={{fontSize: "18px", textTransform: "capitalize", display: 'inline'}}>State:  </h4>{e.state}</p>
                <p className="card-title mb-3" style={{fontSize: "18px", textTransform: "capitalize"}}><h4 style={{fontSize: "18px", textTransform: "capitalize", display: 'inline'}}>Prefered Language:  </h4>{e.language}</p>
                <p className="card-title mb-3" style={{fontSize: "18px", textTransform: "capitalize"}}><h4 style={{fontSize: "18px", textTransform: "capitalize", display: 'inline'}}>Career Choice:  </h4>{e.career}</p>
                <h4 style={{fontSize: "18px", textTransform: "capitalize", display: 'inline'}}>Interests:-  </h4>
                <ul style={{fontSize: "18px", textTransform: "capitalize", display: 'inline'}}>
                    <li className="ms-5">{e.interest1}</li>
                    <li className="ms-5">{e.interest2}</li>
                    <li className="ms-5">{e.interest3}</li>
                </ul>
            </div>
        </div>
      </div>
    )
}

export default MenteeDetails;

