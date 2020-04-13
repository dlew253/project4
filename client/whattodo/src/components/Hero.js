import React from 'react';
import { Link } from "react-router-dom";
import { Button } from "@material-ui/core";

function Hero() {
    return (
        <div className="info">        
          <br></br>
          <br></br>
          <h1>
            Keep track of your life
          </h1>
          <br></br>
          <br></br>
          <br></br>
          <Button
            className="btn"
            variant="contained"
            color="secondary"
            size="large"
            component={Link}
            to="/signup"
            >
              Try It Today!
          </Button>
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
  
  export default Hero;