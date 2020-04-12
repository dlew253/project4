import React from "react";
import { Redirect } from "react-router-dom";
import Signup from "../components/Signup";

function UserSignup(props) {

  if (props.user) {
    return <Redirect to="/home" />
  }
  
  return (
    <div>
        <UserSignup user={props.user} updateUser={props.updateUser}/>
    </div>
  );
}

export default Signup;