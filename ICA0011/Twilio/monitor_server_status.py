import requests
import time
import os
from twilio.rest import Client
server_url = "http://localhost"


def send_twilio_notification(site, status_code):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
                body=f"The Web Server ({site}) is down ({status_code})",
                from_='+16309312303',
                to='+xxx'
                )
    print(message.sid)


def check_server_status():
    time_now = str(time.ctime())
    try:
        r = requests.request("GET", url=server_url)
        if r.status_code == 200:
            print(time_now + " Server is working")
        else:
            print(time_now + " Server is down")
            send_twilio_notification(server_url, r.status_code)
    except:
        print(time_now + " Server is down")
        send_twilio_notification(server_url, 502)
    time.sleep(1800)  # 30min = 1800sec
    check_server_status()


check_server_status()
