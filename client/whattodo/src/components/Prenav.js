import React from 'react';
import { Link } from "react-router-dom";
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Button from '@material-ui/core/Button';
import Logo from "./Logo";
//gotta ask chris for a logo
function PreNav() {
  
  return (
    <div>
      <AppBar position="static">
        <Toolbar>
          <Logo link='/'/>
          <Button 
            color="inherit"
            component={Link}
            to="/login">Login</Button>
          <Button 
            color="inherit"
            component={Link}
            to="/signup">Sign Up</Button>
          
        </Toolbar>
      </AppBar>
    </div>
  );
}

export default PreNav;

  // https://material-ui.com/components/app-bar/
  // https://material-ui.com/getting-started/templates/