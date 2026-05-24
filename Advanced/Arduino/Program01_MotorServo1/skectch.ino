#include <Servo.h>
Servo motor1;
Servo motor2;
Servo motor3;

int range1 = 180;
int range2 = 45;
int range3 = 30;



void setup(){
  motor1.attach(9);
  motor2.attach(10);
  motor3.attach(11);



  motor1.write(0);
  motor2.write(0);
  motor3.write(0);
  delay(1000);
}


void loop(){
  for (int s = 0; s <= range1; s++){ motor1.write(s); delay(15);}
  delay(1000);
  
  for (int s = 0; s <= range2; s++) { motor2.write(s); delay(15); }
  delay(1000);

  for (int s = 0; s <= range3; s++) { motor3.write(s); delay(15); }
  delay(1000);
 

 for(int d = 180; d >= 0; d--){
  if(d <= range1) motor1.write(d);
  if(d <= range2) motor2.write(d);
  if(d <= range3) motor3.write(d);
  delay(15);
 }
 delay(3000);
}
