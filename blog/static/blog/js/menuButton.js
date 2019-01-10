$(document).ready(function() {
    $("#menu-icon").click(function() {
        $("#dropdown-menu").slideToggle();
    })
    
    $(window).resize(function() {
        if($(window).width() > 550) {
            $("#dropdown-menu").hide();
        }
    });
});