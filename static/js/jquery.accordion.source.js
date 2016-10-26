/**
*	@name							Accordion
*	@descripton						This Jquery plugin makes creating accordions pain free
*	@version						1.3
*	@requires						Jquery 1.2.6+
*
*	@author							Jan Jarfalk
*	@author-email					jan.jarfalk@unwrongest.com
*	@author-website					http://www.unwrongest.com
*
*	@licens							MIT License - http://www.opensource.org/licenses/mit-license.php
*/

(function(jQuery){
  jQuery.fn.extend({  
    accordion: function() {       
      return this.each(function() {

        var $ul = $(this);
        if($ul.data('accordiated'))
        return false;

        $.each($ul.find('ul, li>div'), function(){
          $(this).data('accordiated', true);
          $(this).hide();
        });

        $.each($ul.find('.accordionitem'), function(){
          $(this).click(function(e){
            e.preventDefault();
            activate(this);
            return void(0);
          });
        });

        function activate(el,effect) {
          $(el).parent('li').toggleClass('active').siblings().removeClass('active').children('ul, div').slideUp('fast');
          $(el).siblings('ul, div')[(effect || 'slideToggle')]((!effect)?'fast':null);

          try { 
            $(el).parent().find('.subaccordion').find('.carousel').carousel();
          } catch(e) { 
          }
        }

        if (location.hash && location.hash.length > 0) {
          var openlink = $('.accordion').find(location.hash).find('.accordionitem');
          activate(openlink, 'toggle');
        }
      });
    } 
  }); 
})(jQuery);
