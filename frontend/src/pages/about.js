import * as React from "react"
import logo from '../logo.svg'

export default function About() {
  return (
    <div>
      <img src={logo} className="App-logo" alt="logo" />
      <p>
        Guess the word - game
      </p>
      <a
        className="App-link"
        href="/about"
      >
        About
      </a>
    </div>
  );
}
