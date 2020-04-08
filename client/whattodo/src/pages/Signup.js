import React from "react";
import { Redirect } from "react-router-dom";
import Signup from "../Components/Signup";

function Signup(props) {

  if (props.user) {
    return <Redirect to="/home" />
  }
  
  return (
    <div>
        <UserSignUp user={props.user} updateUser={props.updateUser}/>
    </div>
  );
}

export default Signup;