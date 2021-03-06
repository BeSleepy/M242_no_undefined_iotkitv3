# Lernreflexion Paul Albisetti

## Arbeitstage
### Tag 2 (04.03.2022)
#### Aktivität
Da ich Krank war habe ich so gut es geht aus dem Home Office gemeinsam mit Benjamin Ideen für das Projekt gesucht. Anschliessend habe ich mich mit AWS und Azure beschäftigt und versucht herauszufinden wie wir unsere Backend Applikation aufsetzen können.

#### Reflexion
Ich hatte bisher noch keine Berührungspunkte mit irgendwelcher Cloud Applikationen und somit war alles für mich Neuland. Es hat desswegen eine Weile gebraucht biss ich überhaupt verstanden habe was wir für unsere Applikation brauchen und wie ich so etwas Ausetzen kann.\ Trotz meiner Abwesenheit hat die Kommunikation im Team aber einigermassen gut Funktioniert und wir haben erfolgreich eine Projektidee gefunden.

### Tag 3 (11.03.2022)
#### Aktivität
Heute hat die Umsetzung von LB02 richtig gestartet. Ich habe mich wider hauptsächlich mit der Cloud befasst. Hauptziel war das Ausetzen einer Datenbank welche vom App Service verwendet werden kann. Ebenfalls habe ich mit Benjamin einige Stunden damit verbracht einen Fehler im http Programm in Verbindung mit dem rfid Programm zu finden.

#### Reflexion
Hardware kann sehr nervig sein. Der Fehler in http und rfid programm war die verwendung eines LED welcher eigentlich nichts mit irgendetwas zu tun haben soll... Ebenfalls ist eine Datenbankinstanz auf Azure erstaundlich teuer.\
Die Kommunikation und Zusammenarbeit war heute deutlich einfacher da wir beide vor Ort waren. Wir sind vor allem auf dem Iotkit deulich weitergekommen.

### Tag 4 (18.03.2022)
#### Aktivität
Abwesend

### Tag 5 (25.03.2022)
#### Aktivität
Ich habe eine Flask API geschrieben und die Datenbank aufgesetzt. Den Code wurde im Anschluss auch auf den App Service deployt, jedoch hat noch nichts alles funktioniert. Grund dafür war die Sicherheitseinstellungen auf der Datenbank. 
#### Reflexion
Ich habe gelernt wie man mit Flask eine REST API in Python schreibt. Ebenfalls habe ich gelernt wie man auf Azure Sicherheitsregeln umgeht für den Zugriff auf die Datanbank. Dies ist zwar überhaupt nicht empfolen jedoch fehlt mir momentan das Wissen die Datenbank und den Zugriff korrekt zu konfigurieren. C++ stellte sich auch sehr mühsam hereaus weil das herauslesen der UID in eine Variable deutlich komplzierter war als gedacht.\
Die Zusammenarbeit hat sehr gut funktioniert. Wir sind heute sehr gut weitergekommen mit unseren Arbeiten.

### Wochenende (26.03.2022/27.03.2022)
#### Aktivität
Ich habe über das Wochenende den Bug in der Flask API gesucht und mit Python eine CLI geschrieben um ein Frontend zu simulieren. Ebenfalls habe ich die Dokumentation zur Cloud und dem Frontend (CLI) geschrieben.
#### Reflexion
Ich habe gelernt wie man text/plain im Body einer Request verwendet. Ursprünglich war die Idee den Body im JSON Format zu haben, dies wurde zur Erleichterung der Logik auf dem Iotkit zu einem JSON als String geänderd. Dies hat in meinen Tests zu einem Fehler geführt da ich denn JSON String im Body mit '' eingeschlossen habe (body = "'{...}'"). Dies führete in der API zu einem Fehler weil das JSON Format im String nicht erkannt wurde. Ebenfalls habe ich das praktische Logging durch die prints im Azure App Service gefunde. Eine CLI mit Python eine sehr schnelle und praktische alternative. Damit habe ich gesehen wie unser Frontend funktionieren müsste und was wir für LB03 alles ändern müssen. Ebenfalls habe ich gelernt wie ich HTTPS implementieren müsste in der Cloud. Das Effektive testen der ganzen Applikation hat noch nicht Funktioniert weil das Iotkit Probleme mit der Internetverbindung hatte.\
Die Backend Applikation, die Datenbanke und die CLI sind fertig und funktionieren zusammen. Die Umsetzung der LB02 ist somit fertig.

### Tag 6 (01.04.2022/Abgabe LB2)
#### Aktivität
Letzte Verbindungsfehler Lösen. Abgabe von LB02. Wir haben HTTPS nicht 100%ig verstanden, nach erklärung konnten wir dies noch in der Doku hinzufügen.
#### Reflexion
Wir haben die Url mit HTTPS statt HTTP auf dem IoTKit definiert. Da das IoTKit kein HTTPS kann funktionierte das natürlicherweise nicht, ein nerviger kleinen Flüchtigkeitsfehler. Unser Wissen über HTTPS war auch nicht bessonders vorhanden. Nächstes mal ein bisschen besser einlesen.

### Tag 7 (08.04.2022)
#### Aktivität
Ich habe eine Library gesucht und gefunden welche für Flask die mqtt Library von Python implementiert. Im Anschluss habe ich Versucht die Library in unserem Code einzubauen.
#### Reflexion
Die API läuft, jedoch bekomme ich keine Daten vom Frontend. Wo das Problem liegt ist noch unklar. Ich muss die API seperat testen um zu identifizieren wo der Fehler liegt.

### Tag 8 (06.05.2022)
#### Aktivität
Ich habe die API einzel getestet und das Problem identifiziert und gelöst. Ebenfalls habe ich begonnen das Frontend zu implementieren. Das deployen der API auf Azure hat wegen der Verwendung einer spezifischen Python Library nicht funktioniert.
#### Reflexion
Das Problem bei der API lag beim sogenanten App Context von Flask. Ich wusste nicht, dass so etwas existiert und hatte desswegen meine Probleme einen Workaround zu finden. Zusätzlich habe ich noch zwei spezifische Testscript (Publish and Subscribe) erstellt um diesen Teil der API mit mqtt zu testen. Das Deployment zu Azure funktionierte leider nicht. Die mqtt Library in Python verwendet eine weitere Library namens typing. Dies Library ist seit Python 3.7 als standard eingebaut und kann auf gewissen Systemen Probleme machen wenn man sie seperat nochmals installiert. Dies war bei mir auf dem Azure App Service der Fall und da ich kein direkter Zugriff hatte (da nach dem Deployment der App Service down geht) konnte ich typing auch nicht deinstalleiren. Ich bin mir sicher es gäbe einen Workaround, jedoch fehlt mir dazu das Wissen oder die richtige Person zum nachfragen. In Absprache mit der Lehrperson verwenden wir nun Node Red um auf einen Subscrieb von mqtt einen HTTP POST auf unsere API aus. Lokal aber funktiniert unser Backend mit mqtt ohne Node Red.

### Wochenende (07.05.2022/08.05.2022)
#### Aktivität
Ich habe das Frontend ersetllt. An der API mussten noch einige kleine Anpassungen durchgeführt werden.
#### Reflexion
Die Return Values von der API sind ein wenig Fragwürdig. Da ich nicht wusste wie ich besser mit HTTP Request in PHP umgehen kann habe ich es so gelassen. Für eine wirckliche Applikation müsste ich mich hier noch weiter erkunden, was der korrekte Weg wäre, Responsens zu senden und behandlen. Der Rest des Frontend war relativ simpel.

---

## Wichtiges zum Mitnehmen
- Azure (oder allgemein Cloud Diensete) sind sehr praktisch. Bieten möglichkeit eigene Applikation zu hosten und Verfügbar zu machen. Riesengross und sehr kompliziert, jedoch gut Dokumentiert: [Doku](https://docs.microsoft.com/en-us/azure/?product=popular).

## Themen
### MCU
Halbleiterchips die einen Prozessor und zugliech Arbeits- und Programmspeicher sowie Peripheriefunktionen enthalten. 
Peripheriefunktionen sind z.B. CAN-(Controller Area Network), I²C-(Inter-Integrated Circuit), SPI-(Serial Peripheral Interface), serielle Schnittstellen, PWMAusgänge, Analog-Digital-Umsetzer.
Tritt oft in eingebetteten Systemen unbemerk in Alltag ein (Auto, Heimanwendungen, Medizin, Büroanwendung).

### Bus System
System zur Datenübertragung zwischen mehreren Teilnehmern über eine gemeinsame Übertragungsweg.
Es gibt verschiedene Topologien von Bus Systemen:
- Point-to-Point, Direckte verbindung zwischen zwei Punkten. Beispiel: Serielle Schnittstelle
- Linien-Topologie. Beispiel: I2C
- Multiplexing, braucht einen Zusätzlichen Steuerpin, möchte nur die hälfte der Buspin's verwenden indem in einer Phase die eine Hälfte und in einer anderen Phase die andere Hälfte der Signale gesendet werden. Beispiel: SPI

### IoT
Internet of Things. Vereint die physiche Welt mit der Digitalen. Sensoren nehmen Dinge war, Aktoren wirken auf sie, alles vereint durch das Internet.
IIoT - Industrial Internet of Things
CIoT - Consumer Internet of Things



### GPIO
General Purpose Input/Output. Allzweckeingabe oder Allzweckausgabe ist ein Ping welcher durch Programmiereung entweder als In oder Output verwendet werden kann.
GPIO - Kanal ist eine Gruppe von zusammengefasten Pins. Sie werden oft mit Buchsteben bezeichnet.
Ein einzelner Pin kann meistens mit Buchstaben und Nummer aufgerufen werden (A3).
Arduino Bezeichner (A0-A5, D0-D15)

### Sensoren
Sensorene nehmen die Welt um sich herum auf. Beispiel sind:
- Temperatur
- Bewegung
- Helligkeit
- Kamera

Wichtig: Sie nehmen die Welt auf, und wirken NICHT auf sie (dies ist der Job von Aktoren).


### Aktoren
Aktoren wirken auf die Welt um sich. Beispielsweise mit:
- Motoren
- Audio
- Licht (LED)

Beispiele von Aktoren:
- Servo
- Elektromotor

### Mqtt
Offenes Nachrichtenportokoll für M2M. Basiert auf TCP-Sockets.
Implementiert Publish and Subscribe Pattern. Braucht dazu aber einen zentralen Server (Message Broker) um die beiden Seiten zu verbinden
