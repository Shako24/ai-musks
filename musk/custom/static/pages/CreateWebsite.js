import React from "react";
import { Link } from "react-router-dom";
import ProjectMenu from "./ProjectMenu";
import pic2 from "../images/sketch_input.png";
import pic1 from "../images/textInput.png";
import "../css/CreateWebsite.css";


const CreateWebsite = () => {
    return(
        <>
        <div>
            <ProjectMenu />
            <div className="Background_createpage">
                <img id="img1"
                    src={pic1}
                    alt="text input"
                />
                <img id="img2"
                    src={pic2}
                    alt="sketch input"
                />
                </div>
                <div>
                    <Link to='/create-website/text-input' className="website_option"><h1>Text Input</h1></Link>
                    <Link to='/create-website/image-input' className="website_option" style={{
                        marginLeft: "70%",
                    }}><h1>Image Input</h1></Link>
                </div>
            
        </div>
        </>
    );
}

export default CreateWebsite;
