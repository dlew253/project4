import React from "react";
import { Redirect } from "react-router-dom";


function New(props) {

  if (props.user) {
    return <Redirect to="/home" />
  }
  
  return (
    <div>
      <Notepad/>
    </div>
  );
}

export default New;