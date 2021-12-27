import React, {useState, useContext} from 'react';
import Login from './UI/Login';
import Signup from './UI/Signup';
import Header from './UI/Header';
import Authcontext from "./Store/Authcontext"; 
import Onload from './Pages/Onload';
import './App.css';
import Footer from './UI/Footer';
import {c, d} from './UI/Login';
import {c1, d1} from './UI/Signup'

if(c1) {
  c = c1;
  d = d1;
  console.log(d);
}

function App() {

  const [ isLoggedIn, setIsLoggedIn ] = useState(false);
  const [ type, setType ] = useState('');


  // useEffect(() => {
  //   console.log("updated..");
    
  // }, [p])


   return (

    <Authcontext.Provider 
      value = {
        {
          isLoggedIn,
          type,
        }
      }
    >
      
      <main className="app">
        { console.log("rendered..", isLoggedIn,type) }
        { !(isLoggedIn)  && <Onload isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn} type={type} setType={setType} />}
        { (type === 'Mentor')   && <Onload isLoggedIn={true} setIsLoggedIn={setIsLoggedIn} type={'Mentor'} setType={setType} />  }
        { (type === 'Mentee')   && <Onload isLoggedIn={true} setIsLoggedIn={setIsLoggedIn} type={'Mentee'} setType={setType} /> }
        { (c === 200) && <Onload isLoggedIn={true} setIsLoggedIn={setIsLoggedIn} type={d.type} setType={setType} />} 
        
      </main>
      {/* <Footer/> */}
    </Authcontext.Provider>
  );
}

export default App;
