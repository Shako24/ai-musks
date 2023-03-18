import React, { Component } from "react";

class Counter extends Component {
  doHandleIncrement = () => {
    this.handleIncrement({ id: 1 });
  };
  doHandleDecrement = () => {
    this.handleDecrement({ id: 1 });
  };

  button_styles = {
    width: "90px",
    marginRight: "30px",
    color: "#000000",
    background: "white",
    fontSize: "1em",
    fontWeight: "bold",
    outline: "none",
    border: "none",
    borderRadius: "5px",
    transition: ".2s ease-in",
    cursor: "pointer",
  };

  render() {
    //let classes = this.getBadgeClasses();
    return (
      <div>
        <button
          onClick={() => this.props.onIncrement(this.props.counter)}
          style={this.button_styles}
        >
          +
        </button>
        <span
          style={{
            color: "#fff",
            fontSize: "2.3em",
            margin: "60px",
            fontWeight: "bold",
            cursor: "pointer",
            marginLeft: "30px",
          }}
        >
          {this.formatCount()}
        </span>
        <button
          onClick={() => this.props.onDecrement(this.props.counter)}
          style={this.button_styles}
        >
          -
        </button>
        <button
          onClick={() => this.props.onDelete(this.props.counter.id)}
          style={this.button_styles}
        >
          Delete
        </button>
      </div>
    );
  }

  formatCount() {
    const { value: count } = this.props.counter;
    return count;
  }
}

export default Counter;
