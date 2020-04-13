import React from "react";
import { Redirect } from "react-router-dom";
import EditProfile from "../components/EditProfile";

function Edit(props) {

  if (props.user) {
    return <Redirect to="/home" />
  }
  
  return (
    <div className="edit">
      <EditProfile />
    </div>
  );
}

export default Edit;