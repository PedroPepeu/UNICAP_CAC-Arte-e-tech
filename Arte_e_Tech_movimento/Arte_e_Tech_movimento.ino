// Ultrasonic Sensor
#define echoPin 2;
#define trigPin 3;

long duration;
int distance;

// DC motor
const int m1Forward = 4;
const int m1Backward = 5;
const int enableBridge1 = 6;

//const int m2Forward = 6;
//const int m2Backward = 7;

int power = 80; // between 0 ~ 255

void setup() {
  pinMode(m1Forward, OUTPUT);
  pinMode(m1Backward, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600); // Serial Communication is starting with 9600 of baudrate speed
  Serial.println("Ultrasonic Sensor HC-SR04 Test");


  dcBegin();
  buttonBegin();

}

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
  // Clears the trigPin condition
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  // Displays the distance on the Serial Monitor
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  // will check the distance in centimeters
  if(distance < 50) {
    while(distance < 50) {
      engineOn();
    }
  } else {
    engineOff();
  }
  

}

// void engineOn() {
//   // everytime the sensor sees if someone is close enough to the wall, it turn's on
//   // I can put the loop here
  
// }

// void engineOff() {
//   delay(2000);
//   analogWrite(m1Forward,0);
// }

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
