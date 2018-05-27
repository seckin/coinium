jQuery(document).ready(function($) {
    var MqL = 1070;
    $('a[href="#cd-product-tour"]').on('click', function(event) {
        event.preventDefault();
        $('header').addClass('slide-down');
        if ($(window).width() < MqL) {
            $('body,html').animate({
                'scrollTop': $('#cd-product-tour').offset().top - 30
            }, 200);
        } else {
            $('.cd-main-content').addClass('is-product-tour');
            // uploadVideo(jQuery('.cd-active'));
        }
    });
    $('.cd-prev').on('click', function(event) {
        event.preventDefault();
        var activeSlide = $('.cd-active');
        if (activeSlide.is(':first-child')) {
            showProductIntro();
        } else {
            updateSlider(activeSlide, 'prev');
        }
    });
    $('.cd-next').on('click', function(event) {
        event.preventDefault();
        var activeSlide = $('.cd-active');
        updateSlider(activeSlide, 'next');
    });
    $(document).keyup(function(event) {
        if (event.which == '37' && $('.cd-main-content').hasClass('is-product-tour')) {
            var activeSlide = $('.cd-active');
            if (activeSlide.is(':first-child')) {
                showProductIntro();
            } else {
                updateSlider(activeSlide, 'prev');
            }
        } else if (event.which == '39' && $('.cd-main-content').hasClass('is-product-tour')) {
            var activeSlide = $('.cd-active');
            updateSlider(activeSlide, 'next');
        }
    });
    $(window).on('resize', function() {
        window.requestAnimationFrame(function() {
            if ($(window).width() < MqL) {
                $('.cd-single-item').each(function() {
                    $(this).find('img').css('opacity', 1).end().find('video').hide();
                });
            } else {
                // $('.cd-single-item.cd-active').find('video').show();
                ($('.cd-main-content').hasClass('is-product-tour')) ? $('header').addClass('slide-down'): $('header').removeClass('slide-down');
            }
        });
    });
    $(window).on('scroll', function() {
        window.requestAnimationFrame(function() {
            if ($(window).width() < MqL && $(window).scrollTop() < $('#cd-product-tour').offset().top - 30) {
                $('header').removeClass('slide-down');
            } else if ($(window).width() < MqL && $(window).scrollTop() >= $('#cd-product-tour').offset().top - 30) {
                $('header').addClass('slide-down');
            }
        });
    });

    function showProductIntro() {
        $('header').removeClass('slide-down');
        $('.cd-main-content').removeClass('is-product-tour');
        // $('.cd-active').find('video').get(0).pause();
        // $('.cd-single-item').find('video').each(function() {
        //     $(this).get(0).currentTime = 0;
        // });
    }

    function updateSlider(active, direction) {
        var selected;
        if (direction == 'next') {
            selected = active.next();
            setTimeout(function() {
                active.removeClass('cd-active').addClass('cd-hidden').next().removeClass('cd-move-right').addClass('cd-active').one('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend', function() {
                    active.addClass('cd-not-visible');
                });
            }, 50);
        } else {
            selected = active.prev();
            setTimeout(function() {
                active.removeClass('cd-active').addClass('cd-move-right').prev().addClass('cd-active').one('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend', function() {
                    active.addClass('cd-not-visible');
                });
            }, 50);
        }
        selected.removeClass('cd-not-visible');
        updateSliderNav(selected);
        // uploadVideo(selected);
    }

    function updateSliderNav(selected) {
        (selected.is(':last-child')) ? $('.cd-next').addClass('cd-inactive'): $('.cd-next').removeClass('cd-inactive');
        $('.cd-loader').stop().hide().css('width', 0);
    }

    function uploadVideo(selected) {
        selected.siblings('.cd-single-item').find('video').each(function() {
            $(this).get(0).pause();
        })
        if (selected.find('video').length > 0) {
            selected.find('video').eq(0).show().get(0).play();
        } else {
            var videoUrl = selected.find('.cd-image-container img').data('video'),
                video = $('<video loop><source src="' + videoUrl + '.mp4" type="video/mp4" /><source src="' + videoUrl + '.webm" type="video/webm" />Sorry, your browser does not support HTML5 video.</video>');
            video.appendTo(selected.find('.cd-image-wrapper')).hide();
            var loaded = 'false';
            selected.on('canplaythrough', 'video', function() {
                loaded = 'true';
            });
            $('.cd-loader').show().animate({
                width: '50%'
            }, 1500, function() {
                var timeout = setInterval(function() {
                    if (loaded) {
                        $('.cd-loader').animate({
                            width: '100%'
                        }, 100, function() {
                            $('.cd-loader').css('width', 0);
                            selected.find('video').show().get(0).play();
                            selected.find('img').css('opacity', 0);
                            clearInterval(timeout);
                        });
                    } else {
                        var windowWidth = $(window).width(),
                            widthNew = $('.cd-loader').width() + 10;
                        if (widthNew < windowWidth) {
                            $('.cd-loader').show().animate({
                                width: widthNew + 'px'
                            }, 500);
                        }
                    }
                }, 500);
            });
        }
    }
});
