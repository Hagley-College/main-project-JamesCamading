#include <IRremote.hpp>

#define IR_RECEIVE_PIN 2
#define RED_LED_PIN 3
#define GREEN_LED_PIN 4

void toggleLED(int pin) {
digitalWrite(pin, !digitalRead(pin)); // Toggle LED state
}

void setup() {
Serial.begin(9600);
IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK);

pinMode(RED_LED_PIN, OUTPUT);
pinMode(GREEN_LED_PIN, OUTPUT);
}

void loop() {
  if (IrReceiver.decode()) {
  uint16_t command = IrReceiver.decodedIRData.command;
  Serial.println(command);
  switch (command) {
    case 0x10: // Replace with your remote's command for RED LED
      toggleLED(RED_LED_PIN);
      break;
    case 0x20: // Replace with your remote's command for GREEN LED
      toggleLED(GREEN_LED_PIN);
      break;
    default:
      Serial.println("Unknown Command");
    }
  IrReceiver.resume();
  }
}
