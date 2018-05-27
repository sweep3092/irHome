import paho.mqtt.client as mqtt
import json
import subprocess
import os

_TOKEN = 'token_oywdao992b55LcMw'
HOSTNAME = 'api.beebotte.com'
PORT = 1883
TOPIC = 'ifttt_raspi/irSignal'

def on_connect(client, userdata, flags, respons_code):
    print('status {0}'.format(respons_code))
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(msg.topic + ' ' + str(msg.payload))
    data = json.loads(msg.payload.decode("utf-8"))["data"][0]
    data = {key:value.strip() for key, value in data.items()}
    if "room" in data.keys():
        subprocess.call(['sudo python2 load_and_play.py signals/{}.json'.format(data['device']), '-d', signal])

if __name__ == '__main__':
    client = mqtt.Client()
    client.username_pw_set("token:%s"%_TOKEN)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(HOSTNAME, port=PORT, keepalive=60)

    client.loop_forever()

