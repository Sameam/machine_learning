import React from 'react'
import {Link} from "react-router-dom"

const Card = ({data}) => {
  return (
    <div className="row">
      {data.map((item) => {
        return (
          <div class="col-md-4 mb-4 lead d-flex align-items-stretch" style={{marginLeft:"auto",marginRight:"auto", marginTop:"10px"}}>
          <div class="card mb-3">
            <img className="card-img-top"
            src={item.image} alt="Card cap" />
            <div className="card-body card">
              <h4 className="card-title">Title: {item.title}</h4>
              <p class="card-text">Description: {item.description}</p>
              {item.url && <p className="card-text">Source Code: {item.url}</p>}
            </div>
            <button className='btn btn-success btn-block'><Link to="/bean" style={{color:"black"}}>Start Prediction</Link></button>
          </div> 
        </div>
        )
      })}
    </div>   
  )
}
export default Card