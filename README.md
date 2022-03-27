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
![image](https://user-images.githubusercontent.com/71868338/160281568-db27de60-493e-4a3b-aa84-a90735a63886.png)

Siehe das End Produkt -> [Main.cpp](https://github.com/BeSleepy/M242_no_undefined_iotkitv3/blob/main/Iotkitv3/http/main.cpp)


### Backend

### Frontend
