int estado = 0;
const int led = 13;
const int duracao = 3000;
unsigned long tempoinicial = 0;
unsigned long tempoatual = 0;
void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  pinMode(A0, INPUT_PULLUP);
}

void loop() {
  switch(estado){
    case 0:
      digitalWrite(led, LOW);
      if(!digitalRead(A0)){
        estado = 1;
        tempoinicial = millis();
        delay(50);
      }
      break;
    case 1:
      digitalWrite(led, HIGH);
      tempoatual=millis();
      if(digitalRead(A0)){
        delay(50);
        estado = 2;
      }else if(tempoatual-tempoinicial>=duracao){
        estado = 3;
      }
      break;
    case 2:
      tempoatual=millis();
      if(!digitalRead(A0)){
        estado = 3;
        delay(50);
      }else if(tempoatual-tempoinicial>=duracao){
        estado = 0;
      }
      break;
    case 3:
      digitalWrite(led, LOW);
      if(digitalRead(A0)){
        estado = 0;
        delay(50);
      }
      break;
  }

}
