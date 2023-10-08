#include <Wire.h>

#define I2C_ADDRESS 0x60 // I2C address of the MiniMoto motor driver
#define SDA_PIN 4        // SDA pin (connect to pin 4 on Seeed Xiao)
#define SCL_PIN 5        // SCL pin (connect to pin 5 on Seeed Xiao)

void setup()
{
    Serial.begin(115200); // Initialize Serial communication
    Wire.begin(SDA_PIN, SCL_PIN); // Initialize I2C communication with SDA and SCL pins
    Wire.setClock(400000); // Set I2C clock frequency to 400 kHz
    analogWriteResolution(12); // Set PWM resolution to 12 bits (0-4095)
    Serial.println("Hello, world!"); // Print "Hello, world!" to Serial Monitor
}

void loop()
{
    // Example: Sending commands to MiniMoto motor driver via I2C
    // Start motor 0 forward at full speed
    setMotorSpeed(0, 4095);
    delay(1000);
    
    // Stop motor 0
    setMotorSpeed(0, 0);
    delay(1000);
    
    // Start motor 1 reverse at half speed
    setMotorSpeed(1, 2048);
    delay(1000);
    
    // Stop motor 1
    setMotorSpeed(1, 0);
    delay(1000);
}

void setMotorSpeed(byte motor, int speed)
{
    Wire.beginTransmission(I2C_ADDRESS);
    Wire.write(motor);      // Send motor number (0 or 1)
    Wire.write(speed & 0xFF); // Send low byte of speed
    Wire.write(speed >> 8);   // Send high byte of speed
    Wire.endTransmission();
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