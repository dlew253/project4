import React from 'react';
import { Container, Grid, Typography, Link } from "@material-ui/core";


function Footer() {
    return (
      <footer className="footer">
        <Container maxWidth="lg">
          <Grid container>
            <Grid item md={6}>
              <Typography 
                variant="subtitle2">
                  Copyright © 2020 Dylan Lewis
              </Typography>
            </Grid>
            <Grid item md={4}>
              <Link href="https://github.com/dlew253/project4" className="footer-link">GitHub</Link>
            </Grid>
          </Grid>
        </Container>
      </footer>
    );
  }
  
  export default Footer;