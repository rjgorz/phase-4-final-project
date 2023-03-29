import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import Nav from "../pages/Nav";
import Login from "../pages/Login";
import SongForm from "../components/SongForm"
import Home from "../pages/Home"
import Profile from "../pages/Profile"

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // auto-login
    fetch("/check_session").then((response) => {
      if (response.ok) {
        response.json().then((user) => setUser(user));
      }
    });
  }, []);

  // if (!user) return <Login onLogin={setUser} />;e
  if (!user) return <SongForm user={user} />;

  return (
    <>
      <Nav user={user} setUser={setUser} />
      <main>
        <Switch>
          
          <Route path="/profile">
            <Profile user={user}></Profile>
          </Route>
          <Route path="/home">
            <Home user={user}></Home>
          </Route>
          <Route path="/newsong">
            <SongForm></SongForm>
          </Route>
          <Route path="/">
            <h1>Test</h1>
          </Route>
        </Switch>
      </main>
    </>
  );
}

export default App;
