$(document).ready(function ($) {

    if ($(document).height() <= $(window).height()) {
        $('#cont').height($(document).height());
    }

    $('body').css('overflow','auto');
    $('#loader').hide();

    $('#banner-fade').bjqs({
        'animtype': 'fade',
        'animduration': 800,
        'animspeed': 6000,
        'automatic': true,
        'width': '100%',
        'height': 200,
        'showmarkers': false,
        'responsive': true,
        'showcontrols': false
    });

    $('.accordion').accordion();
/*     $('.subaccordion').accordion(); */
    $('.poigallery').carousel();

    $('#mycarousel').jcarousel();

    $('.accordion').find('li').each(function () {
        if ($(this).find('.item')[0]) {
            $($(this).find('.item')[0]).addClass('active');
        }
    });


    $('#loader').height($(document.body).height() + "px");

    $("#cont a:not([href^='#'])").each(function () {
        if ($(this).is(":not([href^='http://'])")) {
            if ($(this).is(":not([href^='https://'])")) {
                if ($(this).is(":not([href^='mailto:'])")) {
                    if ($(this).is(":not([href^='tel:'])")) {
                        $(this).click(function (e) {
/*                           e.preventDefault(); */
                          $('#loader').show();
                          $('body').css('overflow','hidden');
                        });
                    }
                }
            }
        }
    });

/* <a onclick="window.open('http://www.cinemaimpieriale.it/', '_system', 'toolbar=yes'); return false;" href="#">http://www.cinemaimpieriale.it/</a> */

    $('a[href^="http://"]').attr('target','_blank').each(function() {
      var url = $(this).attr('href');

      $(this).attr('href', '#');
      $(this).click(function(e) {
        e.preventDefault();
        //alert("Opening url in SYSTEM window");

        try {
            window.open(url,'_system');  //, 'toolbar=yes');
        } catch(e) {
            //alert(e.message);
            try {
                window.open(url,'_blank');
            } catch (e) {
                alert(e.message);
            }
        }
        return false;
      });
    });

    $('a[href^="https://"]').each(function() {
      var url = $(this).attr('href');

      $(this).attr('href', '#');
      $(this).click(function(e) {
        e.preventDefault();
        //alert("Opening url in SYSTEM window");

        try {
            window.open(url,'_system');  //, 'toolbar=yes');
        } catch(e) {
            //alert(e.message);
            try {
                window.open(url,'_blank');
            } catch (e) {
                alert(e.message);
            }
        }
        return false;
      });
    });

    $('#currentlanguage span').click(function(e) { 
      e.preventDefault();
      
      $('#languageoverlay').show();
      $('#language').show();
      $(document.body).css('overflow','hidden');
    });

});

function replacementMap() {

    $('#banner-fade').find('img').each(function () {

        if ($replacementmap[$(this).data('src')]) {
            $(this).attr('src', $replacementmap[$(this).data('src')]);
        } else {
            $(this).attr('src', $(this).data('src'));
        }
    });
}
