document.addEventListener("DOMContentLoaded", (event) => {

    let window_location = window.location.pathname.split('/')[1];
    let controller_button = document.querySelectorAll('.list-controller');
    

    let active_menu;
    let active_controller;

    

    
    

    controller_button.forEach((element,index) =>{
        
        element.addEventListener('click' , e =>{
            
            if(active_menu && active_controller)
            {
                if(active_controller != e.target && active_menu != document.querySelectorAll('.edit-watchlist-controller')[index])
                {
                    active_menu.style.display="none";
                    active_controller.className = "bi bi-three-dots-vertical list-controller";
                }
                
            }


            if(e.target.className == "bi bi-three-dots-vertical list-controller")
            {   
                e.target.className = "bi bi-x-lg list-controller-close";
                document.querySelectorAll('.edit-watchlist-controller')[index].style.display = "flex";
            }
            else{
                e.target.className= "bi bi-three-dots-vertical list-controller";
                document.querySelectorAll('.edit-watchlist-controller')[index].style.display = "none";
            }

            
            active_controller =  e.target;
            active_menu = document.querySelectorAll('.edit-watchlist-controller')[index];
                


            
        })
    })

    




    

    if (window_location == 'readlist') {
        document.getElementById('readlist-button').classList.add('mode-choice');
        document.getElementById('watchlist-button').classList.remove('mode-choice');
    } else if (window_location == 'watchlist') {
        document.getElementById('watchlist-button').classList.add('mode-choice');
        document.getElementById('readlist-button').classList.remove('mode-choice');
    }


    document.querySelectorAll('#watchlist-button, #readlist-button').forEach(ell => {
        ell.addEventListener('click', (e) => {

            let url = "";
            let list_type = "";

            if (e.target.id == 'watchlist-button') {
                document.getElementById('watchlist-button').classList.add('mode-choice');
                document.getElementById('readlist-button').classList.remove('mode-choice');
                url = "/watchlist/" + document.getElementById('user_id').textContent;
                list_type = "watchlist";

            } else if (e.target.id == 'readlist-button') {
                document.getElementById('readlist-button').classList.add('mode-choice');
                document.getElementById('watchlist-button').classList.remove('mode-choice');
                url = "/readlist/" + document.getElementById('user_id').textContent;
                list_type = "readlist";
            }


            fetch(url, {
                    method: "POST",
                    credentials: 'same-origin',
                    body: JSON.stringify({
                        'queryType': list_type
                    })

                })
                .then((res) => res.json())
                .then((data) => {
                    let final = data;

                    let urlState = "";
                    let tag = "";
                    if (final.length > 0) {
                        final.forEach(elem => {

                            if (list_type == "watchlist") {
                                tag += `<div class = "list-card text-light"><a href="http://${window.location.host}/anime/${elem.id}"><img src="${elem.thumbnail}" alt="${elem.title}" class="list-card-image thumbnail-image" />
                        </a><div class="title-info-text">
                        <h5 class="text-start">${elem.title}</h5><p class="text-start">${elem.genre.map(genreElement => {
                            
                            return  genreElement;
                        }).join(', ')} </p></div></div>`;
                            } else if (list_type == "readlist") {
                                tag += `<div class = "list-card text-light"><a href="http://${window.location.host}/manga/${elem.id}"><img src="${elem.thumbnail}" alt="${elem.title}" class="list-card-image thumbnail-image" />
                        </a><div class="title-info-text">
                        <h5 class="text-start">${elem.title}</h5><p class="text-start"> ${elem.genre.map((genreElement) => {
                            
                            return genreElement;
                        }).join(', ')}</p></div></div>`;
                            }



                        }); // end final.forEach

                    } // end if(final.length)
                    else if (final.length == 0) {
                        tag = `<div class = "list-card text-light"><h1 class="text-light blank-list">You got nothing to read/watch at the moment.</h1></div>`;
                    }
                    document.getElementById('watchlist-card-container').innerHTML = tag;


                    if (list_type == "watchlist") {

                        urlState = `${window.location.protocol}//${window.location.hostname}:${window.location.port}/watchlist/${document.getElementById('user_id').textContent}`;

                    } else if (list_type == "readlist") {
                        urlState = `${window.location.protocol}//${window.location.hostname}:${window.location.port}/readlist/${document.getElementById('user_id').textContent}`;
                    }


                    window.history.replaceState(null, null, urlState);

                })
                .catch((error) => {
                    console.error(error);
                })
        })
    });




});