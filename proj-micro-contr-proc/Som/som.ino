const int led = 13; 
const int pinPot = A5;
int periodo = 1;
int tempo_inicial = 0;


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
  delayMicroseconds(tempo_onda);
  digitalWrite(led, LOW);
  delayMicroseconds(tempo_intervalo);
}

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  pinMode(pinPot, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  int tempo_atual = millis();
  if(tempo_atual - tempo_inicial>= 100){
    periodo++;
    tempo_inicial = tempo_atual;
  }
  int valor_lido = analogRead(pinPot);
  int duty = map(valor_lido, 0, 1023, 0, 100);
  dutyCicle(duty);
}
