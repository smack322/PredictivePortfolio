import logo from './logo.svg';
import './App.css';
import {
  BrowserRouter as Router,
  Route,
  Routes
} from 'react-router-dom';
import Navbar from './component/Navbar';
import Microsoft from './component/Microsoft';
import Walmart from './component/Walmart';
import Apple from './component/Apple';
import Home from './component/Home'

function App() {
  return (
    <div className="App">
      
      <Router>
            <Navbar />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/microsoft" element={<Microsoft />} />
                <Route path="/walmart" element={<Walmart />} />
                <Route path="/apple" element={<Apple />} />
            </Routes>
        </Router>
    </div>
  );
}

export default App;
