#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: A Simple class to test dialogue and media"""

import qi
import time
import sys
import argparse


class MediaTest(object):
    """
    A simple class to react to face detection events.
    """

    def __init__(self, app):
        """
        Initialisation of qi framework and event detection.
        """
        super(MediaTest, self).__init__()
        app.start()
        session = app.session
        # Get the service ALMemory.
        self.memory = session.service("ALMemory")
        # Connect the event callback.
        self.subscriber = self.memory.subscriber("cpeshow")
        self.subscriber.signal.connect(self.on_event_cpeshow)
        # Get the service ALAudioPlayer
        self.audio_player_service = session.service("ALAudioPlayer")
    

        # Get the service ALTabletService.
        try:
            self.tabletService = session.service("ALTabletService")
            self.tabletService.showImage("http://198.18.0.1/apps/essai_script_multimedia/love.jpg")

        except Exception, e:
            print "Error was: ", e

        # Getting the service ALDialog
        try:
            self.ALDialog = session.service("ALDialog")
            self.ALDialog.resetAll()
            self.ALDialog.setLanguage("French")
            # Loading the topics directly as text strings
            self.topic_name = self.ALDialog.loadTopic("/home/nao/.local/share/PackageManager/apps/essai_script_multimedia/topfiles/ExampleDialog_frf.top")

            # Activating the loaded topics
            self.ALDialog.activateTopic(self.topic_name)

            # Starting the dialog engine - we need to type an arbitrary string as the identifier
            # We subscribe only ONCE, regardless of the number of topics we have activated
            self.ALDialog.subscribe('ExampleDialog')

        except Exception, e:
            print "Error was: ", e

    def on_event_cpeshow(self, value):
        """
        Callback for event cpe show
        """
        print "cpeshow call back call"
        self.tabletService.showImage("http://198.18.0.1/apps/essai_script_multimedia/logo_CPE.jpg")
        #Launchs the playing of a file
        self.audio_player_service.playFile("/home/nao/.local/share/PackageManager/apps/essai_script_multimedia/sounds/Happy-sound.mp3")
        self.tabletService.showImage("http://198.18.0.1/apps/essai_script_multimedia/love.jpg")

    def run(self):
        """
        Loop on, wait for events until manual interruption.
        """
        print "Starting HumanGreeter"
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print "Interrupted by user, stopping HumanGreeter"
            #xxx.unsubscribe("cpeshow")
            # stopping the dialog engine
            self.ALDialog.unsubscribe('ExampleDialog')
            # Deactivating the topic
            self.ALDialog.deactivateTopic(self.topic_name)
            # now that the dialog engine is stopped and there are no more activated topics,
            # we can unload our topic and free the associated memory
            self.ALDialog.unloadTopic(self.topic_name)
            #stop
            sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    try:
        # Initialize qi framework.
        connection_url = "tcp://" + args.ip + ":" + str(args.port)
        app = qi.Application(["CpeDemo", "--qi-url=" + connection_url])
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    demoMedia = MediaTest(app)
    demoMedia.run()
