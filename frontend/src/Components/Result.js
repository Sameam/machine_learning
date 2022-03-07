import React from 'react'
import score from "./score"
import {Link} from "react-router-dom"

const Result = (props) => {
  return (
    <div>
      {score.filter(item => item.name === props.score).map(data => (
        <div className="card mx-auto" style={{width: '30rem', margin:"2px"}}>
          <img className="card-img-top" src={data.image} alt="Card cap" />
          <div className="card-body">
            <h5 className="card-title">{data.name}</h5>
            <p className="card-text">Description: {data.description}</p>
            <p className="card-text">Benefits: {data.benefits}</p>
            <p className="card-text">Recipe: {data.Ingredients}</p>
          <div class="col-sm-3">
            <Link to="/" class="btn btn-primary ">Back</Link>
          </div>  
          </div>
        </div>
      ))}
    </div>
  )
}

export default Result