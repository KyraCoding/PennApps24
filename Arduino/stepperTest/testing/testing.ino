String x;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void  loop() {
  while (!Serial.available());
  x = Serial.readString();
  x.trim();
  if (x.length() > 0) {
    Serial.print(x);
  }
  
}