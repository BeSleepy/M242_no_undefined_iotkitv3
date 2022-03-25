/** Beispiel Senden von Sensordaten an ThingSpeak
    */
#include "http_request.h"
#include "OLEDDisplay.h"
#include "MFRC522.h"
#include "mbed.h"
#include <cstdio>
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
    float value1, value2;

   

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


    oled.printf("Scan Card");  
    while( 1 )
    {
        
        if ( rfidReader.PICC_IsNewCardPresent())
        {
                
                if ( rfidReader.PICC_ReadCardSerial()) 
                {
                    oled.clear();
                    oled.cursor( 1, 0 );                
                    // Print Card UID (2-stellig mit Vornullen, Hexadecimal)
                    oled.printf("UID: ");
                    for ( int i = 0; i < rfidReader.uid.size; i++ )
                        oled.printf("%02X:", rfidReader.uid.uidByte[i]);
                    oled.printf("\r\n");
                    
                    // Print Card type
                    int piccType = rfidReader.PICC_GetType(rfidReader.uid.sak);
                    oled.printf("PICC Type: %s \r\n", rfidReader.PICC_GetTypeName(piccType) );

                    hum_temp.get_temperature(&value1);
                    hum_temp.get_humidity(&value2);

                    sprintf( message, "%s?key=%s&field1=%f&field2=%f", host, key, value1, value2 );
                    printf( "%s\n", message );
                    oled.cursor( 1, 0 );
                    oled.printf( "temp: %3.2f\nhum : %3.2f", value1, value2 );

                    //myled = 1;
                    HttpRequest* get_req = new HttpRequest( network, HTTP_POST, message );

                    HttpResponse* get_res = get_req->send();
                    if (!get_res)
                    {
                        printf("HttpRequest failed (error code %d)\n", get_req->get_error());
                        return 1;
                    }
                    delete get_req;
                    //myled = 0;
                }  
        }
    }
    
}