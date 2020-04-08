import React from "react";
import { Link, Redirect } from "react-router-dom";
import { AppBar, Toolbar, Button } from "@material-ui/core";
import Searchbar from "./Searchbar";
import Logo from "./Logo";


// come back to the design later
//material has some possibly better templates to use to diversify.
function Postnav(props) {
  const handleLogout = e => {
    e.preventDefault() 
    //this is gonna change with auth implementation
    localStorage.removeItem('mernToken')
    props.updateUser();
  }

    return (
      <AppBar position="static">
        <Toolbar>
          <Logo link="/" />
          <Searchbar />
          <Button
            color="inherit"
            component={Link}
            to="/profile">User</Button>
          <Button
            color="inherit"
            component={Link}
            to="/" onClick={handleLogout}>Logout</Button>
        </Toolbar>
      </AppBar>
    );
  }
  
  export default Postnav;

