function Sidebar(){
    return(

        <div className="sidebar"> {/* Sidebar start*/}

        <div className="logo">
        <h1>Kai</h1>
        </div>

        <div className="user">
        <img src="https://www.w3schools.com/w3images/avatar6.png" alt="User Name" className="user-image" />
        <p className="username">Hi, User!</p>
        </div>

        <div className="side-nav">
          <ul className="main-nav">
          <li><button className="link-button">Current Watchlist</button></li>
            <li><button className="link-button">Recommended</button></li>  {/* According to current watchlist */}
            <li><button className="link-button">Popular Now</button></li>
            <li><button className="link-button">New Releases</button></li> 
            <li><button className="link-button">Upcoming Anime</button></li>
            </ul>
        
        <div className="line-break">
          <hr />
        </div>

          <ul className="second-nav">
            <li><button className="link-button">Popular Genres</button></li>
            <li><button className="link-button">VA of the Month</button></li>
            <li><button className="link-button">Currently Airing</button></li>
          </ul>
        </div>

        </div> 
    );

}

export default Sidebar;