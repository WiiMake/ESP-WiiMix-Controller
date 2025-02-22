#include "main.h"
#include <Arduino.h>
#include <WiFi.h> // Include the WiFi library

void setup() {
  WiFi.mode(WIFI_OFF); // Disable Wi-Fi
  btStop(); // Disable Bluetooth if it's enabled

  Serial.begin(115200);
  delay(10000);
  Serial.println("Initing");

  pinMode(BTN_A, INPUT_PULLUP);
  pinMode(BTN_B, INPUT_PULLUP);
  pinMode(BTN_X, INPUT_PULLUP);
  pinMode(BTN_Y, INPUT_PULLUP);
  pinMode(BTN_UP, INPUT_PULLUP);
  pinMode(BTN_DOWN, INPUT_PULLUP);
  pinMode(BTN_LEFT, INPUT_PULLUP);
  pinMode(BTN_RIGHT, INPUT_PULLUP);
  pinMode(BTN_START, INPUT_PULLUP);
  pinMode(BTN_Z, INPUT_PULLUP);
  pinMode(BTN_L, INPUT_PULLUP);
  pinMode(BTN_R, INPUT_PULLUP);
  pinMode(ADC_LEFT_X, INPUT);
  pinMode(ADC_LEFT_Y, INPUT);
  pinMode(ADC_RIGHT_X, INPUT);
  pinMode(ADC_RIGHT_Y, INPUT);
  pinMode(ADC_TRIGGER_L, INPUT);
  pinMode(ADC_TRIGGER_R, INPUT);
}

void loop() {
  // create a computer parsable string for the controller state
  Serial.print("A:");
  Serial.print(digitalRead(BTN_A));
  Serial.print(" B:");
  Serial.print(digitalRead(BTN_B));
  Serial.print(" X:");
  Serial.print(digitalRead(BTN_X));
  Serial.print(" Y:");
  Serial.print(digitalRead(BTN_Y));
  Serial.print(" UP:");
  Serial.print(digitalRead(BTN_UP));
  Serial.print(" DOWN:");
  Serial.print(digitalRead(BTN_DOWN));
  Serial.print(" LEFT:");
  Serial.print(digitalRead(BTN_LEFT));
  Serial.print(" RIGHT:");
  Serial.print(digitalRead(BTN_RIGHT));
  Serial.print(" START:");
  Serial.print(digitalRead(BTN_START));
  Serial.print(" Z:");
  Serial.print(digitalRead(BTN_Z));
  Serial.print(" L:");
  Serial.print(digitalRead(BTN_L));
  Serial.print(" R:");
  Serial.print(digitalRead(BTN_R));
  Serial.print(" LEFT_X:");
  Serial.print(analogRead(ADC_LEFT_X));
  Serial.print(" LEFT_Y:");
  Serial.print(analogRead(ADC_LEFT_Y));
  Serial.print(" RIGHT_X:");
  Serial.print(analogRead(ADC_RIGHT_X));
  Serial.print(" RIGHT_Y:");
  Serial.print(analogRead(ADC_RIGHT_Y));
  Serial.print(" TRIGGER_L:");
  Serial.print(analogRead(ADC_TRIGGER_L));
  Serial.print(" TRIGGER_R:");
  Serial.print(analogRead(ADC_TRIGGER_R));
  

  Serial.println();
  delay(1000);
}
