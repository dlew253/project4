import React from "react";
import { Link } from "react-router-dom";
import { AppBar, Toolbar, Button } from "@material-ui/core";
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
          <Logo link='/'/>
          <Button
            color="inherit"
            component={Link}
            to="/profile">User</Button>
          <Button
            color='inherent'
            component={Link}
            to='/New'>New</Button>
          <Button
            color='inherent'
            component={Link}
            to='/Lists'>My Lists</Button>
          <Button
            color="inherit"
            component={Link}
            to="/" onClick={handleLogout}>Logout</Button>
        </Toolbar>
      </AppBar>
    );
  }
  
  export default Postnav;
