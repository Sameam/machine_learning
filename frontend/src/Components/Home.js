import React from 'react'
import Card from "./Card"
import Base from "./Base"
import Data from "./data"

const Home = () => {
  return (
    <Base>
      <h2 className='text-center' style={{padding:"10px"}}>Welcome to ML prediction for different Models</h2>
      <p>There are two models: 
        <ul>
          <li>Predict the different types of dry beans</li>
          <li>Predict the images</li>
        </ul>
      </p>
      <div className="card-group text-black">
        <Card className="card-top" data={Data}/>
      </div>  
   </Base>

  )
}

export default Home