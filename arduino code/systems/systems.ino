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
  if (Serial.available() > 0) {
    // Read the first byte
    slot = Serial.read();
    if (slot < 13) {
      digitalWrite(LED_BUILTIN, HIGH);
      digitalWrite(slot, HIGH);
      String message = String("Activate guild to slot "+String(slot)); 
      Serial.println(message);
    }//startbyte ok
    else{
      digitalWrite(slot, LOW);
      for( int i=0; i<13; i++){
          digitalWrite(i, LOW);
        }
      String message = String("Process Completed"); 
      Serial.println(message);
      digitalWrite(LED_BUILTIN, LOW);
    }
  }//serial avail
}//loop
