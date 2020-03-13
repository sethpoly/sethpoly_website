// Smooth scrolling for all NAV ITEMS
document.getElementById('nav-about').addEventListener('click', function() {
    SmoothVerticalScrolling(document.getElementById('about-header'), 350, "top");
});
document.getElementById('nav-projects').addEventListener('click', function() {
    SmoothVerticalScrolling(document.getElementById('projects-header'), 350, "top");
});
document.getElementById('nav-contact').addEventListener('click', function() {
    SmoothVerticalScrolling(document.getElementById('contact-header'), 350, "top");
});

// Scroll to top on page refresh
window.onbeforeunload = function () {
  window.scrollTo(0, 0);
}




// The outer modal element
var modal = document.getElementById('modal');

// Display the project-modal based off what project was clicked
// @param: the project that was chosen
function showProject(id) {
    
    // To hold values for each different element in the modal
    var title;
    var img;
    var subheading;
    var description;
    var link;
        
    switch(id) {
        case 'project-transit':
            title='Lost in Transit';
            img='transit-modal.png';
            subheading='Video-game published on Steam. Developed using Gamemaker Studio 2.';
            description='As a solo video-game developer. I designed, programmed, and marketed Lost in Transit. I self-published the title in January 2020 on Steam.';
            link='https://store.steampowered.com/app/1165600/Lost_in_Transit/';
            break;
        case 'project-turntabler':
            title='Turntabler';
            img='turntabler-modal.png';
            subheading='Interactive website developed using Javascript, node.js, and the Spotify Web API.';
            description='A node.js website that dynamically creates virtual vinyl records based off what Spotify artist the user searches for. Utilized the Spotify Web API endpoints to return the data about all artists/albums.';
            link='http://turntabler.com/';
            break;
        case 'project-memjars':
            title='Memjars';
            img='memjars-modal.png';
            subheading='Social media website developed using Firebase and Javascript';
            description='Memjars is a social media platform used for the sole purpose to share and reminisce memories between friends, colleagues, and family. Users create <em>memory jars</em>, share them with their friends, and start filling the jars with memories, together.';
            link='https://github.com/sethpoly/memjars';
            break;
    }
    
    // Append the newly created HTML to the modal to view
    modal.innerHTML = '<div class="modal-content"><div class="modal-header"><span id="btn-close-modal" onclick="closeModal()"class="close">&times;</span><img class="modal-img" src="'+img+'"></div><div class="modal-body"><h3 class="modal-heading">'+title+'</h3><p class="modal-subheading">'+subheading+'</p><hr><p class="modal-description">'+description+'</p><a href="'+link+'" target="_blank"><button class="btn-viewproject">View project</button></a></div></div>';
    
    // Display modal
    setTimeout(displayModal(modal), 1);
}

// Display modal after timer is up
function displayModal(modal) {
        modal.style.display = 'block';
}

// When the user clicks anywhere outside of the modal, close it
document.onclick = function(event) {
    if(event.target == modal) {
        modal.style.display = "none";
  }
}

// Close the modal when the X is clicked
function closeModal() {
    modal.style.display = "none";
}

function SmoothVerticalScrolling(e, time, where) {
    var eTop = e.getBoundingClientRect().top;
    var eAmt = eTop / 100;
    var curTime = 0;
    while (curTime <= time) {
        window.setTimeout(SVS_B, curTime, eAmt, where);
        curTime += time / 100;
    }
}

function SVS_B(eAmt, where) {
    if(where == "center" || where == "")
        window.scrollBy(0, eAmt / 2);
    if (where == "top")
        window.scrollBy(0, eAmt);
}



