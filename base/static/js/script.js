var watchlistClicked = true;

document.getElementById('togglelist').onclick = () => {
    if(watchlistClicked == true)
    {
        document.querySelector('.watchlist-button').style.backgroundColor = 'black';
        document.querySelector('.readlist-button').style.backgroundColor = 'orange';
        watchlistClicked = false;
    }
}
