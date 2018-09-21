const long pausa_curta = 100;
const long pausa_longa = 300;
const int intervalo_char = 500;

void pisca_curto(int led){
  digitalWrite(led, HIGH);
  delay(pausa_curta);
  digitalWrite(led, LOW);
  delay(pausa_curta);
}
void pisca_longo(int led){
  digitalWrite(led, HIGH);
  delay(pausa_longa);
  digitalWrite(led, LOW);
  delay(pausa_longa);
}


const int led = 13;
char vogal = ' ';

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()){
    vogal = Serial.read();

    if(vogal == 'a'){
      pisca_curto(led);
      delay(pausa_curta);
      pisca_longo(led);
      delay(intervalo_char);
    }else if(vogal == 'e'){
      pisca_curto(led);
      delay(intervalo_char);
    }else if(vogal == 'i'){
      pisca_curto(led);
      delay(pausa_curta);
      pisca_curto(led);
      delay(intervalo_char);
    }else if(vogal == 'o'){
      pisca_longo(led);
      delay(pausa_curta);
      pisca_longo(led);
      delay(pausa_curta);
      pisca_longo(led);
      delay(intervalo_char);
    }else if(vogal == 'u'){
      pisca_curto(led);
      delay(pausa_curta);
      pisca_curto(led);
      delay(pausa_curta);
      pisca_longo(led);
      delay(intervalo_char);
    }
  }else{
    vogal == '_';
  }
  
  


}
