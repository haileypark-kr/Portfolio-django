$('.btn-example').click(function () {
    var picture_id = $(this).attr('picture_id');
    $('.pop-layer[picture_id='+picture_id+"]").modal({
        show : true
    })
});

$('.nav-item').click(function () {
    var name = $(this).attr('sec-name');
    $([document.documentElement, document.body]).animate({
        scrollTop: $("div[sec-name="+name+"]").offset().top-100
    }, 500);

});

$('.pagename').click(function () {
    $([document.documentElement, document.body]).animate({
        scrollTop: $("#page-top").offset().top-100
    }, 500);
});