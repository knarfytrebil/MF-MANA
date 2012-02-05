//fix ie6 position
$(function(){
    var h = $(window).height() - 40;
    var h2 = $(window).height() - 84;
    var w = $(window).width() - 154;
    var w2 = $(window).width() -372;
    $('.frame-container').css({height: h+'px'});
    $('.col-side').css({height: h+'px'});
    $('.col-frame').css({height: h+'px'});
    $('.directory-tree').css('height','300px');
    $('.col-sub').css({height: h2+'px'});
    $('.page-main').css({height: h2+'px'});
    $('.page-main').css({width: w+'px'});
    $('.col-main').css({width: w2+'px'});
})
