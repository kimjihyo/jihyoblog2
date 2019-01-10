$(document).ready(function() {
    $("#all span").css("background-color", "rgb(82, 255, 47)");
    $("#all span").css("color", "black");
    $("#all").click(function() {
        $(".posts").show();
        $(".tags span").css("background-color", "black");
        $("#all span").css("background-color", "black");
        $(".tags span").css("color", "rgb(82, 255, 47)");
        $("#all span").css("background-color", "rgb(82, 255, 47)");
        $("#all span").css("color", "black");
        $("#tag-heading").html("All");
    });

    $(".tags span").click(function() {
        $(".posts").show();
        $(".tags span").css("background-color", "black");
        $("#all span").css("background-color", "black");
        $("#all span").css("color", "rgb(82, 255, 47)");
        $(".tags span").css("color", "rgb(82, 255, 47)");
        $("#tag-heading").html($(this).parent().attr("id"));
        $("#"+$(this).parent().attr("id")+" span").css("background-color", "rgb(82, 255, 47)");
        $("#"+$(this).parent().attr("id")+" span").css("color", "black");

        $(".posts:not(.posts."+$(this).parent().attr('id')+")").hide();
    });
});