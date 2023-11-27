#! /usr/bin/env python
# -*- encoding: UTF-8 -*-


import qi
import argparse
import sys
import time
import signal
import requests
import random
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
        self.player = self.session.service("ALAudioPlayer")
        self.behavior = self.session.service("ALBehaviorManager")

        self.weather_url = "http://api.openweathermap.org/data/2.5/weather?id=6454573&APPID=49b584e311c58fa09794e5e25a19d1af&UNITS=metric"
        self.blague_index = -1
        self.blague_non_index = -1
        # self.musique_index = -1





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

        temperature_kelvins = main_info["temp"]
        temperature_degrees = temperature_kelvins - 273.15

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

    def blague_aleatoire_ethic(self):
        blagues = [
            "J’ai 40 boules toutes rondes et j’excite les vieilles dames, Qui suis-je ?\nLe Bingo !",
            "Qu’est-ce qu’un nem avec des écouteurs ?\nUn nem P3.",
            "Quel est le comble pour un joueur de bowling ?\nC’est de perdre la boule !",
            "Quel métier les chiens peuvent-ils exercer ?\nElectrichien !",
            "Pourquoi les plongeurs sous-marin plongent-ils toujours en arrière et jamais en avant ?\nParce que sinon ils tombent dans le bateau.",
            "Pourquoi les flamands roses lèvent une patte en dormant ?\nParce que s’ils levaient les deux, ils tomberaient.",
            "Quelle est la plante qu’on n’arrose jamais et qu’on écrase sans qu’elle ne s’abîme ?\nLa plante des pieds.",
            "Qu’est-ce qu’un homme avec une mitraillette dans un champ de blé ?\nUn céréale killer…",
            "Quelle est la différence entre un crocodile et un alligator ?\nC’est Caïman la même chose…",
            "Comment appelle-t-on les petits d’une oie ?\nLes noisettes.",
            "Pourquoi les maisons en Angleterre ne sont-elles pas solides ?\nParce qu’elles sont en glaise.",
            "Que fait une vache avec une radio ?\nDe la meuhsique !",
            "Quel est le comble pour un marin ?\nAvoir le nez qui coule !",
            "Que dit un oignon quand il se cogne ?\nAïe",
            "Quelles sont les lettres les plus vieilles de l’alphabet ?\nA G",
            "Connais-tu la blague de la chaise ?\nElle est pliante !",
            "Comment appelle-t-on du riz que l’on peut manger en voiture ?\nDu risotto",
            "Quel est le fruit préféré de l’homme ?\nL’ananas",
            "Qu’est-ce qu’un squelette dans une armoire ?\nC’est quelqu’un qui a gagné à cache-cache.",
            "Quelle est la ressemblance entre un facteur et un jongleur ?\nIl leur faut tous les deux beaucoup d’adresse.",
            "Quel est le comble pour un marin ?\nAvoir le nez qui coule !",
            "Quels sont les animaux qui sont souvent fatigués ?\nLe dodo et le paresseux !",
            "Quelle est la blague à deux balles ?\nPan Pan !",
            "A combien rouliez-vous ? demande le gendarme.\nA deux seulement, mais si vous voulez monter, il reste de la place",
            "Quel est le comble pour un professeur de géographie ?\nC’est de perdre le nord",
            "De quelle couleur sont les parapluies quand il pleut ?\nIls sont tout verts !",
            "Que dit un vitrier à son fils pour qu’il soit sage ?\nTiens-toi à carreaux si tu veux une glace !",
            "Quelle est la profession du soleil ?\nChef de rayons.",
            "Que dit un informaticien quand il s’ennuie ?\nJe me fichier.",
            "Quel est l’animal le plus à la mode ?\nLa taupe modèle !",
            "Que dit un citron qui fait un cambriolage ?\nPlus un zeste !!",
            "Quel est le sport préféré des chèvres ?\nL’aéro-bique",
            "Quel est le sport préféré des insectes ?\nLe criquet",
            "Comment sait-on quand c’est un gorille qui sonne à la porte ?\nÇa fait king-kong !",
            "Quel super-héros joue le mieux au base-ball ?\nBatte-Man",
            "Quel est le point commun entre un pêcheur et un mannequin ?\nIls surveillent leur ligne !",
            "Pourquoi les escargots ne font jamais de sport ?\nParce qu’ils en bavent.",
            "Que fait une ampoule quand elle grille ?\nElle appelle à LED"
        ]

        if(self.blague_index == -1):
            self.blague_index = random.randint(0, blagues.__len__()-1)
            result = blagues[self.blague_index]
        else : 
            result = blagues[self.blague_index]
            self.blague_index = -1

        print "blague ethique: % s" % result

        return result
    
    def blague_aleatoire_non_ethic(self):
        blagues = [
            "Des enfants sonnent chez une dame. La dame leur répond :\nQu’y a-t-il ?\nOn aimerait savoir si votre fils Titouan peut jouer avec nous ?\nMais vous savez que Titouan n’a ni bras ni jambe ?\nOui mais on a besoin d’un ballon.",
            "Pourquoi la petite fille tombe-t-elle de la balançoire ?\nParce qu'elle n’a pas de bras.",
            "Qu'est-ce qui est pire qu'un bébé dans une poubelle ?\nUn bébé dans deux poubelles.",
            "Qu'est-ce qui est mieux que gagner une médaille d'or aux Jeux Paralympiques ?\nMarcher.",
            "Que faire quand on trouve un épileptique en crise dans une baignoire ?\nAjouter de la lessive et y jeter son linge sale.",
            "Maman, maman, papa s'est pendu dans le jardin !\nPoisson d’avril ! Il s’est pendu dans le grenier !",
            "Un enfant juif dans un camp de concentration joue avec de la poussière. Un garde s’approche et dit :\nEh bien alors ? On joue avec Papa et Maman ?",
            "Un père à son fils :\nFiston, tu sais ce qu’a dit ta sœur quand elle a perdu sa virginité ?\nOh non papa…\nExactement !",
            "Ma femme a rigolé quand je lui ai dit que j’avais encore le corps d’un jeune de 18 ans. Elle a beaucoup moins ri quand elle l’a vu en morceaux dans le congélateur.",
            "Dans une classe, une professeur demande à ses élèves :\nQui peut me dire quels sont les meilleurs matériaux combustibles ?\nUn élève juif, ayant la réponse, lève la main en espérant être interrogé :\nJe sais ! Je sais ! Moi Madame ! Moi !\nExcellente réponse quoi d’autre ?",
            "Quel est le point commun entre un nécrophile et un homme qui se baigne en Bretagne ?\nTous les deux disent : « Elle est froide mais une fois dedans, elle est bonne. »",
            "Quel est le point commun entre un juif et des chaussures ?Il y en a plus en 39 qu’en 45.",
        ]

        if(self.blague_non_index == -1):
            self.blague_non_index = random.randint(0, blagues.__len__()-1)
            result = blagues[self.blague_non_index]
        else : 
            result = blagues[self.blague_non_index]
            self.blague_non_index = -1

        return result  
    

    def hello_arm(self):
        """
        Launch and stop a behavior, if possible.
        """
        # Check that the behavior exists.
        if (self.behavior.isBehaviorInstalled("Stand/Gestures/Hey_1")):
            # Check that it is not already running.
            if (not self.behavior.isBehaviorRunning("Stand/Gestures/Hey_1")):
                # Launch behavior. This is a blocking call, use _async=True if you do not
                # want to wait for the behavior to finish.
                self.behavior.startBehavior("Stand/Gestures/Hey_1", _async=True)
                time.sleep(0.5)
            else:
                print "Behavior is already running."

        else:
            print "Behavior not found."
        return





    def play_random_music(self):        
        paths = [
            "/home/nao/.local/share/PackageManager/apps/Projet_CouGir/music/acoustic-guitar-loop-f-91bpm-132687.mp3",
            "/home/nao/.local/share/PackageManager/apps/Projet_CouGir/music/fat-kick-drumloop-99bpm-141016.mp3",
            "/home/nao/.local/share/PackageManager/apps/Projet_CouGir/music/pigeons-flying-6351.mp3",
            "/home/nao/.local/share/PackageManager/apps/Projet_CouGir/music/suspense_strings_001wav-14805.mp3",
            "/home/nao/.local/share/PackageManager/apps/Projet_CouGir/music/timbo-drumline-loop-103bpm-171091.mp3"
        ]


        randIndex = random.randint(0, paths.__len__()-1)

        self.player.playFile(paths[randIndex])

def main(session):

    s = session
    my_module = ProjectModule(s)
    s.registerService("ProjectModule", my_module)

    # Get the service ALTabletService.

    try:
        tabletService = session.service("ALTabletService")
        tabletService.loadApplication("Projet_CouGir")
        # tabletService.showWebview()
        # tabletService.clearWebview()
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
        my_module.hello_arm()

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
