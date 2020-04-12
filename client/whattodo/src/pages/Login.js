import React from "react";
import { Redirect } from "react-router-dom";
import Login from "../components/Login";
//import Footer from "../components/Footer"
function UserLogin(props) {

  if (props.user) {
    return <Redirect to="/home" />
  }
  
  return (
    <div>
      <UserLogin user={props.user} updateUser={props.updateUser}/>
      
    </div>
   
  );
}

export default Login;