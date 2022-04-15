import Sidebar from './components/Sidebar';
import Card from './components/Card';
import Header from './components/Header';

function App() {
  const arr = ['Anime1', 'Anime2', 'Anime3', 'Anime4', 'Anime5', 'Anime5', 'Anime5', 'Anime5', 'Anime5', 'Anime5'];
  return (
    <>
    <div className="app">
        
        <Sidebar />
        <div className="main-container">
        <Header />

        <div >
          <ul className="anime-list">
        {arr.map((item, ind) => {
          return <li><Card title={item}/></li>;
        })
        }
        </ul>
        </div>
        
        </div>

      
    </div>
    
    </>
  );
}

export default App;
