import React from "react";
import { Switch, Route } from "react-router-dom";
import Landing from "../pages/Landing";
import Login from "../pages/Login";
import Signup from "../pages/Signup";
import Home from "../pages/Home";
import NotFound from "../pages/NotFound";

function Content(props) {
  return(
    <Switch>
      <Route path="/" exact={true} render={() => <Landing user={props.user ? props.user : null} /> } />
      <Route path="/login" render={() => <Login user={props.user} updateUser={props.updateUser} /> } />
      <Route path="/signup" render={() => <Signup user={props.user} updateUser={props.updateUser} />}  />
      <Route path="/home" render={() => <Home user={props.user ? props.user : null} />} />
      <Route path="*" component={NotFound} />
    </Switch>
  );
}

export default Content;