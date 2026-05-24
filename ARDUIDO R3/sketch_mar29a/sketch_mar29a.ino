#include <Servo.h>

Servo motor;
void setup(){
  motor.attach(9);

}

void loop(){
  for(int i = 20; i<=180; i++){
    motor.write(i);
    delay(40);
  }
  delay(2000);
 
}