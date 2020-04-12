import React from "react";
import { Redirect } from "react-router-dom";


function Lists(props) {

  if (props.user) {
    return <Redirect to="/home" />
  }
  
  return (
    <div>
      <h2> yeah</h2>
    </div>
  );
}

export default Lists;