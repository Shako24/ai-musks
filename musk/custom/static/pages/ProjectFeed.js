// References


import axios from "axios";
import React from "react";
import "../css/Project_feed.css";
import ProjectMenu from "./ProjectMenu";

const ProjectFeed = () => {
  const backgroundState = true;

  const config = {
    header: {
      'Content-type': 'application/json',
      "Authorization": `Token ${localStorage.getItem('token')}`
    }
  }

  axios
    .get("http://127.0.0.1:8000/projects/", config)
    .then((resp) => {
      console.log(resp.data);
    })
    .catch((err) => {
      console.log(err.response.data);
      console.log(config)
    });

  return (
    <div className="Background-projectfeed">
      <div>
        <ProjectMenu state={backgroundState} />
      </div>
      <div
        className="Project-Container"
        style={{
          marginLeft: backgroundState ? "20%" : "3%",
        }}
      >
        <div className="box"></div>
      </div>
    </div>
  );
};

export default ProjectFeed;
