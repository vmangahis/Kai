document.addEventListener("DOMContentLoaded", (event) => {
    let window_location = window.location.pathname.split('/')[1];
    console.log(window_location);
    if(window_location == 'readlist')
    {
        document.getElementById('readlist-button').classList.add('mode-choice');
        document.getElementById('watchlist-button').classList.remove('mode-choice');
    }
    else if(window_location == 'watchlist'){
        document.getElementById('watchlist-button').classList.add('mode-choice');
        document.getElementById('readlist-button').classList.remove('mode-choice');
    }
    document.querySelectorAll('#watchlist-button, #readlist-button').forEach(ell => {
        ell.addEventListener('click', (e) => {
            
            
//            console.log('user is '+ document.getElementById('user_id').textContent);
            let url = "";
            let list_type = "";
            if(e.target.id == 'watchlist-button')
            {
                document.getElementById('watchlist-button').classList.add('mode-choice');
                document.getElementById('readlist-button').classList.remove('mode-choice');
                url = "/watchlist/" + document.getElementById('user_id').textContent;
                list_type = "watchlist";
                
            }
    
            else if(e.target.id == 'readlist-button')
            {   
                document.getElementById('readlist-button').classList.add('mode-choice');
                document.getElementById('watchlist-button').classList.remove('mode-choice');
                url = "/readlist/" + document.getElementById('user_id').textContent;
                list_type = "readlist";
            }
            
            
            fetch(url , 
                {
                    method: "POST",
                    credentials: 'same-origin',
                    body: JSON.stringify({
                        'queryType': list_type
                    })
                    
                })
                .then((res) => Response.json(res))
                .then((data) => {
                    console.log('data is' + JSON.stringify(data));
                })
                .catch((error) => {
                    console.error(error);
                })
        })
    });    

});

