// References
// https://www.folkstalk.com/2022/09/how-to-import-images-from-public-folder-in-react-js-with-code-examples-2.html

import React from "react";
import "../css/Home.css";
import ProjectMenu from "./ProjectMenu";

const ProjectFeed = () => {
  function importAll(r) {
    let images = {};
    r.keys().forEach((item, index) => {
      images[item.replace("./", "")] = r(item);
    });
    return images;
  }


  const images = importAll(require.context("../images", false, /\.(png)$/));


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
        <img className="img_row1" src={images["v27_90.png"]} alt="Project 1" />
        <img className="img_row1" src={images["v27_91.png"]} alt="Project 2" />
        <img
          className="img_row1"
          style={{
            height: "160px",
          }}
          src={images["v27_92.png"]}
          alt="Project 3"
        />
        <img
          className="img_row1"
          style={{
            height: "160px",
          }}
          src={images["v27_93.png"]}
          alt="Project 4"
        />
        <div className="project-text-div">
          <label>Project 1</label>
          <label style={projectText}>Project 2</label>
          <label style={projectText}>Project 3</label>
          <label style={projectText}>Project 4</label>
        </div>
        <img className="img_row2" src={images["v27_125.png"]} alt="Project 5" />
        <img className="img_row2" src={images["v27_126.png"]} alt="Project 6" />
        <img className="img_row2" src={images["v27_127.png"]} alt="Project 7" />
        <img className="img_row2" src={images["v27_128.png"]} alt="Project 8" />
        <div className="project-text-div">
          <label>Project 5</label>
          <label style={projectText}>Project 6</label>
          <label style={projectText}>Project 7</label>
          <label style={projectText}>Project 8</label>
        </div>
      </div>
    </div>
  );
};

export default ProjectFeed;
