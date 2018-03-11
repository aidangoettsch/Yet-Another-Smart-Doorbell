import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import registerServiceWorker from './registerServiceWorker';

import { BrowserRouter, Link, Route } from 'react-router-dom'
import { Button } from 'material-ui'


class App extends Component {
  render() {
    return (
      <div>
        <Link to='/inside'><Button>INSIDE</Button></Link>
        <Link to='/outside'><Button>OUTSIDE</Button></Link>
      </div>
    )
  }
}

ReactDOM.render(
  <BrowserRouter>
    <Route exact path="/*" component={App} />
    {/*<Route path="/inside" component={Inside} />*/}
    {/*<Route path="/outside" component={Outside} />*/}
  </BrowserRouter>
  , document.getElementById('root'));
registerServiceWorker();
