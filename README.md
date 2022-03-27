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

Anschliessen werden die 



### Backend

### Frontend
