import React from 'react'

import '../App.css'

function Result(props) {

    return (
        <div className="result">
            <p>
                <span>{props.result.who.data} </span>
                <span>{props.result.what.data} </span>
                <span>{props.result.where.data} </span>
                <span>{props.result.why.data}</span>
            </p>
        </div>
    )
}

export default Result