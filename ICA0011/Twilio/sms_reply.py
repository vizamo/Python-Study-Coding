import os
import subprocess

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome'


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """
    Way to do it without password: command sudo visudo, 
    add line "myuser ALL=(ALL) NOPASSWD: /etc/init.d/apache2"
    After that is possible to start server with command "sudo systemctl start apache2"
    """
    resp = MessagingResponse()
    sms = request.values.get('Body', None)
    if sms == "service apache2.start":
        os.system("/etc/init.d/apache2 start")
        resp.message("Service is restarted")
    else:
        resp.message("Unknown command")
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
