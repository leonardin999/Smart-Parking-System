#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

int startbyte;
int slot;
void setup() {
  // put your setup code here, to run once:
  lcd.init();
  lcd.begin(16,2);;
  lcd.backlight();
  lcd.clear();
  // Change this Digital output
  pinMode(1, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  lcd.setCursor(5,0);
  lcd.print("WELCOME");
  lcd.setCursor(1,1);
  lcd.print("SMART PARKING!");
  delay(1000);
}

void loop() {
  // Wait for serial input (min 3 bytes in buffer)
  lcd.clear();
  lcd.setCursor(5,0);
  lcd.print("WELCOME");
  lcd.setCursor(1,1);
  lcd.print("SMART PARKING!");
  if (Serial.available() > 0) {
    // Read the first byte
    slot = Serial.read();
    if (slot < 13) {
      digitalWrite(LED_BUILTIN, HIGH);
      digitalWrite(slot, HIGH);
      String message = String("Activate guild to slot "+String(slot));
      lcd.clear();
      lcd.setCursor(5,0);
      lcd.print("ACTIVATE");
      lcd.setCursor(0,1);
      lcd.print("GUIDE TO SLOT "+String(slot)+"."); 
      Serial.println(message);
    }//startbyte ok
    else{
      digitalWrite(slot, LOW);
      for( int i=0; i<13; i++){
          digitalWrite(i, LOW);
        }
      String message = String("Process Completed");
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("GUIDE COMPLETED."); 
      Serial.println(message);
      digitalWrite(LED_BUILTIN, LOW);
    }
  }//serial avail
  delay(7000);
}//loop
