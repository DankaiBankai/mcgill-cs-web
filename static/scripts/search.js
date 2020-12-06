let searchFieldShow = false;

function searchField(){
    if (!searchFieldShow){
        let search = document.getElementById("searchBar");
        search.style.display = "block";
        searchFieldShow = true;
    }
    else{
        let search = document.getElementById("searchBar");
        search.style.display = "none";
        searchFieldShow = false;
    }
}

function go(){
    let input = document.getElementById("searchField").value;
    if (input.toLowerCase() === "prospective"){
        window.location.href = "/prospective";
        console.log("prospective");
    }
    if (input.toLowerCase() === "login"){
        window.location.href = "/login";
        console.log("login");
    }
    if (input.toLowerCase() === "academic"){
        window.location.href = "/academic-menu";
        console.log("academic");
    }
    if (input.toLowerCase() === "research"){
        window.location.href = "/research";
        console.log("research");
    }
    if (input.toLowerCase() === "donate"){
        window.location.href = "/donate";
        console.log("donate");
    }
    if (input.toLowerCase() === "login"){
        window.location.href = "/login";
        console.log("login");
    }
    if (input.toLowerCase() === "people"){
        window.location.href = "/people-menu";
        console.log("people");
    }
    if (input.toLowerCase() === "news"){
        window.location.href = "/news";
        console.log("news");
    }
    if (input.toLowerCase() === "employment"){
        window.location.href = "/employment";
        console.log("employment");
    }
    if (input.toLowerCase() === "about"){
        window.location.href = "/about-menu";
        console.log("about");
    }
}