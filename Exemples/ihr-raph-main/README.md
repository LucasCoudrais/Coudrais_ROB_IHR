# Mini projet

## Mettre en place deux scenarios :

- Un scénario doit montrer un comportement éthique , l'autre non (il peut aussi s'agir idéalement de deux variantes du même scénario)

- Utiliser la tablette 

- Utiliser le module dialogue/qichat

- Mettre en place un service (au sens naoqi) et l'interfacer avec le dialogue

- Faire un lien avec un webservice sur internet ou développer son propre webservice.


## Rendu et evaluation:

  - La note est donnée en fonction du respect des consignes, du travail fourni et de l'originalité des réalisations. Les 3 axes a satisfaire sont :
    - La composante éthique
    - La qualité de l'interaction
    - La qualité technique

  - Un bonus est donné si minimisation de l'usage de choregraphe.

  - Votre production sera accompagnée des éléments décrits dans le point ci-dessous (story board, video, ...)

  - Rendu sur GitLab (repo privé, donnez le droit maintener à votre enseignant):
    - Projet complet et fonctionnel
    - Readme d'explication avec les éléments suivants :
      - Description du/des cas éthique(s) mis en oeuvre
      - Au moins 3 références bibliographiques des cas éthiques traités (doc, page, chapitre, ref si existante) d'au moins 2 documents différents
      - Story Board
      - Lien vers vidéo youtube
      - Instructions de mise en route
      - Instructions d'usage
    - Fichier excel évaluation des risques 


## Doc.
  - [Syntaxe des dialogues (fichier *.top) avec le module qichat](http://doc.aldebaran.com/2-1/naoqi/audio/dialog/dialog-syntax_full.html)
  - Comportements prédéfinis
    - [alanimatedspeech-api](http://doc.aldebaran.com/2-1/naoqi/audio/alanimatedspeech-api.html)
    - [liste des comportements disponibles](http://doc.aldebaran.com/2-1/naoqi/audio/alanimatedspeech_advanced.html)

## [Exemples](examples/README.md)

## Tips

### SSH
- Pour se connecter en ssh au pepper1 (par exemple), tapez dans un terminal `ssh nao@pepper1.local` puis le mot de passe de la majeure...
- Pour transférer des fichiers, utilisez `scp` (ligne de commande), ou `FileZilla` (outil graphique)

### Tablette

#### Internet 
Le code python/choregraphe est executé sur un PC embarqué. Le html/javascript est executé sur la tablette. Si vous voulez GET des données depuis la tablette, il faut aussi la connecter à internet. Pour cela, connectez vous en SSH au robot, executez la commande `qicli call ALTabletService._openSettings` et regardez la tablette du Pepper pour la suite de la procédure de connection à internet.  




