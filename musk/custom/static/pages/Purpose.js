import React, { useState } from "react";
import ProjectMenu from "./ProjectMenu";
import { useNavigate } from "react-router-dom";
import "../css/Purpose.css";
import axios from "axios";

const Purpose = () => {
  const current = new Date();
  const currentDate = `${current.getFullYear()}-${
    current.getMonth() + 1
  }-${current.getDate()}`;

  const navigate = useNavigate(); // to navigate to other pages

  const [pageCheck, setpageCheck] = useState({
    pages: [
      { value: false },
      { value: false },
      { value: false },
      { value: false },
    ],
  });
  const [isActive, setisActive] = useState(false);
  const [message, setMessage] = useState("");

  // to login to the website home page
  const nextClicked = (e) => {
    e.preventDefault();

    const purpose = {
      creator: localStorage.getItem("user"),
      projectName: document.getElementById("webName").value,
      purpose: document.getElementById("framework").value,
      date: currentDate,
      homePage: pageCheck.pages[0].value,
      aboutPage: pageCheck.pages[1].value,
      contactPage: pageCheck.pages[2].value,
      customPage: pageCheck.pages[3].value,
      customPageName: document.getElementById("customName").value,
    };


    // const newpurs = { "creator": "shazil23", "name": "NEW WEBS", "purpose": "Blog", "date": "2022-11-7", "homePage": false, "aboutPage": true, "contactPage": true, "customPage": false, "customPageName": "" }

    axios
      .post("http://127.0.0.1:8000/purpose/", purpose, {
        headers: {
          "Authorization": `Token ${localStorage.getItem("token")}`,
        }
      })
      .then((resp) => {
        console.log(resp.data);
        navigate('/create-website/options')
      })
      .catch((err) => {
        console.log(err.response.data);
      });

      
    
    console.log(purpose);
  };

  // Custom checkbox: shows and hide custom page name text area
  const customLabel = (index) => {
    setisActive((current) => !current);
    checkChange(index);
    setMessage("");
  };
  const custominputChange = (e) => {
    setMessage(e.target.value);
  };

  // select purpose name
  const handleChange = (e) => {
    console.log("Purpose Selected");
    // purpose.purpose = e.target.value;
  };

  // function for check box value
  const checkChange = (index) => {
    const pages = pageCheck.pages;
    pages[index].value = !pages[index].value;
    setpageCheck({ pages });
  };

  // box_style for for input and select fields
  const box_styles = {
    width: "auto",
    height: "auto",
    background: "#e0dede",
    padding: "10px",
    border: "none",
    outline: "none",
    borderRadius: "5px",
  };

  return (
    <div>
      <ProjectMenu />
      <div className="Background_purpose">
        <h1
          style={{
            display: "flex",
            justifyContent: "center",
            marginRight: "90px",
          }}
        >
          This is a Purpose Page
        </h1>
        <div>
          <form 
            style={{
              marginLeft: "20%",
              width: "50%",
              height: "auto",
              padding: "20px",
              background:
                "linear-gradient(to bottom, #0f0c29, #302b63, #24243e)",
            }}
          >
            <div className="purpose_field_row">
              <label className="purpose_header">Name of the website</label>
              <input
                id="webName"
                type="name"
                name="website name"
                placeholder="Website Name"
                required=""
                style={box_styles}
              />
            </div>
            <div className="purpose_field_row">
              <label className="purpose_header">
                What is the purpose of the website:{" "}
              </label>
              <select
                id="framework"
                style={box_styles}
                onChange={(e) => handleChange(e)}
              >
                <option
                  value="Corporate"
                  style={box_styles}
                  label="Corporate"
                />
                <option
                  value="E-Commerce"
                  style={box_styles}
                  label="E-Commerce"
                />
                <option value="Blog" style={box_styles} label="Blog" />
                <option
                  value="Portfolio"
                  style={box_styles}
                  label="Portfolio"
                />
                <option value="Wiki" style={box_styles} label="Wiki" />
              </select>
            </div>
            <div className="purpose_field_column">
              <label className="purpose_header">
                How many pages do you want
              </label>
              <div
                style={{
                  display: "flex",
                  flexDirection: "row",
                }}
              >
                <input
                  type="checkbox"
                  id="Home"
                  name="Home"
                  onChange={() => checkChange(0)}
                />
                <label className="page_option">Home</label>
                <input
                  type="checkbox"
                  id="About"
                  name="About"
                  onChange={() => checkChange(1)}
                />
                <label className="page_option" htmlFor="About">
                  About
                </label>
                <input
                  type="checkbox"
                  id="Contact"
                  name="Contact"
                  onChange={() => checkChange(2)}
                />
                <label className="page_option" htmlFor="Contact">
                  Contact
                </label>
                <input
                  type="checkbox"
                  id="Custom"
                  name="Custom"
                  onChange={() => customLabel(3)}
                />
                <label className="page_option" htmlFor="Custom">
                  Custom
                </label>
              </div>
              <div
                id="customPageDiv"
                style={{
                  display: isActive ? "block" : "none",
                  paddingTop: "10px",
                }}
              >
                <input
                  id="customName"
                  name="customPageName"
                  type="text"
                  placeholder="Title of the Custom page"
                  value={message}
                  onChange={custominputChange}
                  style={box_styles}
                />
              </div>
            </div>
            <div
              style={{
                display: "flex",
                justifyContent: "center",
                marginRight: "60px",
                marginTop: "80px",
              }}
            >
              <button
                onClick={nextClicked}
                name="nextClicked"
                style={{
                  width: "50%",
                  height: "40px",
                  margin: "10px auto",
                  display: "block",
                  color: "#fff",
                  background: "#573b8a",
                  fontSize: "1em",
                  fontWeight: "bold",
                  marginTop: "20px",
                  outline: "none",
                  border: "none",
                  borderRadius: "5px",
                  transition: ".2s ease-in",
                  cursor: "pointer",
                }}
              >
                Next
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Purpose;
