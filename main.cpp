#include <Arduino.h>
#include "config.h"

void setup() {
    pinMode(RED_LED_PIN, OUTPUT);
    digitalWrite(RED_LED_PIN, HIGH);  // Red LED lights immediately at startup.

    digitalWrite(GREEN_LED_PIN, LOW);
    digitalWrite(ALERT_BUZZER_PIN, LOW);
    pinMode(GREEN_LED_PIN, OUTPUT);
    pinMode(ALERT_BUZZER_PIN, OUTPUT);

    noTone(ALERT_BUZZER_PIN);
    digitalWrite(ALERT_BUZZER_PIN, LOW);

    Serial.begin(COMMAND_BAUD);
    Serial.println(F("Ready: red LED ON; 1=phishing, 0=safe"));
}

void loop() {
    while (Serial.available() > 0) {
        const char command = static_cast<char>(Serial.read());

        switch (command) {
            case '1':
                digitalWrite(GREEN_LED_PIN, LOW);
                digitalWrite(RED_LED_PIN, HIGH);
                tone(ALERT_BUZZER_PIN, ALERT_TONE_HZ);
                Serial.println(F("Phishing detected"));
                break;

            case '0':
                noTone(ALERT_BUZZER_PIN);
                digitalWrite(ALERT_BUZZER_PIN, LOW);
                digitalWrite(RED_LED_PIN, LOW);
                digitalWrite(GREEN_LED_PIN, HIGH);
                Serial.println(F("Safe link"));
                break;

            default:
                // Ignore line endings and unrelated characters.
                break;
        }
    }
}
