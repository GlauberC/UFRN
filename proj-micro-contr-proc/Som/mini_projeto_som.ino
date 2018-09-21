const long periodo = 50;
const int pause = 50;


const int pin = 10;
const int c = 261;
const int d = 294;
const int e = 329;
const int f = 349;
const int g = 392;
//const int a = 440;
const int a = 220;

//const int b = 493;
const int b = 247;

const int c2 = 523;

//int beats[] = { 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 4 };
//int beats[] = { 1, 1, 1, 2, 1, 1,1,1, 1, 1, 2, 1, 1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,4};
int beats[] = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1};
//String notes = "ccggaagffeeddc";
//String notes = "cdefff cdcddd cgfeee cdefff ";
String notes = "bbbbb bbbbbbb eeeeeee ddddddd a bbbbbb bbbbbb be bbbbb bbbbbbbd";

int retorna_nota(char l){
  switch(l){
    case 'c':
      return c;
    case 'd':
      return d;
    case 'e':
      return e;
    case 'f':
      return f;
    case 'g':
      return g;
    case 'a':
      return a;
    case 'b':
      return b;
    default:
      return 0;
  }
}

void setup() {
  // put your setup code here, to run once:
  pinMode(pin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i = 0; i < notes.length(); i++){
    long tempo = periodo * beats[i];
    Serial.println(notes[i]);
    int nota = retorna_nota((notes[i]));
    if (nota == 0){
      noTone(pin);
    }else {
      tone(pin, nota);
    }
    delay(tempo);
    
    noTone(pin);
    delay(pause);
    
    
  }
}
