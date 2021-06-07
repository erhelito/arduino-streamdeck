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
    boutons();
    fonct_volume();

    Serial.flush();

    delay(100);
}

void boutons() {
    pause = digitalRead(pausePin);
    suivant = digitalRead(suivantPin);
    precedent = digitalRead(precedentPin);

    if (pause == 1) {        
        Serial.print(1);
    }

    else {
        Serial.print(0);
    }


    if (suivant == 1) {        
        Serial.print(1);
    }

    else {
        Serial.print(0);
    }


    if (precedent == 1) {        
        Serial.print(1);
    }

    else {
        Serial.print(0);
    }
}

void fonct_volume() {
    volume = analogRead(potentiometrePin);
    volume = map(volume, 0, 1023, 0, 100);

    if (volume < 10) {
        Serial.print("0");
        Serial.print("0");
        Serial.println(volume);
    }

    else if (volume < 100) {
        Serial.print("0");
        Serial.println(volume);
    }

    else {
        Serial.println(volume);
    }
}