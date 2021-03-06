import React from "react";
import { Redirect } from "react-router-dom";
import Notepad from "../components/Notepad"

function New(props) {

  if (props.user) {
    return <Redirect to="/home" />
  }
  
  return (
    <div className='notepad'>
      <Notepad/>
    </div>
  );
}

export default New;