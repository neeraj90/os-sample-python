from flask import Flask
from flask import send_from_directory
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World Neeraj!"

@application.route('/static/<path:path>')
def send_video(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    application.debug = True
    application.run()
