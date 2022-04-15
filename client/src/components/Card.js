import ButtonComponent from "./ButtonComponent";

function Card(props){

    return (
    <div className="card">
        <img src="./resources/placeholder-anime.png" className="image-card"  alt="" />
        <h2>{props.title}</h2>
        <p>Description</p>
        <ButtonComponent label="Add to Watchlist" class="add-watchlist"/>
    </div>
    );
    
}

export default Card;