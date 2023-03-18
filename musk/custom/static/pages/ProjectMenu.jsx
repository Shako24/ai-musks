import * as React from "react";
import "../css/ProjectMenu.css";
import { Link, Navigate } from "react-router-dom";
import { useState } from "react";
import { Squash as Hamburger } from "hamburger-react";
import axios from "axios";

const ProjectMenu = (state) => {
  const [iconChange, seticonChange] = useState(state);

  function refreshPage() {
    window.location.reload(false);
  }

  const logoutClick = () => {
    localStorage.removeItem("user");
    localStorage.removeItem("token");
    refreshPage();

    axios
      .post("http://127.0.0.1:8000/auth/logout/", {})
      .then((resp) => {
        console.log(resp.data.detail);
      })
      .catch((err) => {
        console.log(err.response.data);
      });
  };

  return (
    <>
      <div className="header">
        <h1
          style={{
            width: "12%",
            color: "rgba(87,211,255,1)",
            position: "absolute",
            top: "10px",
            left: "87px",
            fontFamily: "Oswald",
            fontWeight: "Regular",
            fontSize: "40px",
            opacity: "1",
            textAlign: "center",
          }}
        >
          LOGO
        </h1>
      </div>

      <div
        className="inner-container"
        style={{
          width: iconChange ? "15%" : "0%",
          transition: ".8s ease-in-out",
        }}
      >
        <div
          style={{
            position: "absolute",
            overflow: "visible",
          }}
        >
          <Hamburger
            toggled={iconChange}
            toggle={seticonChange}
            color="#ffffff"
            onToggle={(toggled) => {
              Hamburger.color = "#6d44b8";
            }}
          />
        </div>
        <Link
          to="/"
          className="text-menu"
          style={{
            marginTop: "100px",
          }}
        >
          HOME
        </Link>
        <Link to="/create-website" className="text-menu">
          CREATE WEBSITE
        </Link>
        <Link to="/projects" className="text-menu">
          PROJECTS
        </Link>
        <Link to="/download-website" className="text-menu">
          DOWNLOAD WEBSITE
        </Link>
        <Link to="/demo" className="text-menu">
          DEMO
        </Link>
        <Link
          to="/account"
          type="button"
          className="text-menu"
          onClick={logoutClick}
        >
          LOGOUT
        </Link>
        <label
          className="text-menu"
          style={{
            marginTop: "300px",
          }}
        >
          HELP
        </label>
      </div>
    </>
  );
};

export default ProjectMenu;
