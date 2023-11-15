$(document).ready(function () {
    session = new QiSession();

    function saySomething() {
        session.service("ALTextToSpeech").done(function(tts) {
            tts.say("Je dis quelque chose");
        }).fail(function(error) {
            console.log("An error occured: ", error);
        })
    };


    function wake() {
        session.service("ALMotion").done(function(motion) {
            motion.wakeUp();
        });
    }

    function rest() {
        session.service("ALMotion").done(function(motion) {
            motion.rest();
        });
    }


    $('#say').on('click', function() {
        console.log("click on say");
        saySomething();
    })


    $('#wake').on('click', function() {
        console.log("click on wake");
        wake();
    })

    $('#rest').on('click', function() {
        console.log("click on rest");
        rest();
    })




});
