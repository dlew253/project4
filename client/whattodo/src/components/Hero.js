import React from 'react';
import { Link } from "react-router-dom";
import { Button, Typography } from "@material-ui/core";

function Hero() {
    return (
        <div className="info">
          <Typography
            variant="h1">
    //what eveer i call this
          </Typography>
          <Typography
            variant="h4">
              Keep track of your life
          </Typography>
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
        </div>
    );
  }
  
  export default Hero;