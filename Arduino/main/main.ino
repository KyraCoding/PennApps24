String x;

void setup() {
  Serial.begin(115200);
  pinMode(13, OUTPUT);
}

void  loop() {
  if (Serial.available()) {
    x = Serial.readString();
    x.trim();
    for (int i =0;i<x.length();i++) {
      char c = x[i];
      if (c == '0') {
        digitalWrite(13, LOW);
      } else if (c == '1') {
        digitalWrite(13, HIGH);
      }
      delay(10);
    }
    digitalWrite(13, LOW);
    Serial.print(x);
    Serial.flush();
  }
}