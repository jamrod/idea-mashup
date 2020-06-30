import React from 'react'

import '../App.css'

function Result(props) {

    return (
        <div className="result">
            {props.result.who.data ?
                <p>
                    <span className="capital">{props.result.who.data} </span>
                    <span className="capital">needs to {props.result.what.data} </span>
                    <span className="capital">at {props.result.where.data} </span>
                    <span className="capital">{props.result.why.data}</span>
                </p>
                : null}
        </div>
    )
}

export default Result