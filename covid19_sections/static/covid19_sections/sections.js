$(document).ready(function() {
    $(".section p").hide();

    /* The Django template uses forLoop.counter to generate the index value in the class name.
       Iterating through the block appends the index value to #section so that each element will see the toggle effect
       the p element is appended to the #section to generate a unique identifier for each block; "Ex: #section1 p"*/
    $(".section").each(function (index) {
         var index = index + 1;
         var section = "#section" + index;
         var p = section + " p";

         $(section).click(function (){
             if($(this).find($(".fas")).hasClass("fa-chevron-down"))
             {
                 $(this).find($(".fas")).removeClass("fa-chevron-down").addClass("fa-chevron-up")
             }
             else if($(this).find($(".fas")).hasClass("fa-chevron-up"))
             {
                  $(this).find($(".fas")).removeClass("fa-chevron-up").addClass("fa-chevron-down")
             }
             $(p).slideToggle(200);

             $(".message").css({transition: "opacity .5s ease-out", opacity: "0"});
             $(".message").delay(500).hide(500);
        })
    })


});