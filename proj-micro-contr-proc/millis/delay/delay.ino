int estado = 0;
void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  pinMode(A0, INPUT_PULLUP);
}

void loop() {
  if(estado == 0){
    digitalWrite(13, LOW);
  }
  if(!digitalRead(A0)){
    digitalWrite(13, HIGH);
    delay(50);
    estado = 1;
    
  }
  if(estado == 1){
    delay(3000);
    if(digitalRead(A0)){
      estado = 0;
    }
    estado = 0;
    
  }

}
