import './App.scss';
import {BrowserRouter, Switch, Route} from "react-router-dom"
import Home from './Components/Home';
import Prediction from './Components/Prediction';

function App() {
  return (
   <BrowserRouter>
    <Switch>
      <Route path="/" exact component={Home}/>
      <Route path="/bean" exact component={Prediction} />
    </Switch>
   </BrowserRouter>
  );
}

export default App;
