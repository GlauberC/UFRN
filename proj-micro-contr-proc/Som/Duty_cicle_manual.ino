const int led = 13;
const int pinPot = A5;
const int periodo = 20;



void dutyCicle(int n){
  // Recebe porcentagem
  int porcent = n;
  int tempo_maximo = periodo;
  int tempo_onda = (tempo_maximo * porcent) / 100;
  int tempo_intervalo = (tempo_maximo * (100 - n)) / 100; 
  pisca(tempo_onda, tempo_intervalo);
}
void pisca(int tempo_onda, int tempo_intervalo){
  digitalWrite(led, HIGH);
  delay(tempo_onda);
  digitalWrite(led, LOW);
  delay(tempo_intervalo);
}

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  pinMode(pinPot, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int valor_lido = analogRead(pinPot);
  int duty = map(valor_lido, 0, 1023, 0, 100);
  dutyCicle(duty);
}
