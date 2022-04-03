import {IconContext} from 'react-icons';
import {FaSearch} from 'react-icons/fa';
import SearchBox from './SearchBox';

function Header() {
    return(
        <div className="header">
        <h1 className="page-title">header</h1>

        <div className='search-container'>
        <IconContext.Provider value={{ color: "white", className: "search-button", size: "4em"}}>
            <SearchBox />
            <FaSearch />
        </IconContext.Provider>
        </div>

      </div>
    );
}

export default Header;