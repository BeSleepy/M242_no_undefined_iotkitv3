/** Beispiel Senden von Sensordaten an ThingSpeak
    */
#include "http_request.h"
#include "OLEDDisplay.h"
#include "MFRC522.h"
#include "mbed.h"
#include <cstdio>
#include <string>
#include <iostream>
#include <format>
//#include "json.hpp"

// for convenience
//using json = nlohmann::json;

#if MBED_CONF_IOTKIT_HTS221_SENSOR == true
#include "HTS221Sensor.h"
#endif
#if MBED_CONF_IOTKIT_BMP180_SENSOR == true
#include "BMP180Wrapper.h"
#endif



// UI
OLEDDisplay oled( MBED_CONF_IOTKIT_OLED_RST, MBED_CONF_IOTKIT_OLED_SDA, MBED_CONF_IOTKIT_OLED_SCL );

// NFC/RFID Reader (SPI)
MFRC522    rfidReader( MBED_CONF_IOTKIT_RFID_MOSI, MBED_CONF_IOTKIT_RFID_MISO, MBED_CONF_IOTKIT_RFID_SCLK, MBED_CONF_IOTKIT_RFID_SS, MBED_CONF_IOTKIT_RFID_RST ); 



static DevI2C devI2c( MBED_CONF_IOTKIT_I2C_SDA, MBED_CONF_IOTKIT_I2C_SCL );
#if MBED_CONF_IOTKIT_HTS221_SENSOR == true
static HTS221Sensor hum_temp(&devI2c);
#endif
#if MBED_CONF_IOTKIT_BMP180_SENSOR == true
static BMP180Wrapper hum_temp( &devI2c );
#endif

// ThingSpeak URL und API Key ggf. anpassen 
char host[] = "http://api.thingspeak.com/update";
char key[] = "A2ABBMDJYRAMA6JM";

// I/O Buffer
char message[1024];

//DigitalOut myled(MBED_CONF_IOTKIT_LED1);

int main()
{
    uint8_t id;
    float temperature, humidity;
    string card_id;

   

    printf("\tThingSpeak\n");
    rfidReader.PCD_Init();
    // Init all sensors with default params 
    hum_temp.init(NULL);
    hum_temp.enable();

    hum_temp.read_id(&id);
    printf("HTS221  humidity & temperature    = 0x%X\r\n", id);

    // Connect to the network with the default networking interface
    // if you use WiFi: see mbed_app.json for the credentials
    WiFiInterface* network = WiFiInterface::get_default_instance();
    if (!network) {
        printf("ERROR: No WiFiInterface found.\n");
        return -1;
    }

    printf("\nConnecting to %s...\n", MBED_CONF_APP_WIFI_SSID);
    int ret = network->connect(MBED_CONF_APP_WIFI_SSID, MBED_CONF_APP_WIFI_PASSWORD, NSAPI_SECURITY_WPA_WPA2);
    if (ret != 0) {
        printf("\nConnection error: %d\n", ret);
        return -1;
    }

    printf("Success\n\n");
    printf("MAC: %s\n", network->get_mac_address());
    SocketAddress a;
    network->get_ip_address(&a);
    printf("IP: %s\n", a.get_ip_address());

    oled.clear();
    oled.cursor( 1, 0 );    
    oled.printf("Scan Card");
    while( 1 )
    {
        
        if ( rfidReader.PICC_IsNewCardPresent())
        {
                
                if ( rfidReader.PICC_ReadCardSerial()) 
                {
                    oled.clear();
                    card_id = "";
                    oled.cursor( 1, 0 );                
                    // Print Card UID (2-stellig mit Vornullen, Hexadecimal)
                    oled.printf("UID: ");
                    
                    for ( int i = 0; i < rfidReader.uid.size; i++ )
                    {
                        oled.printf("%02X:", rfidReader.uid.uidByte[i]);
                        //printf("%02X:", rfidReader.uid.uidByte[i]);
                        card_id = card_id + std::to_string(rfidReader.uid.uidByte[i]) + ":";
                    }
                    std::cout << std::string(card_id+"\r\n");


                   
                    
                    // Print Card type
                    int piccType = rfidReader.PICC_GetType(rfidReader.uid.sak);

                    hum_temp.get_temperature(&temperature);
                    hum_temp.get_humidity(&humidity);
                    //printf("HTS221:  [temp] %.2f C, [hum]   %.2f%%, [UID] %s\r\n", value1, value2, cardid.c_str());
             
                    oled.clear();
                    oled.cursor( 1, 0 );
                    oled.printf("Scan successful");

                     /*json j= {
                        {"temperature", value1},
                        {"humidity", value2},
                        {"cardId", cardid}
                    };*/                    //HttpRequest to backend
                    HttpRequest* post_req = new HttpRequest( network, HTTP_POST, "https://m242cloud.azurewebsites.net/api/iotkit");
                    char body[1024];
                    sprintf( body, "{ \"temperature\": \"%f\", \"humidity\": \"%f\", \"UID\": \"%s\"}", temperature, humidity, card_id.c_str());
                    //sprintf(j);
                    HttpResponse* post_res = post_req->send(body, strlen(body));
                }
        }
    }
    
}