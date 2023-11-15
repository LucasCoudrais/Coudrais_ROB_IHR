
pepper proposes a webserver which is used to display data on tablet.
The tablet is just use a web navigator.
So the html content has to be located on a special special location
you have to give the  name you want  to the directory project but next you  need a html subdirectory inside.
So here we create the directories during the scp transfer
scp -r essai_script_multimedia nao@"adresseIPduPepper":/home/nao/.local/share/PackageManager/apps/

You can start the app from a ssh on pepper
:~$ ssh nao@"adresseIPduPepper" 
pepperX [0] ~ $ cd /home/nao/.local/share/PackageManager/apps/essai_script_multimedia
pepperX [0] ~/.local/share/PackageManager/apps/essai_script_multimedia $ python app.py

or from a PC where  pynaoqi (2.5.x) is installed
python app.py --ip ""adresseIPduPepper" 
(BUT : the project (html, topfiles and sounds directories)  have to be previously transfered on the pepper)
																																																																																																																																																																	


