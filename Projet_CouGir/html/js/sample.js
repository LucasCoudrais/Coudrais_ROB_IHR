$(document).ready(function () {
    session = new QiSession();

    $('#page_start').show();
    $('#page_selection').hide();
    $('#page_weather').hide(); 
    $('#page_date_hour').hide(); 
    $('#page_music').hide(); 
    $('#page_joke_choice').hide();               
    $('#page_joke_choice').hide();               
    $('#page_non_ethical_tip').hide();               
    $('#page_ethical_tip').hide();  

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
                $('#page_weather').hide(); 
                $('#page_date_hour').hide(); 
                $('#page_music').hide(); 
                $('#page_joke_choice').hide();               
                $('#page_non_ethical_tip').hide();               
                $('#page_ethical_tip').hide();   });
        });

        ALMemory.subscriber("SimpleWeb/Page/Start").done(function(subscriber) {

            subscriber.signal.connect(function() {  
                $('#page_start').show();             
                $('#page_selection').hide();
                $('#page_weather').hide(); 
                $('#page_date_hour').hide(); 
                $('#page_music').hide(); 
                $('#page_joke_choice').hide();               
                $('#page_non_ethical_tip').hide();               
                $('#page_ethical_tip').hide();  
            });
        });   

        ALMemory.subscriber("SimpleWeb/Page/Selection").done(function(subscriber) {

            subscriber.signal.connect(function() {     
                $('#page_start').hide();          
                $('#page_selection').show();
                $('#page_weather').hide(); 
                $('#page_date_hour').hide(); 
                $('#page_music').hide(); 
                $('#page_joke_choice').hide();               
                $('#page_non_ethical_tip').hide();               
                $('#page_ethical_tip').hide();  
            });
        });

        ALMemory.subscriber("SimpleWeb/Page/Weather").done(function(subscriber) {
                
                subscriber.signal.connect(function() {  
                    session.service("ProjectModule").done(function (tts) {
                        // tts is a proxy to the ALTextToSpeech service
                        tts.get_temperature().done(function (temp) {
        
                            tts.get_humidity().done(function (hum) {
        
                                tts.get_pressure().done(function (press) {
                                    document.getElementById("text_custom_weather").innerHTML = "Il fait actuellement " + temp + " degrés. Une humidité de " + hum + " pourcent. Et une pression de " + press;
                                    console.log("I speak " + lang);
                                    }).fail(function (error) {
                                        console.log("An error occurred: " + error);
                                    });
                                    console.log("I speak " + lang);
                                }).fail(function (error) {
                                    console.log("An error occurred: " + error);
                                });
                                console.log("I speak " + lang);
                            }).fail(function (error) {
                                console.log("An error occurred: " + error);
                            });
                        }).fail(function (error) {
                        console.log("An error occurred:", error);
                        });
        
                    session.service("ProjectModule").done(function (tts) {
                            // tts is a proxy to the ALTextToSpeech service
                            tts.get_weather_icon().done(function (string) {
                                document.getElementById("weather_img").setAttribute("src", string);
                            }).fail(function (error) {
                            console.log("An error occurred:", error);
                        });

                    $('#page_start').hide();             
                    $('#page_selection').hide();
                    $('#page_weather').show();               
                    $('#page_date_hour').hide(); 
                    $('#page_music').hide(); 
                    $('#page_joke_choice').hide();               
                    $('#page_non_ethical_tip').hide();               
                    $('#page_ethical_tip').hide();                
                });
            });    
        });

        ALMemory.subscriber("SimpleWeb/Page/DateHour").done(function(subscriber) {

            subscriber.signal.connect(function() {  

                session.service("ProjectModule").done(function (tts) {
                    // tts is a proxy to the ALTextToSpeech service
                    tts.get_datetime().done(function (datetime) {
                        document.getElementById("text_custom_datetime").innerHTML = "Nous sommes le " + datetime;
                      }).fail(function (error) {
                        console.log("An error occurred: " + error);
                      });
                  }).fail(function (error) {
                    console.log("An error occurred:", error);
                });

                $('#page_start').hide();             
                $('#page_selection').hide();
                $('#page_weather').hide();               
                $('#page_date_hour').show();   
                $('#page_music').hide(); 
                $('#page_joke_choice').hide();               
                $('#page_non_ethical_tip').hide();               
                $('#page_ethical_tip').hide();              
            });
        }); 
        
        ALMemory.subscriber("SimpleWeb/Page/Music").done(function(subscriber) {

            subscriber.signal.connect(function() {  
                $('#page_start').hide();             
                $('#page_selection').hide();
                $('#page_weather').hide();               
                $('#page_date_hour').hide();   
                $('#page_music').show(); 
                $('#page_joke_choice').hide();               
                $('#page_non_ethical_tip').hide();               
                $('#page_ethical_tip').hide();              
            });
        }); 

        ALMemory.subscriber("SimpleWeb/Page/SelectionJoke").done(function(subscriber) {

            subscriber.signal.connect(function() {  
                $('#page_start').hide();             
                $('#page_selection').hide();
                $('#page_weather').hide();               
                $('#page_date_hour').hide();               
                $('#page_music').hide(); 
                $('#page_joke_choice').show();               
                $('#page_non_ethical_tip').hide();               
                $('#page_ethical_tip').hide();               
            });
        });   
        
        ALMemory.subscriber("SimpleWeb/Page/NonEthicTip").done(function(subscriber) {

            subscriber.signal.connect(function() {  
                
                session.service("ProjectModule").done(function (tts) {
                    // tts is a proxy to the ALTextToSpeech service
                    tts.blague_aleatoire_non_ethic().done(function (non_ethic) {
                        document.getElementById("text_non_ethic_tip").innerHTML = non_ethic;
                    }).fail(function (error) {
                        console.log("An error occurred: " + error);
                    });
                }).fail(function (error) {
                    console.log("An error occurred:", error);
                });

                $('#page_start').hide();             
                $('#page_selection').hide();
                $('#page_weather').hide();               
                $('#page_date_hour').hide();               
                $('#page_music').hide(); 
                $('#page_joke_choice').hide();               
                $('#page_non_ethical_tip').show();               
                $('#page_ethical_tip').hide();               
            });
        });   

        ALMemory.subscriber("SimpleWeb/Page/EthicTip").done(function(subscriber) {

            subscriber.signal.connect(function() {  

                session.service("ProjectModule").done(function (tts) {
                    // tts is a proxy to the ALTextToSpeech service
                    tts.blague_aleatoire_ethic().done(function (ethic) {
                        document.getElementById("text_ethic_tip").innerHTML = ethic;
                      }).fail(function (error) {
                        console.log("An error occurred: " + error);
                      });
                  }).fail(function (error) {
                    console.log("An error occurred:", error);
                });

                $('#page_start').hide();             
                $('#page_selection').hide();
                $('#page_weather').hide();               
                $('#page_date_hour').hide();               
                $('#page_music').hide(); 
                $('#page_joke_choice').hide();               
                $('#page_non_ethical_tip').hide();               
                $('#page_ethical_tip').show();               
            });
        });   

    });


	$('#page_start').on('click', function() {
        console.log("click Start");
        raise('SimpleWeb/Home', 1)
    });

    $('#page_selection_1').on('click', function() {
        console.log("click 1");
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

    $('#page_selection_4').on('click', function() {
        console.log("click 4");
        raise('SimpleWeb/Button4', 1)       
    });

    $('#ethic_joke').on('click', function() {
        console.log("click ButtonEthic");
        raise('SimpleWeb/ButtonEthic', 1)       
    });

    $('#non_ethic_joke').on('click', function() {
        console.log("click ButtonNonEthic");
        raise('SimpleWeb/ButtonNonEthic', 1)       
    });

    $('#page_home1').on('click', function() {
        console.log("click ButtonHome");
        raise('SimpleWeb/Home2', 1)      
    });
    $('#page_end1').on('click', function() {
        console.log("click ButtonEnd");
        raise('SimpleWeb/Start', 1)       
    }); 
    
    $('#page_home2').on('click', function() {
        console.log("click ButtonHome");
        raise('SimpleWeb/Home2', 1)      
    });
    $('#page_end2').on('click', function() {
        console.log("click ButtonEnd");
        raise('SimpleWeb/Start', 1)       
    });   

    $('#page_home3').on('click', function() {
        console.log("click ButtonHome");
        raise('SimpleWeb/Home2', 1)      
    });
    $('#page_end3').on('click', function() {
        console.log("click ButtonEnd");
        raise('SimpleWeb/Start', 1)       
    });  

    $('#page_home4').on('click', function() {
        console.log("click ButtonHome");
        raise('SimpleWeb/Home2', 1)      
    });
    $('#page_end4').on('click', function() {
        console.log("click ButtonEnd");
        raise('SimpleWeb/Start', 1)       
    });  

    $('#page_home5').on('click', function() {
        console.log("click ButtonHome");
        raise('SimpleWeb/Home2', 1)      
    });
    $('#page_end5').on('click', function() {
        console.log("click ButtonEnd");
        raise('SimpleWeb/Start', 1)       
    }); 
    
    $('#page_home6').on('click', function() {
        console.log("click ButtonHome");
        raise('SimpleWeb/Home2', 1)      
    });
    $('#page_end6').on('click', function() {
        console.log("click ButtonEnd");
        raise('SimpleWeb/Start', 1)       
    });  


});
