let authenticated = JSON.parse(document.getElementById('authenticated').textContent);
let testData = JSON.parse(document.getElementById('data'))
console.log(testData);
if (!authenticated) {
    document.getElementById("login-watchlist").addEventListener("click", (ev) => {
        document.location.href = "/login/";
    });
}

let addtoList = document.getElementById('addtoList');
/*addtoList.addEventListener('click', ev => {
    fetch('addtolist/',

        {
            method: "POST",

        }
    )
});*/