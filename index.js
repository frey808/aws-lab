function openNav(){
    document.getElementById("nav").style.display = "inline";
    document.getElementById("opennav").style.display = "none";
}

function closeNav(){
    document.getElementById("nav").style.display = "none";
    document.getElementById("opennav").style.display = "inline";
}

function updateData(apiResponse){
    document.getElementById("test").innerHTML = apiResponse;
}

function swap(){
    //swap view
}

function fetchData(){
    // fetch('https://mqbmmuwreh.us-east-2.awsapprunner.com/').then((response) => { //for deployment ONLY - comment out while testing locally
    fetch('http://localhost:8080/').then((response) => { //for local testing ONLY - comment out before pushing
        if (response.status === 200){
            return (response.json()) ;
        }else{
            console.log("HTTP error:" + response.status + ":" +  response.statusText);
            return ([["status ", response.status]]);
        }
    }).then ((jsonOutput) => {
        updateData(jsonOutput);
    }).catch((error) => {
        console.log(error);
        updateData("error caught");
    })

}

function createItem(){
    //add
}

function editItem(){
    //edit
}

function deleteItem(){
    //delete
}