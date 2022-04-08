from cgi import test
import hashlib
import datetime
import json

from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth
from time import time
from flask_mqtt import Mqtt

from db import db
from models.user import User
from models.device import Device


app = Flask(__name__)
auth = HTTPBasicAuth()
CORS(app)

username = 'undefined@m242-db-undefined'
password = 'cipw3kdiS9mbj5v'
server = 'm242-db-undefined.mysql.database.azure.com'
db_name = 'm242_no_undefined_iotkit'
port = '3306'
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{username}:{password}@{server}:{port}/{db_name}"
app.config['SCHEDULER_API_ENABLED'] = True
db.init_app(app)


app.config['MQTT_BROKER_URL'] = 'cloud.tbz.ch'  # use the free broker from HIVEMQ
app.config['MQTT_BROKER_PORT'] = 1883  # default port for non-tls connection
app.config['MQTT_USERNAME'] = ''  # set the username here if you need authentication for the broker
app.config['MQTT_PASSWORD'] = ''  # set the password here if the broker demands authentication
app.config['MQTT_KEEPALIVE'] = 15  # set the time interval for sending a ping to the broker to 5 seconds
app.config['MQTT_TLS_ENABLED'] = False  # set TLS to disabled for testing purposes

mqtt = Mqtt()

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('m242_lb03_albisetti_harlacher/iotkit')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    payload=message.payload.decode()

    try:
        json_body = json.loads(payload)
    except Exception as e:
        print('Failed to load body as json: ' + str(e))
        return

    if json_body.get('UID') and json_body.get('temperature') and json_body.get('humidity'):
        print("Try to load user by UID")
        try:
            user = User.query.filter_by(card_uid=json_body.get('UID')).first()
        except Exception as e:
            print(f"Faild to load user with UID {json_body.get('UID')} cause " + str(e))
            return

        print("Try to load device based on user")
        try:
            device = Device.query.filter(Device.fk_user == user.id_user).first()
        except Exception as e:
            print(f"Faild to load device with UID {json_body.get('UID')} cause " + str(e))
            return

        sensor_data = {
            "temperature": json_body.get('temperature'),
            "humidity": json_body.get('humidity')
        }

        print('Set last card scan to current timestamp in seconds')
        device.last_card_scan = str(time())
        device.sensor_data = json.dumps(sensor_data)
        db.session.commit()
        print("Last card scan updated!")
        
    else:
        print("Body does not contain all required parameters")


@app.route('/create_db')
def create_db():
    db.create_all()

    username = "test"
    pw = "test"
    card_id = "148:130:73:26:"

    new_user = User(username, hashlib.sha256(pw.encode('utf-8')).hexdigest(), card_id)
    db.session.add(new_user)  # Add user to DB

    db.session.commit()

    user = User.query.filter_by(username=username).first()

    last_card_scan = "0"
    sensor_data = "None"
    fk_user = user.id_user

    new_todo = Device(last_card_scan=last_card_scan, sensor_data=sensor_data, fk_user=fk_user)
    db.session.add(new_todo)

    db.session.commit()

    return "DB initialization finished"


@app.route("/login", methods=["POST"])
def login():
    """
        body of POST request:
        {
            username
            password
        }
        :return:
    """
    body = request.json  # depending on input from php my be request.json
    if body.get('username') and body.get('password'):
        user = User.query.filter_by(username=body.get('username')).first()
        if not user:
            return "False"
        hashed_password = hashlib.sha256(body['password'].encode('utf-8')).hexdigest()
        if not hashed_password == user.password:
            return "False"

        device = Device.query.filter(Device.fk_user == user.id_user).first()
        last_card_scan = device.last_card_scan
        current_time = time()

        if float(last_card_scan) + 60 >= current_time:
            return "True"
        else:
            return "False"

    else:
        return "False"


@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if not user:
        return False
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    if not hashed_password == user.password:
        return False
    return True


@app.route("/api/get_sensors", methods=["GET"])
@auth.login_required
def get_sensors():
    """
    sensor_data from device for current user
    :return:
    """
    auth_header = request.authorization
    user = User.query.filter_by(username=auth_header.username).first()

    device = Device.query.filter(Device.fk_user == user.id_user).first()
    sensor = device.sensor_data

    print("load sensor data json")
    try:
        sensor = json.loads(sensor)
    except Exception as e:
        print('Failed to load sensor data json:' + str(e))

    print(str(sensor))
    return jsonify(sensor)


@app.route("/api/iotkit", methods=["POST"])
def iotkit():
    """
    HTTP Request from iotkit with sensor_data and card_id in body
    body of POST request:
    "{"temperature": %f "humidity": %f "UID": %s}"

    get user based on card_uid
    get device with same user.id
    set last_card_scan to current timestamp
    """
    print("-------------------------------------------- iotkit post incomming --------------------------------------------")
    body = request.get_data()  # may be request.json
    body = body.decode('ascii')
    print('this is body of iotkit request: ' + body)
    print("try to load body to json")
    try:
        json_body = json.loads(body)
    except Exception as e:
        print('Failed to load body as json: ' + str(e))
        return 'Failed to load body as json'

    if json_body.get('UID') and json_body.get('temperature') and json_body.get('humidity'):
        print("Try to load user by UID")
        try:
            user = User.query.filter_by(card_uid=json_body.get('UID')).first()
        except Exception as e:
            print(f"Faild to load user with UID {json_body.get('UID')} cause " + str(e))
            return "Unknown UID"

        print("Try to load device based on user")
        try:
            device = Device.query.filter(Device.fk_user == user.id_user).first()
        except Exception as e:
            print(f"Faild to load device with UID {json_body.get('UID')} cause " + str(e))
            return f"Device not found from user with uid {json_body.get('UID')}"

        sensor_data = {
            "temperature": json_body.get('temperature'),
            "humidity": json_body.get('humidity')
        }

        print('Set last card scan to current timestamp in seconds')
        device.last_card_scan = str(time())
        device.sensor_data = json.dumps(sensor_data)
        db.session.commit()
        return "Last card scan updated!"
        
    else:
        print("Body does not contain all required parameters")
        return "Body does not contain all required parameters"


if __name__ == '__main__':
    app.run()
