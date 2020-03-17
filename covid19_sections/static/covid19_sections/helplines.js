$(document).ready(function () {

    $("div.country-table-row-group:nth-child(odd)").css({"background-color": "#f1f3f4"})

    if($("div.national-number p").text() === "") {
      $("div.national-number").hide()
    }

    if($("div.national-email p").text() === "") {
      $("div.national-email").hide()
    }

});