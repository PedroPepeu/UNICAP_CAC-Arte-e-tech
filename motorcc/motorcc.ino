// constant
const int enableBridge1 = 2;
const int motor1Forward = 3;
const int motor1Backward = 4;

// variables
int power = 80 // between 0 ~ 255;
int buttonPin = 7;
int buttonState = 0;

// general declaration calling declaration methods
void setup() {
  dcBegin();
  buttonBegin();
}

// button declaration
void buttonBegin() {
  pinMode(buttonPin, INPUT);
}

// h bridge declaration
void dcBegin() {
  pinMode(motor1Forward, OUTPUT);
  pinMode(motor1Backward, OUTPUT);
  pinMode(enableBridge1, OUTPUT);
}

void loop() {
  int button = buttonS();
  dcTurnOn();
  if(button = HIGH){
    dcForward();
    delay(2000);
  }
  dcStop();

}

int buttonS() {
  buttonState = digitalRead(buttonPin);  
}

long distance() {
  
}

// h bridge turning on
void dcTurnOn () {
  digitalWrite(enableBridge1, HIGH);
}

// turns on dc engine forward
void dcForward() {
  delay(1000);
  analogWrite(motor1Backward, 0);
  analogWrite(motor1Forward, Power);
}

// turns on dc engine backward
void dcBackward() {
  delay(1000);
  analogWrite(motor1Backward, Power);
  analogWrite(motor1Forward, 0);
}

// stop engines
void dcStop() {
  analogWrite(motor1Backward, 0);
  analogWrite(motor1Forward, 0);
}

// turns off h bridge
void dcTurnOff() {
  digitalWrite(enableBridge1, LOW);
}
