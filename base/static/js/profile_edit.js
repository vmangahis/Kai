document.addEventListener("DOMContentLoaded", () => {
   
    let upload = document.getElementById("id_avatar");
    let image = document.getElementById("avatar-label");
    upload.addEventListener("change", function(e) {
            let file = document.getElementById("id_avatar").files[0];
            let rd = new FileReader();
            rd.onloadend = function(e)
            {image.style.backgroundImage = "url(" + rd.result + ")";
                }
            if(file){
                rd.readAsDataURL(file);
            }
    })
})