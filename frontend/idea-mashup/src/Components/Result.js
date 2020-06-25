import React from 'react'

import '../App.css'

function Result(props) {

    return (
        <div className="result">
            <span>{props.result}</span>
        </div>
    )
}

export default Result