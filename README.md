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
Um HTTPS auf der Cloud zu verwenden müsste man beim starten der Applikation den Zertifikat mitgeben.

##### IotKit
Beim IotKit ein Zertifikat muss vorhanden sein, damit es beim HTTPS Request mit geschickt werden kann.\
Referenz: [HTTPS-TUTORIAL](https://os.mbed.com/teams/sandbox/code/http-example/file/4b847971db1b/source/main-https.cpp/)


```
#include "https_request.h"
```

Zertifikat Beispiel:
```
const char SSL_CA_PEM[] =  "-----BEGIN CERTIFICATE-----\n"
    "MIIDQTCCAimgAwIBAgITBmyfz5m/jAo54vB4ikPmljZbyjANBgkqhkiG9w0BAQsF\n"
    "ADA5MQswCQYDVQQGEwJVUzEPMA0GA1UEChMGQW1hem9uMRkwFwYDVQQDExBBbWF6\n"
    "b24gUm9vdCBDQSAxMB4XDTE1MDUyNjAwMDAwMFoXDTM4MDExNzAwMDAwMFowOTEL\n"
    "MAkGA1UEBhMCVVMxDzANBgNVBAoTBkFtYXpvbjEZMBcGA1UEAxMQQW1hem9uIFJv\n"
    "b3QgQ0EgMTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALJ4gHHKeNXj\n"
    "ca9HgFB0fW7Y14h29Jlo91ghYPl0hAEvrAIthtOgQ3pOsqTQNroBvo3bSMgHFzZM\n"
    "9O6II8c+6zf1tRn4SWiw3te5djgdYZ6k/oI2peVKVuRF4fn9tBb6dNqcmzU5L/qw\n"
    "IFAGbHrQgLKm+a/sRxmPUDgH3KKHOVj4utWp+UhnMJbulHheb4mjUcAwhmahRWa6\n"
    "VOujw5H5SNz/0egwLX0tdHA114gk957EWW67c4cX8jJGKLhD+rcdqsq08p8kDi1L\n"
    "93FcXmn/6pUCyziKrlA4b9v7LWIbxcceVOF34GfID5yHI9Y/QCB/IIDEgEw+OyQm\n"
    "jgSubJrIqg0CAwEAAaNCMEAwDwYDVR0TAQH/BAUwAwEB/zAOBgNVHQ8BAf8EBAMC\n"
    "AYYwHQYDVR0OBBYEFIQYzIU07LwMlJQuCFmcx7IQTgoIMA0GCSqGSIb3DQEBCwUA\n"
    "A4IBAQCY8jdaQZChGsV2USggNiMOruYou6r4lK5IpDB/G/wkjUu0yKGX9rbxenDI\n"
    "U5PMCCjjmCXPI6T53iHTfIUJrU6adTrCC2qJeHZERxhlbI1Bjjt/msv0tadQ1wUs\n"
    "N+gDS63pYaACbvXy8MWy7Vu33PqUXHeeE6V/Uq2V8viTO96LXFvKWlJbYK8U90vv\n"
    "o/ufQJVtMVT8QtPHRh8jrdkPSHCa2XV4cdFyQzR1bldZwgJcJmApzyMZFo6IQ6XU\n"
    "5MsI+yMRQ+hDKXJioaldXgjUkK642M4UwtBV8ob2xJNDd2ZhwLnoQdeXeGADbkpy\n"
    "rqXRfboQnoZsG4q5WTP468SQvvG5\n"
    "-----END CERTIFICATE-----\n"
    "-----BEGIN CERTIFICATE-----\n"
    "MIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/\n"
    "MSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\n"
    "DkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow\n"
    "SjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT\n"
    "GkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC\n"
    "AQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF\n"
    "q6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8\n"
    "SMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0\n"
    "Z8h/pZq4UmEUEz9l6YKHy9v6Dlb2honzhT+Xhq+w3Brvaw2VFn3EK6BlspkENnWA\n"
    "a6xK8xuQSXgvopZPKiAlKQTGdMDQMc2PMTiVFrqoM7hD8bEfwzB/onkxEz0tNvjj\n"
    "/PIzark5McWvxI0NHWQWM6r6hCm21AvA2H3DkwIDAQABo4IBfTCCAXkwEgYDVR0T\n"
    "AQH/BAgwBgEB/wIBADAOBgNVHQ8BAf8EBAMCAYYwfwYIKwYBBQUHAQEEczBxMDIG\n"
    "CCsGAQUFBzABhiZodHRwOi8vaXNyZy50cnVzdGlkLm9jc3AuaWRlbnRydXN0LmNv\n"
    "bTA7BggrBgEFBQcwAoYvaHR0cDovL2FwcHMuaWRlbnRydXN0LmNvbS9yb290cy9k\n"
    "c3Ryb290Y2F4My5wN2MwHwYDVR0jBBgwFoAUxKexpHsscfrb4UuQdf/EFWCFiRAw\n"
    "VAYDVR0gBE0wSzAIBgZngQwBAgEwPwYLKwYBBAGC3xMBAQEwMDAuBggrBgEFBQcC\n"
    "ARYiaHR0cDovL2Nwcy5yb290LXgxLmxldHNlbmNyeXB0Lm9yZzA8BgNVHR8ENTAz\n"
    "MDGgL6AthitodHRwOi8vY3JsLmlkZW50cnVzdC5jb20vRFNUUk9PVENBWDNDUkwu\n"
    "Y3JsMB0GA1UdDgQWBBSoSmpjBH3duubRObemRWXv86jsoTANBgkqhkiG9w0BAQsF\n"
    "AAOCAQEA3TPXEfNjWDjdGBX7CVW+dla5cEilaUcne8IkCJLxWh9KEik3JHRRHGJo\n"
    "uM2VcGfl96S8TihRzZvoroed6ti6WqEBmtzw3Wodatg+VyOeph4EYpr/1wXKtx8/\n"
    "wApIvJSwtmVi4MFU5aMqrSDE6ea73Mj2tcMyo5jMd6jmeWUHK8so/joWUoHOUgwu\n"
    "X4Po1QYz+3dszkDqMp4fklxBwXRsW10KXzPMTZ+sOPAveyxindmjkW8lGy+QsRlG\n"
    "PfZ+G6Z6h7mjem0Y+iWlkYcV4PIWL1iwBi8saCbGS5jN2p8M+X+Q7UNKEkROb3N6\n"
    "KOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==\n"
    "-----END CERTIFICATE-----\n";
```
HTTP Request --> HTTPS Request
```
HttpsRequest* post_req = new HttpsRequest(network, SSL_CA_PEM, HTTP_POST, "https://httpbin.org/post");
```

##### (Cloud) Backend Applikation

```
context = ('local.crt', 'local.key')#certificate and key files
app.run(ssl_context=context)
```

### Frontend (CLI)
Das Frontend ist eine Python CLI. Der Source Code befindet sich hier: [CLI](https://github.com/BeSleepy/M242_no_undefined_iotkitv3/tree/main/CLI)\
Für die Ausführung ist vorausgesetzt, dass Python 3.8 installiert ist und die Backend Applikation erfolgreich auf Azure deployt wurde.

Die Python Library "requests" wird verwendet um mit der Backend Applikation über HTTP zu kommunizieren.\
```pip install requests```

Ausgefürt wird das Programm mit:\
```python3 main.py```

---
# LB3 für Modul 242 - Mikroprozessoranwendung realisieren
Für die LB3 benutzen wir das bestende Programm der LB2 jedoch wird sie erweitert.

## Anleitung
### MQTT
Zu beginn klone die MQTT Repository : https://github.com/iotkitv3/mqtt.git
anschliessend füge die Logik vom bestehenden Programm hinzu und wiederhole die Anleitung der LB2. In anderen Worten die Libraries wieder importieren.

#### MQTT konfiguration
Damit man etwas publishen kann, muss ein Topic erstellt werden.
```
char* topicAuthentification = (char*) "m242_lb03_albisetti_harlacher/iotkit";
```
Anschliessend muss der Broker bzw. den Host konfiguriert werden.
```
char* hostname = (char*) "cloud.tbz.ch";
```

Damit wir keinen leeren String bzw. Message publishen muss noch die Message aktualisiert werden und anschliessend beim Topic senden.
```
sprintf( buf, "%s,%f,%f", card_id.c_str(), temperature, humidity); 
publish( mqttNetwork, client, topicAuthentification );    
```

Siehe genaue Details : [Main.cpp](https://github.com/BeSleepy/M242_no_undefined_iotkitv3/blob/main/Iotkitv3/mqtt/main.cpp)
