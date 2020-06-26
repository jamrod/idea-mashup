import React from 'react'

import '../App.css'

function Request(props) {

    return (
        <div className="request">
            <button onClick={() => props.callRequest()}>Mashup!</button>
        </div>
    )
}

export default Request