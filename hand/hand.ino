long int timer;
#include <Servo.h>
Servo hand;
void setup() {
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  
  hand.attach(6);
  attachInterrupt(1, zero, HIGH);
  attachInterrupt(0, releas, HIGH);
 
}

void loop() {
   hand.detach();
   delay(1000);
}
void zero() {  
    hand.attach(6);
    hand.write(0);
    delay(1000); 
  }
 void releas() {
    hand.attach(6);
    hand.write(90);
    delay(1000);
  }
