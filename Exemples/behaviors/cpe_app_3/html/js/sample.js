﻿$(document).ready(function () {
    session = new QiSession();

    $('#page_empty').show();
    $('#page_1').hide();
    $('#page_2').hide();


    session.service("ALMemory").done(function(ALMemory) {

        ALMemory.subscriber("Example/Page0").done(function(subscriber) {

            subscriber.signal.connect(function() {
                $('#page_empty').show();
                $('#page_1').hide();
                $('#page_2').hide();
            });
        });


        ALMemory.subscriber("Example/Page1").done(function(subscriber) {

            subscriber.signal.connect(function() {
                $('#page_1').show();
                $('#page_empty').hide();
                $('#page_2').hide();

            });
        });

        ALMemory.subscriber("Example/Page2").done(function(subscriber) {

            subscriber.signal.connect(function() {
                $('#page_2').show();
                $('#page_empty').hide();
                $('#page_1').hide();
            });
        });
    });

    function raise(event, value) {
        session.service("ALMemory").done(function(ALMemory) {
            ALMemory.raiseEvent(event, value);
        });
    }


    $('#page_1_1').on('click', function() {
        console.log("click 1");
        raise('Example/Button1', 1)
    });

    $('#page_1_2').on('click', function() {
        console.log("click 2");
        raise('Example/Button2', 1)
    });

    $('#page_1_3').on('click', function() {
        console.log("click 3");
        raise('Example/Button3', 1)
    });

    $('#red').on('click', function() {
        console.log("click red");
        raise('Example/Red', 1)
    });

    $('#blue').on('click', function() {
        console.log("click blue");
        raise('Example/Blue', 1)
    });

    $('#yellow').on('click', function() {
        console.log("click yellow");
        raise('Example/Yellow', 1)
    });


});
