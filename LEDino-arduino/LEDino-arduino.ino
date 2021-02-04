/* 
 *  Receptor de paquetes UDP y controlador de LED tricolor
 *  
 *  Recordar que en la red "bart" el arduino tiene un IP fija: 192.168.1.14
 *
 *  Valentin Berman 6/1/21
 */



#include <SPI.h>
#include <WiFi101.h>
#include <WiFiUdp.h>


// Punto de acceso y contraseña:
const char ssid[5] = "Bart";
const char pass[9] = "Ayudante";

// Puerto:
const unsigned int puerto = 51234;

// Clases:
WiFiUDP UDP;

// Variables:
char paquete[100];
int estado = WL_IDLE_STATUS;
bool parpadear = false;
bool ledEncendido = true; // contrala cuando se prende o apaga el led en el parpadeo
int tamanoPaquete;
int larg;
unsigned long tiempo1, tiempo2;


// Constantes
const byte pinRojo = 0;
const byte pinVerde = 1;
const byte pinAzul = 2;

const unsigned int timeout = 20000; //tiempo para determinar conección perdida en milisegundos

const unsigned int largoParpadeo = 500; // en ms

// Estructuras definidas por el usuario
struct Color {
  byte rojo;
  byte verde;
  byte azul;
} color;



void setup() {


  // Inicia los pines para el led
  pinMode(pinRojo, OUTPUT);
  pinMode(pinVerde, OUTPUT);
  pinMode(pinAzul, OUTPUT);

  
  // Inicia conexión serial
//  Serial.begin(9600);
//  while (!Serial) {
//    ; // espera a la conexión al puerto serial
  //}
  

  // Inicia una conexión a la red
  tiempo1 = millis();
  while (estado != WL_CONNECTED) 
  {   
    estado = WiFi.begin(ssid, pass);
    tiempo2 = millis();
    if ((tiempo2 - tiempo1) > timeout) problemaLED(); // problemaLED termina el flujo del programa
  }

  // Indicación que el arduino está listo, y da tiempo para que esté lista la conexión
  for (int i = 1; i <= 5; i++)
  {
    analogWrite(pinAzul, 0);
    analogWrite(pinRojo, 255);
    delay(200);
    analogWrite(pinRojo, 0);
    analogWrite(pinVerde, 255);
    delay(200);
    analogWrite(pinVerde, 0);
    analogWrite(pinAzul, 255);
    delay(200);
  }
  apagarLED();
  

  // Mensaje de exito
//  Serial.print("Conectado exitosamente a: ");
//  Serial.println(ssid);
  
  // Inicia un servidor UDP
  UDP.begin(puerto);

  // Define el color inicial del LED
  color.rojo = 0;
  color.verde = 0;
  color.azul = 0;

  // Define el tiempo1 para ser usado más adelante en el parpadeo
  tiempo1 = millis();

}//fin setup


void loop() {
  
  // Recibe un paquete UDP
  tamanoPaquete = UDP.parsePacket();    // .parsePacket se tiene que ejecutar antes que .read

  if(tamanoPaquete)    // Se ejecuta si se recive un paquete
  {
    
    larg = UDP.read(paquete, 100);
    if (larg > 0) paquete[larg] = 0; // termina el string paquete despues del último caracter recibido (recordar que 0 es el fin de un string)

    
    // Determina que hacer según el tipo de mensaje
    // 'c' --> cambio de color
    // 'p' --> parpeadeo
    // 'a' --> enviar el estado actual
    
    switch (paquete[0]) {
      case 'c':
        color = decodificarColor(paquete);
        break;
      case 'p':
        parpadear = decodificarParpadear(paquete, parpadear);
        break;
      case 'a':
        // WIP
        break;
      }
    
  }

  // Controla el comportamiento del LED:
  tiempo2 = millis();
  iluminarLED(color, parpadear, ledEncendido);
  if ((tiempo2 - tiempo1) > largoParpadeo) {
    tiempo1 = tiempo2; // reinicia el temporisador
    ledEncendido = !ledEncendido; // controla el parpadeo del led;
  }

  // Verifíca la conexión
  if (WiFi.status() != WL_CONNECTED) problemaLED();
  
  
}//fin loop



// Funciones:

struct Color decodificarColor(String paquete) {
  // Devuelve una estructura 'color' que contiene los valores con que se debe iluminar el LED

  struct Color color;
  byte separador;

  //Busca el valor de rojo
                                             // substring(1) ignora el primer caracter, que indica el tipo de instrucción
  color.rojo = paquete.substring(1).toInt(); // toInt() convierte el string a digitos hasta que no queden más digitos.
                                             // Deja de convertir a digitos cuando llega al ':'.

  //Busca el valor verde
  
  separador = paquete.indexOf(':');

  color.verde = paquete.substring(separador + 1).toInt();
  

  //Busca el valor de azul

  separador = paquete.indexOf(':', separador + 1);

  color.azul = paquete.substring(separador + 1).toInt();

  return color;
  
}

bool decodificarParpadear(char paquete[100], bool parpadear) {
  // Devuelve el nuevo estado de parpadeo del LED

  switch (paquete[1]) {
    case 'e':
      parpadear = true;
      break;
    case 'a':
      parpadear = false;
      break;
    case 'c':
      parpadear = !parpadear;
      break;
  }
  return parpadear;
}

void iluminarLED(struct Color color, bool parpadear, bool ledEncendido) {
  //Ilumina el led tricolor del color correspondiente

    if (parpadear && !ledEncendido) {      
      apagarLED();
    }
    else {
      analogWrite(pinRojo, color.rojo);
      analogWrite(pinVerde, color.verde);
      analogWrite(pinAzul, color.azul);
    }
}//fin iluminarLED

void problemaLED(){
  // Un patrón de luces que indica un problema
  // Termina el flujo del programa
  
  apagarLED();
  while (true) {
    for (int i = 1; i <= 3; i++){
      analogWrite(pinRojo, 255);
      delay(100);
      analogWrite(pinRojo, 0);
      delay(100);
    }
    delay(1000);
  }
  
}//fin problemaLED

void apagarLED(){
  // apaga completamente el led
  
  analogWrite(pinRojo, 0);
  analogWrite(pinVerde, 0);
  analogWrite(pinAzul, 0);
  
}//fin apagarLED
