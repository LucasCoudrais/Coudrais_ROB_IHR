# Examples


## Liste des exemples 

- essai_script_multimedia
  - Affichage image sur tablette
  - Jouer un son
  - Intercation vocale

- SimpleWeb
  - Affichage page web sur tablette
  - Interaction vocale doublé sur tablette

- SimpleMove
  - Tourne sur lui-même de 30° vers la gauche puis vers la droite avant de revenir à l'angle initial
  - Fait coucou de la main droite 

- TerminalNaoqiChat
  - Chatbot dans un terminal à partir de python / naoqi / *.top files --> Permet de tester un fichier *.top sans robot ni Choregraphe

## Charger un exemple dans le robot

Pour transférer des fichiers, utilisez `scp` (ligne de commande), ou `FileZilla` (outil graphique). Le dossier de l'exemple doit être copié dans le dossier du robot suivant : `/home/nao/.local/share/PackageManager/apps/`  

- nom d'utilisateur : `nao`
- MDP : demander au prof
- port (par defaut) : 22
- adresse : ip du robot ou `pepper1.local`, `pepper2.local`, ...


Pour lancez le code, connectez-vous au robot en ssh, allez dans le dossier choisi dans `/home/nao/.local/share/PackageManager/apps/` , puis tapez `python nom_de_votre_appli.py`