import json
import random
import time

from paho.mqtt import client as mqtt_client


broker = 'cloud.tbz.ch'
port = 1883
topic = "m242_lb03_albisetti_harlacher/iotkit"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set('', '')
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = {
            "temperature": 1,
            "humidity": 2,
            "UID": "148:130:73:26:"
        }
        result = client.publish(topic, json.dumps(msg))
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{json.dumps(msg)}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()