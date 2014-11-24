#include <LiquidCrystal.h>

/*******************************************************

This program will test the LCD panel and the buttons
Mark Bramwell, July 2010

********************************************************/

// select the pins used on the LCD panel
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

// define some values used by the panel and buttons
int lcd_key     = 0;
int adc_key_in  = 0;

void setup()
{
 for(byte i=0;i<8;i++)
 {
   pinMode(22+i,OUTPUT);
 }
 Serial.begin(9600);
 //analogReference(3);
 lcd.begin(16, 2);              // start the library
 lcd.setCursor(0,0);
 lcd.print("Voltaje: "); // print a simple message
}
 
void loop()
{
 lcd.setCursor(9,0);            // move cursor to second line "1" and 9 spaces over

 int sensorValue = analogRead(A1);
 float voltage = sensorValue * (4.35 / 1023.0);
 //float voltage = .21;
 lcd.print(voltage);
 float voltaje_real = voltage * (1100)/(100);
 lcd.setCursor(0,1);
 lcd.print(voltaje_real);
  Serial.println(voltaje_real);
  delay(500);
}


