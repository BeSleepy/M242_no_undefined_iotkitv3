import json

import requests

URL = "https://m242cloud.azurewebsites.net"
LOGIN = "/login"
SENSOR = "/api/get_sensors"


def run():
    print('Please log in to your account to access your device')
    print('Username:')
    username = input()
    print('Password:')
    password = input()

    login(username, password)


def login(username, password):
    login_body = {
        "username": username,
        "password": password
    }
    login_response = requests.post(URL + LOGIN, json=login_body)
    decoded_response = login_response.content.decode('ascii')
    print(decoded_response)
    if decoded_response == "True":
        some_space()
        print("Logged in successfully")
        show_device(username, password)
    else:
        some_space()
        print("Logging failed. Scan your card again and enter your credentials again")
        run()


def show_device(username, password):
    print("Display device Sensors")
    get_sensor_data(username, password)
    show_options(username, password)


def get_sensor_data(username, password):
    try:
        response = requests.get(URL + SENSOR, auth=(username, password))
        response = response.content.decode('ascii')

        sensor = json.loads(response)

        print(f"Humidity is {sensor.get('humidity')}")
        print(f"Temperature is {sensor.get('temperature')}")

    except Exception as e:
        print('Failed to get Sensors:' + str(e))
        return


def show_options(username, password):
    print("Logout (l) or show device sensors again (s)")
    choice = input()
    if choice.lower() == "l":
        some_space()
        run()
    if choice.lower() == "s":
        some_space()
        show_device(username, password)
    else:
        print("Please only enter l or s")
        show_options(username, password)


def some_space():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


if __name__ == '__main__':
    print('Application starting')
    run()

