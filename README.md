# echoip
Python web server that echos your ip.
A Flask app that echos your ip. 
Nginx is needed with the configuration file inside the repository.
Install the requirement with pip : pip install -r requirements
Run gunicorn : gunicorn -w 4 -b 127.0.0.1:8080 ecoip:app
