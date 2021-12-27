import React from 'react';
import { Route, Switch, Redirect, Link } from 'react-router-dom';
import { BrowserRouter as Router} from 'react-router-dom';
import { c,d } from '../UI/Login';
export var e = {}; 

const MenteeDashboard = props => {

  const clickHandler = () => {
    if(c == 200) {
      fetch(`/dashboard/mentee/${d.username}`, {
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
      <div className="d-flex justify-content-center align-items-center" style={{flexDirection: "column",  height: "100vh"}}>
        <h1>Dashboard</h1>
        <br/>
        <Link to="/dashboard/mentees"><button className="btn btn-info" onClick={clickHandler}>View Mentor</button></Link>
      </div>
    )
}

export default MenteeDashboard;
