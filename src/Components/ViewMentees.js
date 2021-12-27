import React from 'react';
import { Link } from 'react-router-dom';
import {e} from './MentorDashboard';


const ViewMentees = (props) => {

    // const mentees = [
    //     {name: "Peter Parker", phoneNumber: 9763726263, interest1: 'Dancing', interest2: 'Singing', interest3: 'Sports', state: 'Maharshtra', language: 'English', career: 'Engineering'},
    //     {name: "Tony Stark",  phoneNumber: 9763726263, interest1: 'Dancing', interest2: 'Singing', interest3: 'Sports', state: 'Maharshtra', language: 'English', career: 'Engineering'},
    //     {name: "Tony Stark",  phoneNumber: 9763726263, interest1: 'Dancing', interest2: 'Singing', interest3: 'Sports', state: 'Maharshtra', language: 'English', career: 'Engineering'}
    // ]

    return (
        <div>
            <h1 className="pt-5"><center>My Mentee</center></h1>
            <div className="d-flex justify-content-center align-items-center" style={{height: "60vh"}}>
                <div className="card shadow text-dark mx-4" style={{width: "17rem", margin: "10px", borderRadius: "20px", backgroundColor: "white"}}>
                    <center>
                        <div className="card-body float-bottom my-5">
                            <h2 className="card-title mb-4" style={{fontSize: "22px", textTransform: "capitalize"}}>{e.name}</h2>
                            <div>
                                <Link className="btn btn-primary" style={{borderRadius: "12px", fontSize: "15px", color: "white"}} to='/dashboard/mentee-details'>View Details</Link>
                            </div>
                        </div>
                    </center>
                </div>
            </div>
        </div>
    )
}

export default ViewMentees;
