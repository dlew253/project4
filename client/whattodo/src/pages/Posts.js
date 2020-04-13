import React from "react";
import { Redirect } from "react-router-dom";


function Posts(props) {

  if (props.user) {
    return <Redirect to="/home" />
  }
  
  return (
    <div>
      <h2> Under Construction</h2>
      <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    </div>


  );
}

export default Posts;