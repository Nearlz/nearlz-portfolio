const sidebarButton = document.querySelector('#sidebar-button-main')

sidebarButton.addEventListener('click',function(){
    document.getElementById('sidebar').classList.toggle('active');
} )

function goHome(section){
    window.location.href = "#home"
}
function goAbout(section){
    window.location.href = "#about"
}
function goKnowledge(section){
    window.location.href = "#knowledge"
}
function goExtra(section){
    window.location.href = "#extra"
}
function goContact(section){
    window.location.href = "#contact"
}

const toggle = document.getElementById('sidebar-button-main')
const sidebar = document.getElementById('sidebar')

document.onclick = function(e){
    if(e.target.id !== 'sidebar' && e.target.id !== 'sidebar-button-main' && e.target.id !== 'sidebar-main'){
        toggle.classList.remove('active');
        sidebar.classList.remove('active');
    }
}

if ($(window).width() >= 768) {
    //My mobile specific code

    VanillaTilt.init(document.querySelectorAll(".extra-container"),{
        max:25,
        speed:150
    });
    
  }