// Include the Arduino Stepper Library
#include <Stepper.h>

// Number of steps per output rotation
const int stepsPerRevolution = 200 ;
String command;
// Create Instance of Stepper library
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);
//Stepper myStepper2(stepsPerRevolution, 4, 5, 6, 7);

void setup()
{
    // Set the speed at 60 rpm
    myStepper.setSpeed(70);
    //myStepper2.setSpeed(60);
    // Initialize the serial port
    Serial.begin(115200);
    pinMode(13, OUTPUT);
}

void loop() 
{
    if (Serial.available()) {
      command = Serial.readString();
      command.trim();
      if (command == "clockwise") {
          // Move clockwise
          digitalWrite(13, HIGH); 
          for (int i =0;i<13;i++) {
            myStepper.step(1);
          }
          //myStepper2.step(stepsPerRevolution);
      }
      else if (command == "counterclockwise") {
          // Move counterclockwise
          digitalWrite(13, LOW);  
          for (int i =0;i<13;i++) {
            myStepper.step(-1);
          }
          //myStepper2.step(-stepsPerRevolution);
      }
    } 
    
}
