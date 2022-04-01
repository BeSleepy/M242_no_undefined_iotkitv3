# M242_no_undefined_iotkitv3
LB2 für Modul 242 - Mikroprozessoranwendung realisieren

![image](https://user-images.githubusercontent.com/71868338/160274076-19859925-7934-4f7c-a2a2-e540c0cfce0a.png)
Dieses Projekt besteht aus drei folgende Elementen
- IotKit
- Cloud API (Backend)
- Frontend CLI

Das IotKit hat die Funktion, anhand der Sensoren, die Temperatur und die Feuchtigkeit zu lesen. Ebenfalls wurde der Kartenleser implementiert. Somit kann das IotKit
die UID einer Karte lesen. Die Idee ist, dass jedes Mal wenn die eine Karte gescannt wird, werden die Daten an der Cloud API gesendet (UID, Temperatur und Feuchtigkeit).

Die Cloud API hat die Funktion,den Input vom Frontend zu Validieren und die erhaltenen Daten vom IotKit ans Frontend weiter zu leiten.

Der Frontend soll dem User ermöglichen sich einzuloggen. Sind die Angaben richtig, wird der User die Daten, die vom IotKit gesendet wurde sehen.

## Anleitung
### IotKit
Als Basis Projekt wurde das http Repo verwendet : https://github.com/iotkitv3/http

#### Libraries hinzufügen
Anschliessen werden die zusätzlichen Libraries zum Projekt hinzugefügt
- Für die Temperatur und Feuchtigkeit Sensoren: https://os.mbed.com/teams/ST/code/HTS221/
- Für den Kartenleser: https://github.com/iotkitv3/MFRC522.git

Um eine Library zum Projekt hinzuzufügen muss man zum Library Tap (unten bei der Console) > Pluszeichen siehe Bild und anschliessend den Library Link hinzufügen.
![image](https://user-images.githubusercontent.com/71868338/160281285-539ccc84-e6c6-42f0-83ad-53420579c6c8.png)

#### Main.cpp Anpassen
Zu Beginn gemäss der http Repo geklonte Files wird ein http Get Request gesendet und die Daten werden auf dem OLED des IotKit dargestellt. In diesem Projekt möchte man jedoch ein Http Post Request an dem Cloud Api senden. So sollte es angepasst werden. Siehe Bild
![image](https://user-images.githubusercontent.com/71868338/161235942-21260681-8606-4660-8bb2-a6e62ef8f78a.png)

Siehe das End Produkt -> [Main.cpp](https://github.com/BeSleepy/M242_no_undefined_iotkitv3/blob/main/Iotkitv3/http/main.cpp)


### (Cloud) Backend Applikation
Wir haben uns entscheiden eine eigene Backend Applikation zu schreiben. Der Source Code dazu findet man in diesem Repo unter Cloud: [Cloud](https://github.com/BeSleepy/M242_no_undefined_iotkitv3/tree/main/Cloud)

Microsoft Azure wird verwendet um die um die Backend Applikation zu Hosten. Mit Azure Student welches man mit der TBZ Email hat kann man sich einen Account mit 100 CHF erstellen. Damit können diese Dienste gratis verwendet werden.

Konkret wird ein App Service und ein Azure Database for MySQL-Einzelserver verwendet. 
Um diese Dienste aufzusetzen folgen sie diesen Tutorials:
- App Service mit Flask Applikation als Beispiel: [App Service](https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-portal%2Cterminal-bash%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cdeploy-instructions-zip-azcli)
- Azure Database for MySQL-Einzelserver: [MySQL-Einzelserver](https://docs.microsoft.com/en-us/azure/mysql/quickstart-create-mysql-server-database-using-azure-portal)

Unsere Backend Applikation wird anschliessend (wie im Tutorial erklärt) auf den App Service installiert.
Wir verwenden Flask mit SQLAlchemy, dies erlaubt uns die DB via Flask zu erstellen.
Nach der installation des Backend Codes auf den App Service öffnet man "app_service_url/create_db". Dieser Aufruf erstellt die gesamte Datanbank mit einem default User welcher unsere Karte verwendet.

Nun stehen drei Rest Endpoints zu verfügung:
##### "app_service_url"/api/iotkit
Dieser Endpoint sollte vom iotkit mittels einer POST Request aufgerufen werden um das Login zu Authentifizieren und Sensordaten mitzuteilen.
Um den Code auf dem iotkit einfach zu halten erwartet der Endpoint einen Body in plain/text mit folgendem Inhalt:\
```{"temperature": "x", "humidity": "y", "UID": "z"}```

##### "app_service_url"/login
Dieser Endpoint wird von der Frontend Applikation mittels einer POST Request aufgerufen um das Login eines Users zu Authentifizieren.
Dabei wird geprüft ob der letzte Kartenscann mit der UID des Users weniger als einer Minute her ist.
Der Endpoint erwartet einen Body im Format application/json mit folgendem Inhalt:\
```
{
  "username": ...,
  "password": ...
}
```
##### "app_service_url"/api/get_sensors
Dieser Endpoint wird von der Frontend Applikation mittels einer GET Request aufgerufen um die neusten Sensordaten zu bekommen.
Dabei erfolgt eine Authentifiziereung mit HTTP-Authentifizierung.
Der Endpoint gibt einen JSON mit der Temperatur und der Feuchtigkeit zurück.

#### HTTPS
Um HTTPS auf der Cloud zu verwenden müsste man beim starten der Applikation noch folgenden Parameter hinzufügen: ssl_context='adhoc'

### Frontend (CLI)
Das Frontend ist eine Python CLI. Der Source Code befindet sich hier: [CLI](https://github.com/BeSleepy/M242_no_undefined_iotkitv3/tree/main/CLI)\
Für die Ausführung ist vorausgesetzt, dass Python 3.8 installiert ist und die Backend Applikation erfolgreich auf Azure deployt wurde.

Die Python Library "requests" wird verwendet um mit der Backend Applikation über HTTP zu kommunizieren.\
```pip install requests```

Ausgefürt wird das Programm mit:\
```python3 main.py```
