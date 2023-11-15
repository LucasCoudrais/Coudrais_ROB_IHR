$(document).ready(function () {
    session = new QiSession();

    $('#page_start').show();
    $('#page_selection').hide();
    $('#page_YesNo').hide(); 

    $('#page_selection_1_selec').hide();
    $('#page_selection_2_selec').hide();
    $('#page_selection_3_selec').hide();    


    function raise(event, value) {
        session.service("ALMemory").done(function(ALMemory) {
            ALMemory.raiseEvent(event, value);
        });
    }

    session.service("ALMemory").done(function(ALMemory) {

        ALMemory.subscriber("SimpleWeb/Page/Empty").done(function(subscriber) {

            subscriber.signal.connect(function() {
                $('#page_selection').hide();
                $('#page_start').hide();
                $('#page_YesNo').hide(); 
            });
        });


        ALMemory.subscriber("SimpleWeb/Page/Selection").done(function(subscriber) {

            subscriber.signal.connect(function() {     
                $('#page_start').hide();          
                $('#page_selection').show();
                $('#page_YesNo').hide(); 
            });
        });

        ALMemory.subscriber("SimpleWeb/Page/Start").done(function(subscriber) {

            subscriber.signal.connect(function() {  
                $('#page_start').show();             
                $('#page_selection').hide();
                $('#page_YesNo').hide(); 
            });
        });        


        ALMemory.subscriber("SimpleWeb/Page/YesNo").done(function(subscriber) {

            subscriber.signal.connect(function() {  
                $('#page_start').hide();             
                $('#page_selection').hide();
                $('#page_YesNo').show(); 

                $('#page_selection_1_selec').hide();
                $('#page_selection_2_selec').hide();
                $('#page_selection_3_selec').hide();                
            });
        });         


        ALMemory.subscriber("SimpleWeb/Select").done(function(subscriber) {

            subscriber.signal.connect(function() {

                ALMemory.getData("SimpleWeb/Select").then(function(data) {
                    data=="S"  ?    $('#page_selection_1_selec').show() : $('#page_selection_1_selec').hide(); // permet d'afficher ou non "is chosen" pour le choix 1
                    data=="P"  ?    $('#page_selection_2_selec').show() : $('#page_selection_2_selec').hide(); // permet d'afficher ou non "is chosen" pour le choix 2
                    data=="B"  ?    $('#page_selection_3_selec').show() : $('#page_selection_3_selec').hide(); // permet d'afficher ou non "is chosen" pour le choix 3

                }, console.log);    
                
              
                raise('SimpleWeb/Next', 1);
     
                

            });
        });        

    });



	$('#page_start').on('click', function() {
        console.log("click Start");
        raise('SimpleWeb/Start', 1)
    });

    $('#page_selection_1').on('click', function() {
        console.log("click 1");s
        raise('SimpleWeb/Button1', 1)
    });

    $('#page_selection_2').on('click', function() {
        console.log("click 2");
        raise('SimpleWeb/Button2', 1)      
    });

    $('#page_selection_3').on('click', function() {
        console.log("click 3");
        raise('SimpleWeb/Button3', 1)       
    });



    $('#page_yes').on('click', function() {
        console.log("click ButtonYes");
        raise('SimpleWeb/ButtonYes', 1)      
    });

    $('#page_no').on('click', function() {
        console.log("click ButtonNo");
        raise('SimpleWeb/ButtonNo', 1)       
    });    


});
