const int trigPin = 11;
const int echoPin = 12;
long durasi;
int jarak;

void setup() {
  pinMode(trigPin, OUTPUT); 
  pinMode(echoPin, INPUT); 
  Serial.begin(9600); 
}

void loop() {
  // Membersihkan trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Mengirim sinyal 10 mikrodetik
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Membaca waktu pantulan
  durasi = pulseIn(echoPin, HIGH);

  // Menghitung jarak (cm)
  jarak = durasi * 0.034 / 2;

  Serial.print("Jarak Benda: ");
  Serial.print(jarak);
  Serial.println(" cm");
  
  delay(200);
}