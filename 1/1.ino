#include <WiFi.h>
#include <DHT.h> //Install the DHT library
#include <ThingSpeak.h> //Install the ThingSpeak library

char* ssid = "Karthi"; //enter SSID
char* passphrase = "Karthi123"; // enter the password

WiFiServer server(80);
WiFiClient client;
unsigned long myChannelNumber = 2638550;
const char * myWriteAPIKey = "YZ7G5VXMEAXOZYGZ";

unsigned long lastTime = 0;
unsigned long timerDelay = 1000;
// ---DHT declarations
#define DHTPIN 4 // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11 // DHT 11
// Initializing the DHT11 sensor.
DHT dht(DHTPIN, DHTTYPE);
void setup()
{
Serial.begin(115200); //Initialize serial
Serial.print("Connecting to ");
Serial.println(ssid);
WiFi.begin(ssid, passphrase);
while (WiFi.status() != WL_CONNECTED) {
delay(500);
Serial.print(".");
}
// Print local IP address and start web server
Serial.println("");
Serial.println("WiFi connected.");
Serial.println("IP address: ");
Serial.println(WiFi.localIP());
server.begin();
// ---nitialize dht11
dht.begin();
ThingSpeak.begin(client); // Initialize ThingSpeak
}
void loop ()
{
if ((millis() - lastTime) > timerDelay)
{
delay(2500);
float t = dht.readTemperature ();
// Read temperature as Celsius (the default)
float h = dht.readHumidity ();
float f = dht.readTemperature(true);
if (isnan(h) || isnan(t) || isnan(f)) {
Serial.println(F("Failed to read from DHT sensor!"));
return;
}
Serial.print("Temperature (ºC): ");
Serial.print(t);
Serial.println("ºC");
Serial.print("Humidity");
Serial.println(h);
ThingSpeak.setField(1, t);
ThingSpeak.setField(2, h);
// Write to ThingSpeak. There are up to 8 fields in a channel, allowing you tostore up to 8 different
// pieces of information in a channel. Here, we write to field 1.
int x = ThingSpeak.writeFields(myChannelNumber,myWriteAPIKey);
if(x == 200){
Serial.println("Channel update successful.");
}
else{
Serial.println("Problem updating channel. HTTP error code " + String(x));
}
lastTime = millis();
}
}