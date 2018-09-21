
const int sensorPin = A0;    // select the input pin for the potentiometer
const int ledAnalog = 11;
int sensorMap;

void setup() {
  Serial.begin(9600);
  digitalWrite(ledAnalog, OUTPUT);
}


void loop() {
  // read the value from the sensor:
  int sensorValue = analogRead(sensorPin);
  sensorMap = map(sensorValue, 0, 1024, 0, 255);
  if (sensorMap < 100){
    analogWrite(ledAnalog, 255);
  }else{
    analogWrite(ledAnalog, 0);
  }
  
  Serial.println(sensorMap);  
  delay(100);
}
