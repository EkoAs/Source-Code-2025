#include "Servo.h"
Servo motor;
Servo motor2;
Servo motor3;


void setup() {
 motor.attach(9);
 motor2.attach(10);
//  motor3.attach(6);
 motor.write(0);
 motor2.write(180);
}

void loop() {
//  for (int i = 9; i >= 0; i--){
//   motor.write(i * 20);
//   delay(1000);
//  }
int sudut = 180;
int pos = 0;


//  for (int i = 9; i >= 0; i--){
//   motor2.write(i * 20);
//   delay(1000);
//  }

  for(pos=0;pos<=90; pos+=1){
    motor.write(pos);
    // motor3.write(pos);
    motor2.write(180-pos);

    delay(100);
  }
 
 delay(1000);
//  for(pos=0;pos<=90; pos+=1){
//     motor2.write(pos);
//     // motor3.write(pos);
//     // motor2.write(180-pos);

//     delay(100);
//   }
//  delay(2000);

// //  for(int pos=90;pos >=0; pos--){
// //    motor2.write(pos);
// //   //  motor3.write(pos);
// //   //  motor2.write(180-pos);

// //    delay(60);

// //  }
 delay(1000);
 for(int pos=90;pos >=0; pos--){
   motor.write(pos);
  //  motor3.write(pos);
   motor2.write(180-pos);

   delay(60);

 }
 
 delay(6000);
}
