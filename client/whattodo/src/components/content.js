import React from "react";
import { Switch, Route } from "react-router-dom";
import Landing from "../pages/Landing";
import Login from "../pages/Login";
import Signup from "../pages/Signup";
import Home from "../pages/Home";
import NotFound from "../pages/NotFound";
import Posts from "../pages/Posts";
import Edit from "../pages/Edit";
import New from "../pages/New";

function Content(props) {
  return(
    <Switch>
      <Route path="/" exact={true} render={() => <Landing user={props.user ? props.user : null} /> } />
      <Route path="/login" render={() => <Login user={props.user} updateUser={props.updateUser} /> } />
      <Route path="/signup" render={() => <Signup user={props.user} updateUser={props.updateUser} />}  />
      <Route path="/home" render={() => <Home user={props.user ? props.user : null} />} />
      <Route path="/posts" render={() => <Posts user={props.user ? props.user : null} />} />
      <Route path="/new" render={() => <New user={props.user ? props.user : null} />} />
      <Route path="/edit" render={() => <Edit user={props.user ? props.user : null} />} />
      <Route path="*" component={NotFound} />
    </Switch>
  );
}

export default Content;