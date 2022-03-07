import React, {useState, useEffect} from 'react';
import {
  Form, 
  Button, 
  Loading, 
  TextInput
} from "carbon-components-react";
import Result from './Result';

const Prediction = () => {


  const [variable, setVariables] = useState([])
  const [score, setScore] = useState("")
  const [values, setValues] = useState({
    Area: "",
    Perimeter: "",
    MajorAxisLength:"",
    MinorAxisLength: "",
    AspectRation: "",
    Eccentricity: "",
    ConvexArea: "",
    EquivDiameter: "",
    Extent:"",
    Solidity:"",
    roundness:"",
    Compactness:"",
    ShapeFactor1:"",
    ShapeFactor2:"",
    ShapeFactor3:"",
    ShapeFactor4:"",
  });


  const { Area,
      Perimeter,
      MajorAxisLength,
      MinorAxisLength,
      AspectRation,
      Eccentricity,
      ConvexArea,
      EquivDiameter,
      Extent,
      Solidity,
      roundness,
      Compactness,
      ShapeFactor1,
      ShapeFactor2,
      ShapeFactor3,
      ShapeFactor4 } = values;


  const handleChange = (name) =>
    (event) => {
      setValues({ ...values, [name]: event.target.value });
    };

  const handleSubmit = (e) => {
    e.preventDefault();
    const data = {
      Area,
      Perimeter,
      MajorAxisLength,
      MinorAxisLength,
      AspectRation,
      Eccentricity,
      ConvexArea,
      EquivDiameter,
      Extent,
      Solidity,
      roundness,
      Compactness,
      ShapeFactor1,
      ShapeFactor2,
      ShapeFactor3,
      ShapeFactor4
    };
    setScore("Predicting")
    fetch('/prediction', {
      method: 'POST',
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify(data),
    })
    .then(res => res.json())
    .then(res => setScore(res));
  }


  useEffect(()=>{
    fetch('/variable',{
      'methods':'GET',
      headers : {
        'Content-Type':'application/json'
      }
    })
    .then(response => response.json())
    .then(response => setVariables(response))
    .catch(error => console.log(error))
  },[])

  const textInput = (item) => {
    return <TextInput
      id={item.name}
      invalidText="Please enter a numerical value"
      labelText={item.name}
      placeholder={"Enter the value for " + item.name}
      style={{marginBottom:"5px"}}
      onChange={handleChange(item.name)}
      />
  }

  return (
    <div className='mainContainer'>
      {score === "" ? <Form>
        <div className="card" style={{margin:"20px", padding:"20px"}}>
          <h4 className='text-center'>Prediction</h4>
          {variable.length !==0 ? variable.map((item) => {
            return (
              textInput(item))
          }): (<loading description="...Loading"/>)} 
          <Button 
          kind="primary"
          tabIndex={0}
          type="Submit"
          onClick = {handleSubmit}
          >
          Submit
          </Button>
        </div>  
      </Form> : null}
      {score === "Predicting" ? <Loading description='...Loading' /> : <Result score={score} />}
    </div>
  )
}

export default Prediction