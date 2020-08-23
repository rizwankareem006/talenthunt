$(function(){
    $("#realsubmit").hide();
    $("#skillset").hide();
    $("#addToken").click(function(){
        $("#tokens").append(
            "<div class=\"chip\"><span class='tokenValues'>"+$("#chipValue").val()+"</span><span class='closebtn' onclick=\"$($(this).parent()).remove();\">&times;</span></div>"
        );
        $("#chipValue").val("");
    });
});