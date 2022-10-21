document.addEventListener("DOMContentLoaded", (event) => {

    let window_location = window.location.pathname.split('/')[1];
    let controller_button = document.querySelectorAll('.list-controller');
    

    let active_menu;
    let active_controller;
    
    const reinvokeButtonListeners = (cont) => {
        cont.forEach((element,index) =>{
        
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
        });

        
    }


    reinvokeButtonListeners(controller_button);

    
    

    
    




    

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
                    console.log(final);
                    if (final.length > 0) {
                        final.forEach(elem => {

                            if (list_type == "watchlist") {

                                
                                
                                tag += `<div class = "list-card text-light"><a href="http://${window.location.host}/anime/${elem.id}" class="list-card-image thumbnail-image personal-list ${elem.status == "WATCHING" ? "ongoing" : ""}" style="background-image: url(${elem.thumbnail})">
                        </a>
                        <button id="boot-icon" class="bi bi-three-dots-vertical list-controller" style="font-size: 2rem; color: rgb(255, 0, 0);">
                        </button>
                        <div class="edit-watchlist-controller">
                            <ul class="edit-watchlist-menu">
                                
                                <li>
                                <form method="POST" action="http://${window.location.host}/plan/anime/${elem.id}" >
                                <input type="hidden" name=csrfmiddlewaretoken value=${document.getElementsByName('csrf-token')[0].content} />
                                <button type="submit" class="list-controller-button text-light">Move to plan to watch</button>
                                </form>
                                </li>

                                <li>
                                <form method="POST" action="http://${window.location.host}/finish/anime/${elem.id}">
                                <input type="hidden" name=csrfmiddlewaretoken value=${document.getElementsByName('csrf-token')[0].content} />
                                    <button type="submit" class="list-controller-button text-light">Move to completed list</button>
                                </form>
                                </li>                                



                                <li>
                                
                                <form method="POST" action="http://${window.location.host}/drop/anime/${elem.id}">
                                <input type="hidden" name=csrfmiddlewaretoken value=${document.getElementsByName('csrf-token')[0].content} />
                                    <button type="submit" class="list-controller-button text-light">Move to completed list</button>
                                </form>
                                </li>
                            </ul>
                        </div>
                        <div class="title-info-text">
                        <h5 class="text-start">${elem.title}</h5><p class="text-start"></p></div></div>`;
                            } 
                            
                            else if (list_type == "readlist") {
                                tag += `<div class = "list-card text-light"><a href="http://${window.location.host}/manga/${elem.id}" class="list-card-image thumbnail-image personal-list" style="background-image: url(${elem.thumbnail})">
                        </a>

                        <button id="boot-icon" class="bi bi-three-dots-vertical list-controller" style="font-size: 2rem; color: rgb(255, 0, 0);">
                        </button>
                        <div class="edit-watchlist-controller">

                            <ul class="edit-watchlist-menu">

                                 <li>
                                <form method="POST" action="http://${window.location.host}/plan/manga/${elem.id}" >
                                <input type="hidden" name=csrfmiddlewaretoken value=${document.getElementsByName('csrf-token')[0].content} />
                                <button type="submit" class="list-controller-button text-light">Move to plan to watch</button>
                                </form>
                                </li>

                                <li>
                                <form method="POST" action="http://${window.location.host}/finish/manga/${elem.id}">
                                <input type="hidden" name=csrfmiddlewaretoken value=${document.getElementsByName('csrf-token')[0].content} />
                                    <button type="submit" class="list-controller-button text-light">Move to completed list</button>
                                </form>
                                </li>   

                                <li>
                                <form method="POST" action="http://${window.location.host}/drop/manga/${elem.id}">
                                <input type="hidden" name=csrfmiddlewaretoken value=${document.getElementsByName('csrf-token')[0].content} />
                                    <button type="submit" class="list-controller-button text-light">Remove from my list</button>
                                </form>
                                
                                </li>
                            </ul>

                        </div>
                        
                        
                        <div class="title-info-text">
                        <h5 class="text-start">${elem.title}</h5><p class="text-start"> </p></div></div>`;
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
                    controller_button = document.querySelectorAll('.list-controller');
                    reinvokeButtonListeners(controller_button);
                })
                .catch((error) => {
                    console.error(error);
                })
        })


        
        
        
    });

    


    





});