/* REFERENCES
 * https://www.youtube.com/watch?v=roxC8SMs7HU&ab_channel=CooperCodes
 */

import React, { useEffect, useState } from "react";
import Signup from "./pages/Signup";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import Home from './pages/Home'
import ProjectFeed from "./pages/ProjectFeed";
import CreateWebsite from "./pages/CreateWebsite";
import TextInput from "./pages/TextInput";
import ImageInput from "./pages/ImageInput";
import Download from "./pages/Download";
import Demo from "./pages/Demo";
import Purpose from "./pages/Purpose";

const App = () => {
  const [token, setToken] = useState(null);
  const [user, setUser] = useState("");

  const checkToken = () => {
    setToken(localStorage.getItem("token"));
  };

  const checkUser = () => {
    setUser(localStorage.getItem("user"));
  };

  useEffect(() => {
    checkToken();
    checkUser();
    console.log("component refreshed after token add/delete");
  }, [token, user]);

  return (
    <>
      <Router>
        <Routes>
          <Route exact path="/home" element={<Home />} />
          <Route path="/create-website" element={<Purpose />} />
          <Route path="create-website/options" element={<CreateWebsite />} />
          <Route path="/create-website/text-input/" element={<TextInput />} />
          <Route
            path="/create-website/text-input/:id"
            element={<TextInput />}
          />
          <Route path="/create-website/image-input" element={<ImageInput />} />
          <Route path="/projects" element={<ProjectFeed />} />
          <Route
            path="/account"
            element={
              token ? (
                <Navigate replace to="/home" />
              ) : (
                <Signup setToken={setToken} setUser={setUser} />
              )
            }
          />
          <Route path="/download-website" element={<Download />} />
          <Route path="/demo" element={<Demo />} />
          <Route path="purpose" element={<Purpose />} />
          <Route exact path="/" element={<Navigate to="/account" />} />
        </Routes>
      </Router>
    </>
  );
};

export default App;
