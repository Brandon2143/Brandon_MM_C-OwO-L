#include <Wire.h>

void setup()
{
  Wire.begin(); // join i2c bus (address optional for master)
}

byte x = 0;

void loop()
{
  Wire.beginTransmission(4); // transmit to device #4
  Wire.write("x is ");        // sends five bytes
  Wire.write(x);              // sends one byte  
  Wire.endTransmission();    // stop transmitting
  x++;
  delay(500);
}

/*int PWM = 128;                 //maximum power
static volatile int16_t countA=0;
static volatile int16_t countB=0;
float rpm = 0; float rpmA = 0; float rpmB = 0; //rpm for motors

#define MotorPWM_A 46//left motor
#define MotorPWM_B 44//right motor
#define AIN1 32
#define AIN2 34
#define BIN1 30
#define BIN2 36
#define encoderA 2
#define encoderB 3


void setup(){
  Serial.begin(9600);
  pinMode(MotorPWM_A, OUTPUT);
  pinMode(MotorPWM_B, OUTPUT);
  pinMode(AIN1, OUTPUT);
  pinMode(AIN2, OUTPUT);
  pinMode(BIN1, OUTPUT);
  pinMode(BIN2, OUTPUT);
  pinMode(encoderA, INPUT_PULLUP);
  pinMode(encoderB, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(encoderA), IRSA, FALLING);
  attachInterrupt(digitalPinToInterrupt(encoderB), IRSB, FALLING);
}

void loop() {
  for (int i=0; i <=255; i = i+5){
  PWM = i;
  forward();delay(1000);
  RPM_Measure();
  Serial.print(PWM);
  Serial.print(", ");
  Serial.print(rpmA);
  Serial.print(", ");
  Serial.print(rpmB);
  Serial.print(", ");
  Serial.println(rpm);
  }
  stoprobot();
  while(1);
}
void RPM_Measure(){
  countA=0;countB=0;
  delay(100);
  rpmA = countA*3.125; rpmB = countB*3.125;
  rpm = (rpmA+rpmB)/2;
}
void IRSA(){
  countA++;
}
void IRSB(){
  countB++;
}
void stoprobot(){
    digitalWrite(AIN1, LOW);
    digitalWrite(AIN2, LOW);
    digitalWrite(BIN1, LOW);
    digitalWrite(BIN2, LOW);

}

void forward() {
  analogWrite(MotorPWM_A, PWM);
  analogWrite(MotorPWM_B, PWM);
    digitalWrite(AIN1, LOW);
    digitalWrite(AIN2, HIGH);
    digitalWrite(BIN1, LOW);
    digitalWrite(BIN2, HIGH);
}
*/