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
 
## Wichtiges zum Mitnehmen
- Azure (oder allgemein Cloud Diensete) sind sehr praktisch. Bieten möglichkeit eigene Applikation zu hosten und Verfügbar zu machen. Riesengross und sehr kompliziert, jedoch gut Dokumentiert: [Doku](https://docs.microsoft.com/en-us/azure/?product=popular).
