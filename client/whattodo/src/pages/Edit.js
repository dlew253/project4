import React from "react";
import { Redirect } from "react-router-dom";
import Edit from "../Components/Edit";

function Edit(props) {

  if (props.user) {
    return <Redirect to="/home" />
  }
  
  return (
    <div>
      
    </div>
  );
}

export default Edit;