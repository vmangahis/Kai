let authenticated = JSON.parse(document.getElementById('authenticated').textContent);
let testData = JSON.parse(document.getElementById('data'))

if (!authenticated) {
    document.getElementById("login-watchlist").addEventListener("click", (ev) => {
        document.location.href = "/login/";
    });
}