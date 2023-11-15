#! /usr/bin/env python
# -*- encoding: UTF-8 -*-


import qi
import argparse
import sys
import time
import signal
import requests
from datetime import datetime

class ProjectModule:
    """
    Wow, there should be some doc here too
    """
    def __init__(self, session):
        """
        """
        print "MyModule init"
        self.session = session
        self.memory = self.session.service("ALMemory")

        self.weather_url = "http://api.openweathermap.org/data/2.5/weather?id=6454573&APPID=49b584e311c58fa09794e5e25a19d1af&UNITS=metric"


    def __del__(self):
        """
        """
        pass


    def print_weather(self):
        """
        """
        info = requests.get(self.weather_url)

        info_json = info.json()
        print "info_json: %s" % info_json

    def get_temperature(self):
        """
        TODO

        **return (float) :**
           * temperature (in degrees)
        """
        info = requests.get(self.weather_url)

        info_json = info.json()
        main_info = info_json["main"]
        print "main_info: %s" % main_info

        temperature_kelvins = main_info["temp"]
        temperature_degrees = temperature_kelvins - 273.15

        print "temperature: % s" % temperature_degrees
        answer = int(temperature_degrees)
        formatted_answer = "{}".format(answer)
        return formatted_answer
    
    def get_pressure(self):
        """
        TODO

        **return (float) :**
           * temperature (in degrees)
        """
        info = requests.get(self.weather_url)

        info_json = info.json()
        main_info = info_json["main"]
        print "main_info: %s" % main_info

        pressure = main_info["pressure"]

        print "pressure: % s" % pressure
        answer = int(pressure)
        formatted_answer = "{}".format(answer)
        return formatted_answer
    
    def get_humidity(self):
        """
        TODO

        **return (float) :**
           * temperature (in degrees)
        """
        info = requests.get(self.weather_url)

        info_json = info.json()
        main_info = info_json["main"]
        print "main_info: %s" % main_info

        humidity = main_info["humidity"]

        print "humidity: % s" % humidity
        answer = int(humidity)
        formatted_answer = "{}".format(answer)
        return formatted_answer
    
    def get_weather_icon(self):
        """
        TODO

        **return (float) :**
           * temperature (in degrees)
        """
        info = requests.get(self.weather_url)

        info_json = info.json()
        main_info = info_json["main"]
        print "main_info: %s" % main_info

        temperature_kelvins = main_info["temp"]
        temperature_degrees = temperature_kelvins - 273.15

        print "temperatureeeeeeeee: % s" % temperature_degrees

        answer = int(temperature_degrees)
        if answer < 0:
            return "images/snow.png"
        if answer < 20:
            return "images/cloudy.png"

        return "images/sun.png"

    def get_datetime(self):
        # Obtenir la date actuelle au format "15 novembre 2023"
        current_date = datetime.now().strftime("%d %B %Y")

        # Remplacer le nom du mois en français
        mois_fr = {
            'January': 'janvier',
            'February': 'février',
            'March': 'mars',
            'April': 'avril',
            'May': 'mai',
            'June': 'juin',
            'July': 'juillet',
            'August': 'août',
            'September': 'septembre',
            'October': 'octobre',
            'November': 'novembre',
            'December': 'décembre'
        }

        for month_en, month_fr in mois_fr.items():
            current_date = current_date.replace(month_en, month_fr)

        # Obtenir l'heure et les minutes au format "15 heures 2"
        current_time = datetime.now().strftime("%H heures %M")

        formatted_datetime = "{}. Il est actuellement {}".format(current_date, current_time)

        print("Formatted date and time: {}".format(formatted_datetime))

        return formatted_datetime



def main(session):

    s = session
    my_module = ProjectModule(s)
    s.registerService("ProjectModule", my_module)

    # Get the service ALTabletService.

    try:
        tabletService = session.service("ALTabletService")
        tabletService.loadApplication("Projet_CouGir")
        tabletService.showWebview()

    except Exception, e:
        print "Error was: ", e



# Getting the service ALDialog
    try:
    	ALDialog = session.service("ALDialog")
        ALDialog.resetAll()
    	ALDialog.setLanguage("French")

    	# Loading the topics directly as text strings
    	topic_name = ALDialog.loadTopic("/home/nao/.local/share/PackageManager/apps/Projet_CouGir/simple_fr.top")
    	# Activating the loaded topics
    	ALDialog.activateTopic(topic_name)

    	# Starting the dialog engine - we need to type an arbitrary string as the identifier
    	# We subscribe only ONCE, regardless of the number of topics we have activated
    	ALDialog.subscribe('simple2')

    except Exception, e:
        print "Error was: ", e

    try:
        raw_input("\n Press Enter when finished:")
    finally:
        # stopping the dialog engine
        ALDialog.unsubscribe('simple2')

        # Deactivating the topic
        ALDialog.deactivateTopic(topic_name)

        # now that the dialog engine is stopped and there are no more activated topics,
        # we can unload our topic and free the associated memory
        ALDialog.unloadTopic(topic_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
