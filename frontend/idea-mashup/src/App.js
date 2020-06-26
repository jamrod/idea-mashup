import React, { Component } from 'react';

import Header from './Components/Header'
import Footer from './Components/Footer'
import Request from './Components/Request'
import Result from './Components/Result'

import './App.css';

class App extends Component {
  constructor() {
    super()
    this.state = {
      result: ""
    }
  }

  apiCall(url) {
    fetch(url)
      .then(response => response.json())
      .then(response => {
        // this.handleResults(response)
        console.log(response)
      })
      .catch(err => {
        console.error(err)
      })
  }

  makeRequest = (e) => {
    console.log("clicked")
    this.apiCall("http://127.0.0.1:8000/")
  }

  render() {
    return (
      <div className="App">
        <Header></Header>
        <div>
          <p>
            This is a random story idea generator. Click the button to see an idea in the form of -
            "Who":  Person or persons central to the story.
            "What": What is happening or being attempted.
            "Where": The locale for the story or the "What" action.
            "Why": reason or motivation for the action.
        </p>
        </div>
        <Request callRequest={this.makeRequest}></Request>
        <Result result={this.state.result}></Result>
        <Footer></Footer>
      </div>
    )
  }
}

export default App;
