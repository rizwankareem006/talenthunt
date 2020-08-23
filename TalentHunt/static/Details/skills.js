function chipsDisplay(){
    window.alert("Hey!");
    var val = document.getElementById('chipValue').value
    var item = "<div class=\"chip\">"+val+"<span class='closebtn' onclick=\"this.parentElement.style.display='none'\">&times;</span></div>";
    document.getElementsByClassName('tokens').innerHTML += item; 
}