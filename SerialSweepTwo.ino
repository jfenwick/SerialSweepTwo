/*
  SerialSweepTwo
  Reads serial data until the null byte and turns that data into servo movement for two servos

*/
#include <Servo.h> 

Servo myservo1;
Servo myservo2;
char serialData[8];
char serialData1[4];
char serialData2[4];
int pos1 = 20;
int pos2 = 165;

void setup() {
  Serial.begin(115200);
  Serial.println("Ready");
  myservo1.attach(9);
  myservo1.write(20);
  myservo2.attach(10);
  myservo2.write(165);
}

void loop() {
  if (Serial.available()) {
    Serial.readBytesUntil('\0', serialData, 6);
    memmove(serialData1, serialData, 3);
    memmove(serialData2, serialData+3, 3);

    pos1 = atoi(serialData1);
    pos2 = atoi(serialData2);

    myservo1.write(pos1);
    myservo2.write(pos2);
  }
}
