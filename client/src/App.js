import Sidebar from './components/Sidebar';
import Card from './components/Card';
import Header from './components/Header';

function App() {
  const arr = ['a', 'b', 'c'];
  return (
    <>
    <div className="app">
        
        <Sidebar />
        <div className="main-container">
        <Header />

        <div className="anime-list">
        {arr.map((item, ind) => {
          return <Card />;
        })
        }
        
        </div>
        
        </div>

      
    </div>
    
    </>
  );
}

export default App;
