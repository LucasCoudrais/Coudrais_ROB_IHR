#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: A Simple class to test dialogue and media"""

import qi
import time
import sys
import argparse


class DialogTest(object):
    """
    A simple class to make a python chatbot in a terminal with naoqi (*.top files)
    """

    def __init__(self, app):
        """
        Initialisation of qi framework and event detection.
        """
        super(DialogTest, self).__init__()
        app.start()
        session = app.session
        # Get the service ALMemory.
        self.memory = session.service("ALMemory")

        self.subscriber = self.memory.subscriber("Dialog/Answered")
        self.subscriber.signal.connect(self.on_event_answered)

        # Getting the service ALDialog
        try:
            self.ALDialog = session.service("ALDialog")
            self.ALDialog.resetAll()
            self.ALDialog.setLanguage("French")
            # Loading the topics directly as text strings
            self.topic_name = self.ALDialog.loadTopic("~/Documents/home/Documents/S9/IHR/Exemples/ihr-raph-main/examples/TerminalNaoqiChat/topfiles/ExampleDialog_frf.top")

            # Activating the loaded topics
            self.ALDialog.activateTopic(self.topic_name)

            # Starting the dialog engine - we need to type an arbitrary string as the identifier
            # We subscribe only ONCE, regardless of the number of topics we have activated
            self.ALDialog.subscribe('ExampleDialog')

        except Exception, e:
            print "Error was: ", e

    def on_event_answered(self, value):
        """
        Callback for answers in Dialog
        """
        print "R: " + value

    def run(self):
        """
        Loop on, wait for events until manual interruption.
        """
        print "Starting HumanGreeter"
        try:
            while True:
                fi = raw_input('H: ')
                #print fi
                self.ALDialog.forceInput(fi)
                self.ALDialog.forceOutput()
                time.sleep(1)
        except KeyboardInterrupt:
            print "Interrupted by user, stopping HumanGreeter"

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

    demoDialog = DialogTest(app)
    demoDialog.run()
