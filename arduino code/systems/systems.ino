int startbyte;
int slot;
void setup() {
  // put your setup code here, to run once:
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
}

void loop() {
  // Wait for serial input (min 3 bytes in buffer)
  if (Serial.available() > 3) {
    // Read the first byte
    slot = Serial.read();
    Serial.println(slot);
    if (slot < 12) {
      digitalWrite(LED_BUILTIN, HIGH);
        digitalWrite(slot, HIGH);
        String message = String("Guild to Slot: "+String(slot)+"."); 
        Serial.println(message);
        Serial.print("");

    }//startbyte ok
    else{
      digitalWrite(slot, LOW);
      String message = String("Guildline completed."); 
      Serial.println(message);
      Serial.print("");
    }
  }//serial avail
}//loop
