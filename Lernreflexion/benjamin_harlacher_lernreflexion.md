# Lernreflexion Benjamin Harlacher

## Arbeitstage
---
### Tag 2 (04.03.2022)
#### Aktivität
Ich habe mit meinem Projektpartner Ideen gesucht, was wir machen könnten. Anschliessend habe ich mich mit dem IoTkit beschäftig und einige Beispiel Programme angeschaut und ein wenig experimentiert.

#### Reflexion
Da ich in diesem Modul das erste Mal mit C++ schaffe, war es für mich nicht so einfach etwas drauf los zu programmieren z.B. um einen String in CommandLine zu schreiben, musste ich die flags kennen das %s für String ist oder %f für float etc. Ich hatte zwar im ersten Lehrjahr ein Modul mit C gehabt, konnte dadurch Ähnlichkeiten finden, jedoch war das schon lange her, so wurde einiges wieder aufgefrischt. An diesem Tag war mein Arbeitspartner krank und hat teilweise im Home-Office gearbeitet, was jedoch nicht ganz optimal für die Zusammenarbeit war aber wir konnten einen Fortschritt machen für das Projekt.

---

### Tag 3 (11.03.2022)
#### Aktivität
Ich habe heute richtig mit dem LB2 angefangen bezogen auf das IoTkit. Habe das http Programm als Basis verwendet und die Library von dem Kartenleser hinzugefügt und die Logik des Programmes angepasst gemäss der Projekt Idee. Heute wurde ebenfalls das Repo für das Projekt erstellt.
#### Reflexion 
Ich habe heute gelernt wie man Libraries in Mbed Studio hinzufügt. Das Hinzufügen war relativ einfach, jedoch als ich weiter arbeiten wollte. Gab es einen Error, die das Projekt zum Abstürzen bringt. Der explizite Grund haben ich, mein Partner und sowohl der Lehrer nicht gefunden, jedoch fanden wir heraus das man die "myled" Variable aus kommentieren musste, ansonsten stürtzt das Programm bei rfidReader.PCD_Init(); ab. Als ich das mbed Projekt ins Repo schieben wollte und pushen gab es ein Error. Das mbed Projekt wurde ja geklont in anderen Worten ebenfalls ein Repository. Wenn ich im Parent Repo pushe, werden die Änderungen im Child Repo nicht gepusht.
Um das Problem zu lösen, müsste man das Child Repo als submodule hinzufügen. Später realisierte ich das ich im Child Repo gar nicht pushen kann, da es ja nicht mein Projekt ist und dem entsprechend auch keine Berechtigung habe. Das Problem wurde noch nicht gelöst, wird aber im späteren Zeitpunkt wieder aufgegriffen.

---

### Tag 4 (18.03.2022)
#### Aktivität
Ich habe heute ein weiteres Library hinzugefügt nämlich die für die Temperatur und Feuchtigkeit Sensoren. Habe ebenfalls den Http Request angepasst. Zu beginn war es ein get Request an einer API. Jetzt ist es ein Habe anschliessend die Logik des Programmes angepasst.
#### Reflexion
Heute war mein Arbeitspartner abwesend was für die Zusammenarbeit nicht so optimal war, jedoch habe ich die nötigen Information, die ich brauche am Vortag bekommen.
Ich hatte ein Error den ich noch nicht lesen konnte, nämlich: Die UID einer Karte wird durch eine Iteration gelesen und auf dem OLED dargestellt. Ich möchte jedoch das es in einem String gespeichert wird und anschliessend anhand der Http Request, die Daten gesendet werden. Das Problem liegt daran von UID.Byte zu einem String umzuwandeln.

---
### Tag 5 (25.03.2022)
#### Aktivität
Zu beginn der Lektion habe ich mich mit dem Repo Prolem fokussiert. Anschliessend versuchte ich weiter mit dem UID Problem.
#### Reflexion
Zur Repo Problem, wurde als Lösung den Inhalt des Child Repo kopiert und in ein eigenes directory hinzugefügt. Für das UID Problem wurde nicht ganz sauber gelöst aber eine erste Lösung ist jetzt vorhanden. Das Program lauft. Ich konnte jedoch noch nicht die Verbindung mit dem Backend testen, da unser Backend noch nicht bereit war.
Es wurde mithilfe dieser Funktion gelöst:
```
std::to_string(variable)
```
---

### Sontag (27.03.2022)
#### Aktivität
Ich habe heute mit meinem Partner die Verbindung zwischen dem IoTkit und dem Backend getestet. Ebenfalls habe ich mich heute für die Dokumentation beschäftigt.
#### Reflexion
Beim Testen der Verbindung stürzt das Program durch irgend ein Grund ab. Es kann sein das die Verbindung vom WLan vielleicht eine Rolle spielt. Plan wäre es nächsten Freitag nochmals zu testen. Habe weitere potentielle Fehler gesucht, habe jedoch keine Entdeckt.

---
## Thema
### IoT
Das Internet der Dinge (IdD) (englisch Internet of Things, Kurzform: IoT) ist ein Sammelbegriff für Technologien einer globalen Infrastruktur der Informationsgesellschaften, die es ermöglicht, physische und virtuelle Objekte miteinander zu vernetzen und sie durch Informations- und Kommunikationstechniken zusammenarbeiten zu lassen

Ziel des Internets der Dinge ist es, automatisch relevante Informationen aus der realen Welt zu erfassen, miteinander zu verknüpfen und im Netzwerk verfügbar zu machen. Dieser Informationsbedarf besteht, weil in der realen Welt Dinge einen bestimmten Zustand haben (z. B. „Luft ist kalt“, „Druckertoner ist voll“), dieser Zustand im Netzwerk jedoch nicht verfügbar ist. Ziel ist also, dass viele reale Dinge die eigenen Zustandsinformationen für die Weiterverarbeitung im Netzwerk zur Verfügung stellen.

---
### Sensoren
Sensoren sind technische Bauteile, die Eigenschaften der Umgebung (z. B.: Wärmestrahlung, Temperatur, Feuchtigkeit, Druck, Schall, Helligkeit oder Beschleunigung) erfassen und in ein weiter verarbeitbares elektrisches Signal umformen.

Beispiele:
- Hall Sensor

Ein Hall Sensor (auch Hall-Sonde oder Hall-Geber, nach Edwin Hall) nutzt den Hall-Effekt zur Messung von Magnetfeldern. Der auf dem IoTKit verwendetete Hall Sensor kann zur Lage Erfassung eines Permanentmagnetes genutzt werden, d.h. es kann der Nordpol oder Südpol des Magneten bestimmt werden.

Anwendungen
- Alarmanlagen, z.B. zum Sichern von Fenstern.
- Im Auto zur Kontrolle ob der Sicherheitsgurt geschlossen ist, als Raddrehzahlsensoren, zur Erkennung des Zündzeitpunkts.
- Zur Geschwindigkeitsmessung, z.B. für E-Bikes.
- In der Kraftwerkstechnik zur Erfassung der Turbinendrehzahl.

---
### Aktoren
Aktoren (Wandler; Antriebselemente) setzen die elektronischen Signale in mechanische Bewegung oder andere physikalische Grössen um und greifen damit aktiv in die Umgebung des eingebetteten Systems ein.

Beispiele:
- Dioden, 7-Segement-Anzeigen, Displays
- Ventile (Pneumatik, Hydraulik)
- Motoren (Gleichstrom/Wechselstrom)
- Magnete (Manipulatoren, Lautsprecher)

Anwendungen:
- In vielen Robotern kommen Standard Boards mit individuellen Shield's zum Einsatz.
- Der Siegeszug der DIY (Do-it-yourself) 3D Druckern, wäre ohne die Arduino Mega Boards nicht denkbar gewesen.
- LED Strips eröffnen neue Möglichkeiten für die Dekorative Beleuchtungen von Gegenständen und Räumen.

---
### Service
