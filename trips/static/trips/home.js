//VARIABLES FROM "home.html":

function handleAlerts(type, msg){
    /*
    Parameters:
    type: the type of alert one wants displayed
    msg: the message one wants displayed

    Returns an alert written in html using boostrap
    */
    const alertBox = document.getElementById('alert-box');
    console.log(msg);
    alertBox.innerHTML = `
        <div class="alert alert-${type}" role="alert">
            ${msg}
        </div>
    `
}

function redirectToTrips(url){
    /*
    PARAMETERS:
    None

    Redirects user to trips overview page if they decide to delete a trip
    */
    console.log("here");
    console.log(typeof url);
    alert("redirecting...");
    window.location.replace(url);

}