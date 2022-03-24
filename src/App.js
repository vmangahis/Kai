import AnimeCard from "./components/AnimeCard";



function App() {
  return (
    <>
    <div className="app">

        <div className="sidebar">
          
        <div className="logo">
        <h1>Kai</h1>
        </div>
      
        <div className="user">
        <img src="https://www.w3schools.com/w3images/avatar6.png" alt="User Name" className="user-image" />
       
        <p>User Name</p>
        </div>

        <div className="side-nav">
          <ul>
            <li><button className="link-button">Recommended</button></li>  {/* According to current watchlist */}
            <li><button className="link-button">Popular Now</button></li>
            <li><button className="link-button">New Releases</button></li> 
            <li><button className="link-button">Upcoming</button></li>
            <li><button className="link-button">Current Watchlist</button></li>
            
          </ul>
        </div>
        </div>

       

      <AnimeCard />
    </div>
    </>
    
  );
}

export default App;
