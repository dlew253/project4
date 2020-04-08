import React from "react";
import { Redirect } from "react-router-dom";
import Login from "../Components/Login";

function Login(props) {

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