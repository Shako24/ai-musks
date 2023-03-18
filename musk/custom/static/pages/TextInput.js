import React from "react";
import { useState } from "react";
import Counter from "../components/counter";
import ProjectMenu from "./ProjectMenu";
import "../css/TextInput.css";

const TextInput = () => {
  const [state, setState] = useState({
    counters: [
      { id: 0, value: 0, name: "Heading" },
      { id: 1, value: 0, name: "Checkbox" },
      { id: 2, value: 0, name: "Navigation Bar" },
      { id: 3, value: 0, name: "Dropdown" },
      { id: 4, value: 0, name: "Textbox" },
      { id: 5, value: 0, name: "Footer" },
      { id: 6, value: 0, name: "Paragrapgh" },
      { id: 7, value: 0, name: "Label" },
      { id: 8, value: 0, name: "Image" },
      { id: 9, value: 0, name: "Text Area" },
      { id: 10, value: 0, name: "Button" },
      { id: 11, value: 0, name: "Link" },
    ],
  });

  const [viewCounter, setviewCounter] = useState({
    viewStatus: [
      { id: 0, value: false },
      { id: 1, value: false },
      { id: 2, value: false },
      { id: 3, value: false },
      { id: 4, value: false },
      { id: 5, value: false },
      { id: 6, value: false },
      { id: 7, value: false },
      { id: 8, value: false },
      { id: 9, value: false },
      { id: 10, value: false },
      { id: 11, value: false },
      // { id: 12, value: false },
    ],
  });

  const handleIncrement = (counter) => {
    console.log(counter);
    const counters = [...state.counters];
    const index = counters.indexOf(counter);
    counters[index] = { ...counter };
    counters[index].value++;
    console.log(state.counters[0]);
    setState({ counters });
  };

  const handleDecrement = (counter) => {
    console.log(counter);
    const counters = [...state.counters];
    const index = counters.indexOf(counter);
    counters[index] = { ...counter };
    counters[index].value--;
    console.log(state.counters[0]);
    setState({ counters });
  };

  //const [items, setItems] = useState([...handleReset.map((x, id) => ({ id, ...x }))]);

  const handleReset = () => {
    var check = document.getElementsByClassName("checkBox");
    const counters = state.counters.map((c) => {
      c.value = 0;
      return c;
    });
    setState({ counters });

    const viewStatus = viewCounter.viewStatus.map((i) => {
      i.value = false;
      return i;
    });

    for (let index = 0; index < check.length; index++) {
      check[index].checked = false;
    }

    setviewCounter(viewCounter);
    console.log(viewCounter);
  };

  const handleDelete = (counterId) => {
    const counters = state.counters.filter((c) => c.id !== counterId);
    setState({ counters });
  };

  const handleChange = (id) => {
    const viewStatus = viewCounter.viewStatus;
    viewStatus[id].value = !viewStatus[id].value;

    setviewCounter({ viewStatus });
    console.log(viewCounter.viewStatus[id].value);
  };

  return (
    <div
      style={{
        display: "absolute",
        background: "grey",
        height: "1100px",
      }}
    >
      <ProjectMenu />
      <div
        style={{
          height: "auto",
          marginLeft: "16%",
          display: "flex",
          flexDirection: "column",
        }}
      >
        <button onClick={handleReset} className="reset_button">
          Reset
        </button>
        {state.counters.map((counter) => (
          <div
            style={{
              display: "flex",
              flexDirection: "row",
              columnGap: "200px",
              marginLeft: "40px",
            }}
          >
            <div class="choice">
              <label>
                <input
                  className="checkBox"
                  type="checkbox"
                  value="1"
                  onChange={() => handleChange(counter.id)}
                />
                <span>{counter.name}</span>
              </label>
            </div>
            <div
              style={{
                display: viewCounter.viewStatus[counter.id].value
                  ? "block"
                  : "none",
                transition: "0.5s ease-in-out",
                marginTop: "15px",
              }}
            >
              <Counter
                key={counter.id}
                onDelete={handleDelete}
                onIncrement={handleIncrement}
                onDecrement={handleDecrement}
                counter={counter}
              />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default TextInput;
