int pause;
int suivant;
int precedent;

int val_potentiometre;
int volume;

const int pausePin = 3;
const int suivantPin = 2;
const int precedentPin = 4;

const int potentiometrePin = A0;

void setup() {
    pinMode(pausePin, INPUT);
    pinMode(suivantPin, INPUT);
    pinMode(precedentPin, INPUT);

    Serial.begin(9600);
}

void loop() {
    pause = digitalRead(pausePin);
    suivant = digitalRead(suivantPin);
    precedent = digitalRead(precedentPin);
    
    Serial.print(pause);
    Serial.print(suivant);
    Serial.print(precedent);

    volume = analogRead(potentiometrePin);
    volume = map(volume, 0, 1023, 0, 100);
    Serial.println(volume);

    Serial.flush();

    delay(100);
}