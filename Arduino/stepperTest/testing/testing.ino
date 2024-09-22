String x;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void  loop() {
  if (Serial.available());
  x = Serial.readString();
  x.trim();
  Serial.print(x);
}