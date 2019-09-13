$(document).ready(function() {
    $('.homepage-image').hover(
        function() {
            $(this).find('img').css('opacity', '0.5');
            $(this).find('figure-caption').css('opacity','1');
        },
        function() {
            $(this).find('img').css('opacity', '1');
            $(this).find('figure-caption').css('opacity','0');
        }
    );
});
