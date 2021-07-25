console.log("hello world");

//VARIABLES FROM "home.html":

const saveTripButton = document.getElementById('save-trip-button');
const saveTripForm = document.getElementById('save-trip-from');
const alertBox = document.getElementById('alert-box');
const tripCreated = document.getElementById('trip_created')



// FUNCTIONS:

const handleAlerts = (type, msg) => {
    /*
    Parameters:
    type: the type of alert one wants displayed
    msg: the message one wants displayed

    Returns an alert written in html using boostrap
    */
    alertBox.innerHTML = `
        <div class="alert alert-${type}" role="alert">
            ${msg}
        </div>
    `
}

saveTripForm.addEventListener('submit', ()=>{
    console.log('clicked')
    if(tripCreated){
        handleAlerts('success', 'Trip Created');
    }
    else{
        handleAlerts('danger', 'Oops...something went wrong');
    }
})