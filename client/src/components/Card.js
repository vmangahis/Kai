import ButtonComponent from "./ButtonComponent";

function Card(){

    return (
    <div className="card">
        <h2>Title</h2>
        <p>Description</p>
        <ButtonComponent label="Add to Watchlist" class="add-watchlist"/>
    </div>
    );
    
}

export default Card;