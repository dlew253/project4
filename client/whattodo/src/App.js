import React from 'react';
import { useState } from 'react';
import { BrowserRouter as Router} from "react-router-dom";
import { createMuiTheme, ThemeProvider } from "@material-ui/core/styles";
import Prenav from "./components/Prenav";
import Postnav from "./components/Postnav";
import Content from "./components/content";
import Footer from "./components/Footer";
import './App.css';

const theme = createMuiTheme({
  palette: {
    primary: {
      light: "#ffe8e8",
      main: "#ff2929",
      dark: "#b52121"
    },
    secondary: {
      light: "#ffffff",
      main: "#ededed",
      dark: "#9c9c9c"
    }
  }
});
 

function App() {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(null);

  const setUserToken = (responseData) => {
    if (responseData) {
      console.log("🐻")
      setToken(responseData.token)
      setUser(responseData.user)
    } else {
      setToken(null)
      setUser(null)
    }
  }
  const updateUser = newUserDeets => {
    setUser(newUserDeets)
  }

  function setNav() {
    return user ? <Postnav updateUser={updateUser} user={user}/> : <Prenav updateUser={updateUser} user={user}/>;
  }


  return (
    <Router>
      <div className="App">
        <ThemeProvider theme={theme}>
        <div className="navigation">{setNav()}</div>
        <div className="content"><Content updateUser={updateUser} user={user} token={token} setUserToken={setUserToken}/></div>
        <Footer/>
        </ThemeProvider>
      </div>
    </Router>
  );
}

export default App;


