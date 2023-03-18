//   REFERENCES
//  https:codepen.io/mamislimen/pen/jOwwLvy

import React, { useState } from "react";
import pic from "../images/v18_24.png";
import "../css/Signup.css";
import { API_LOGIN_URL, API_SIGNUP_URL } from "../constants/";
import axios from "axios";

const Signup = ({ setToken, setUser }) => {
  /*
  function handleCallBackResponse(response) {
      console.log("Encoded JWT ID token: " + response.credential);
  }
  
  useEffect(() => {
      /* global google 
      google.accounts.id.initialize({
          client_id: "461377866911-16jb3ctu6sfclr7omn9pi056ruek57ot.apps.googleusercontent.com",
          callback: handleCallBackResponse
  });

      google.accounts.id.renderButton(
          document.getElementById("signInDiv"),
          { theme: "outline", size: "large" }
      );
  }, []);
  */
  const [wrong, setWrong] = useState(false);
  // const navigate = useNavigate();

  // useEffect(() => {
  //   axios
  //     .get(API_URL, {
  //       headers: {
  //         "Content-Type": "application/json",
  //       },
  //     })
  //     .then((resp) => {
  //       setState(resp.data);
  //     })
  //     .catch((error) => {
  //       setError(error);
  //     });
  // }, []);

  // to navigate to other pages

  const signupClicked = (e) => {
    e.preventDefault();

    // axios
    //   .post("http://127.0.0.1:8000/api/userProfiles/", {
    //     username: "usman",
    //     password: "usman123",
    //     email: "usman@gmail.com",
    //   })
    //   .then((resp) => {
    //     console.log(resp.data);
    //   })
    //   .catch((error) => {
    //     setError(error);
    //   });


    const signupdata = {
      username: document.getElementById("newuser").value,
      email: document.getElementById("newemail").value,
      password1: document.getElementById("newpassword").value,
      password2: document.getElementById("reppassword").value,
    };

    console.log(signupdata);

    axios
      .post(API_SIGNUP_URL, signupdata)
      .then((resp) => {
        console.log("the key generated for new user is ", resp.data);
      })
      .catch((err) => {
        console.log(err.response.data);
      });
  };

  // to login to the website home page
  const loginClicked = (e) => {
    e.preventDefault();
    // axios
    //   .get("http://127.0.0.1:8000/api/userProfiles/", {
    //     headers: {
    //       "Content-Type": "application/json",
    //     },
    //   })
    //   .then((resp) => {
    //     setState(resp.data);
    //     console.log(resp.data);
    //   })
    //   .catch((error) => {
    //     setError(error);
    //   });

    // const email = document.getElementById("loginEmail");
    // const pass = document.getElementById("loginPass");
    // for (let index = 0; index < state.length; index++) {
    //   if (
    //     state[index].email === email.value &&
    //     state[index].password === pass.value
    //   ) {
    //     console.log("login success");
    //     navigate("/home");
    //     break;
    //   } else {
    //     console.log("login failed");
    //   }
    // }

    const username = document.getElementById("loginUsername");
    const pass = document.getElementById("loginPass");

    const logindata = {
      username: username.value,
      password: pass.value,
    };

    axios
      .post(API_LOGIN_URL, logindata)
      .then((resp) => {
        const authUser = localStorage.setItem("user", logindata.username);
        setUser(authUser);
        const authToken = localStorage.setItem("token", resp.data.key);
        setToken(authToken);
        console.log(resp.data.key);
        setWrong(false)
        // navigate("/home");
      })
      .catch((err) => {
        console.log(err.response.data);
        setWrong(true)
      });
  };

  return (
    <div className="Background">
      <div>
        <img src={pic} alt="right background" id="image1" />
      </div>

      <div className="Login_Box">
        <input type="checkbox" id="chk" aria-hidden="true" />

        <div className="login">
          <form>
            <label htmlFor="chk" aria-hidden="true" className="label_account">
              Login
            </label>
            <input
              id="loginUsername"
              type="name"
              name="username"
              placeholder="User name"
              required=""
              className="input_account"
            />
            <label
              htmlFor="chk"
              style={{
                display: wrong ? "flex" : "none",
                justifyContent: "center",
                color: 'red'
              }}
            >
              Wrong email entered
            </label>
            <input
              id="loginPass"
              type="password"
              name="pswd"
              placeholder="Password"
              required=""
              className="input_account"
            />
            <label
              htmlFor="chk"
              style={{
                display: wrong ? "flex" : "none",
                justifyContent: "center",
                color: 'red'
              }}
            >
              Wrong password entered
            </label>
            <button onClick={loginClicked} className="button_account">
              Login
            </button>
          </form>
        </div>

        <div className="signup">
          <form>
            <label htmlFor="chk" aria-hidden="true" className="label_account">
              Sign up
            </label>
            <input
              id="newuser"
              type="Text"
              name="txt"
              placeholder="User name"
              required=""
              className="input_account"
            />
            <input
              id="newemail"
              type="email"
              name="email"
              placeholder="Email"
              required=""
              className="input_account"
            />
            <input
              id="newpassword"
              type="password"
              name="pswd"
              placeholder="Password"
              required=""
              className="input_account"
            />
            <input
              id="reppassword"
              type="password"
              name="pswd"
              placeholder="Password (again)*"
              required=""
              className="input_account"
            />
            <button className="button_account" onClick={signupClicked}>
              Sign up
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Signup;
