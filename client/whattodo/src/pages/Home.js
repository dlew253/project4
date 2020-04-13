import React from "react";
import { Redirect } from "react-router-dom";
//import { makeStyles } from "@material-ui/core/styles";


//const useStyles = makeStyles(theme => ({
//  root: {
//    flexGrow: 1
//  }, 
//  header: {
//    color: theme.palette.primary.main,
//    fontWeight: "bold",
//    marginTop: "1em",
//    marginLeft: "1em"
//  }
//}));

function Home(props) {

    if (!props.user) {
      return <Redirect to='/' />
    }
    
    return (
      <div>
        <h1>Welcome to remindME!</h1>
        <h3> Click new and get started making a list.</h3>
      </div>
    );
  }
  
  export default Home;