const long pausa_curta = 100;
const long pausa_longa = 300;
const int intervalo_char = 500;

unsigned long esperainicial;
unsigned long tempoinicial;
unsigned long tempoatual;
unsigned long diferenca_tempo;

const int led = 13;

const int evita_ruido = 30;

int estado = 0;
String letra = "";

char morse(long tempo){
  char mor;
  if(tempo <= 150){
    mor = '.';
  }else if(tempo >=250 && tempo<=500){
    mor = '-';
  }else if(tempo > 500){
    Serial.println("Invalido");
    mor = ' ';
  }
  return mor;
}

char retorna_letra(String letra){
  char let;
  // R
  if(letra == "---"){
    let = 'O';
  }else if(letra == ".-."){
    let = 'R';
  }else if(letra == "..."){
    let = 'S';
  }else if(letra == "..-"){
    let = 'U';
  }
  return let;
}


void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  pinMode(A0, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  if (estado == 0){
    if(!digitalRead(A0)){
      tempoinicial = millis();
      delay(evita_ruido);
      estado = 1;
    }else if(letra.length()>0){
      if(millis() - esperainicial > 1000){
        estado = 3;
      }
      
    }
  }else if(estado == 1){
    //Conta o tempo
    tempoatual=millis();
    
    //Ao soltar o botão
    if(digitalRead(A0)){
      delay(evita_ruido);
      estado = 2;
    }
  }else if(estado == 2){
    // Criar letra
    diferenca_tempo = tempoatual - tempoinicial;
    char mor = morse(diferenca_tempo);
    if(mor == ' '){
      estado = 3;
    }else{
      letra.concat(mor);
      estado = 0;
      esperainicial = millis();
    }
    
    
    estado = 0;
  }else if(estado == 3){
    // ver letra
    Serial.println(letra);
    Serial.println(retorna_letra(letra));
    
    // voltar ao estado
    letra = "";
    estado = 0;
  }


}
