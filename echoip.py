from sys import argv
from flask import Flask, request
app = Flask(__name__)


@app.route("/ip/")
def index():
    return get_ip()


def get_ip():
    """ This function returns the ip address of the client"""
    return request.environ['HTTP_REMOTE_ADDR'] 

if __name__ == "__main__":
    if 'production' in argv:
        ip = '127.0.0.1'
        port = 8080
    else:
        ip = '0.0.0.0'
        port = 80
    app.run(host=ip, port = port, debug = False)

