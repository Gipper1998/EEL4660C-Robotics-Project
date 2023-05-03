#include <Servo.h>                                                      // Include necessary libraries.
  
Servo sLeft;                                                            // Add Servo motor objects left and right.
Servo sRight;

void fromSerialToMotors(int cmd)                                        // Turn the int to string using if statements.
{
  switch(cmd)
  {
    case 0:                                                             // Stop motors.
    {
      sLeft.writeMicroseconds(1500);
      sRight.writeMicroseconds(1500);
      break;
    }
    case 1:                                                             // Goes forwards.
    {
      sLeft.writeMicroseconds(1300);
      sRight.writeMicroseconds(1700);
      break;
    }
    case 2:                                                             // Goes backwards.
    {
      sLeft.writeMicroseconds(1700);
      sRight.writeMicroseconds(1300);
      break;
    }
    case 3:                                                             // Goes right.
    {
      sLeft.writeMicroseconds(1300);
      sRight.writeMicroseconds(1300);
      break;
    }
    case 4:                                                             // Goes left.
    {
      sLeft.writeMicroseconds(1700);                                    
      sRight.writeMicroseconds(1700);
      break;
    }
    case 5:                                                             // Goes slight right.
    {
      sLeft.writeMicroseconds(1500);
      sRight.writeMicroseconds(1300);
      break;
    }
    case 6:                                                             // Goes slight left.
    {
      sLeft.writeMicroseconds(1700);
      sRight.writeMicroseconds(1500);
      break;
    }
    case 7:                                                             // Goes back right.
    {
      sLeft.writeMicroseconds(1500);
      sRight.writeMicroseconds(1700);
      break;
    }
    case 8:                                                             // Goes back left.
    {
      sLeft.writeMicroseconds(1300);
      sRight.writeMicroseconds(1500);
      break;
    }
    default:                                                            // Stops by default.
    {
      sLeft.writeMicroseconds(1500);
      sRight.writeMicroseconds(1500);
      break;
    }
  }
}

void setup()                                                            // Process Servo motors and Serial Communication.
{
  Serial.begin(9600);
  sLeft.attach(13);
  sRight.attach(12);
  sLeft.writeMicroseconds(1500);
  sRight.writeMicroseconds(1500);
}

void loop()                                                             // Serial Communication.
{
  if (Serial.available())
  {
    while(Serial.available() > 0)
    {
      int bit = Serial.read();                                          // Read the int from serial and go to function.
      fromSerialToMotors(bit - '0');
    }
    Serial.flush();                                                     // Clear serial.
  }
}
