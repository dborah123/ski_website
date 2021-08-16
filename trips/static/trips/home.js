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

function handleAlertsLink(type, msg1, linkmsg, msg2, link){
    /*
    Parameters: type: the type of message one wants to display
    msg1: the message before the link
    linkmsg: the message the has the link
    ms2: the message after the link
    link: link

    Returns an alert written in html using bootstrap
    */

    const alertBox = document.getElementById('alert-box');
    console.log("here ayo")
    alertBox.innerHTML = `
        <div class="alert alert-${type}" role="alert">
            ${msg1}<a href=${link} class="alert-link">${linkmsg}</a>${msg2}
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