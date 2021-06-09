// initialisation des valeurs des trois boutons, et des broches sur lesquels ils sont branchés
int b1;
int b2;
int b3;

const int b1Pin = 3;
const int b2Pin = 2;
const int b3Pin = 4;

// initialisation des valeurs du potentiomètre, et de ses broches
int val_potentiometre;
int pourcentage;

const int potentiometrePin = A0;

void setup() {
    // déclaration des inputs et des outputs, et début de la liaison série
    pinMode(b1Pin, INPUT);
    pinMode(b2Pin, INPUT);
    pinMode(b3Pin, INPUT);

    Serial.begin(9600);
}

void loop() {
    // appel des fonctions boutons de pourcentage (pour traiter les données des différents boutons et du potentiomètre)
    boutons();
    fonct_pourcentage();

    // nettoyage du port série (obligatoire pour  un traitement depuis le programme python)
    Serial.flush();

    // delay pour ne pas surcharger le port série
    delay(100);
}

void boutons() {
    // lecture des valeurs des différents boutons, et affichage dans le port série
    b1 = digitalRead(b1Pin);
    b2 = digitalRead(b2Pin);
    b3 = digitalRead(b3Pin);

    if (b1 == 1) {        
        Serial.print(1);
    }

    else {
        Serial.print(0);
    }


    if (b2 == 1) {        
        Serial.print(1);
    }

    else {
        Serial.print(0);
    }


    if (b3 == 1) {        
        Serial.print(1);
    }

    else {
        Serial.print(0);
    }
}

void fonct_pourcentage() {
    // lecture de la valeur brute du potentiomètre
    pourcentage = analogRead(potentiometrePin);
    // passage en pourcentage (la fonction map fait un produit en croix)
    pourcentage = map(pourcentage, 0, 1023, 0, 100);

    // traitement des données du potentiomètre pour un meilleur affichage dans le port série
    // (affiche par exemple 004 au lieu de 4, ce qui empêche les bugs dans le traitement depuis le programme python)
    if (pourcentage < 10) {
        Serial.print("0");
        Serial.print("0");
        Serial.println(pourcentage);
    }

    else if (pourcentage < 100) {
        Serial.print("0");
        Serial.println(pourcentage);
    }

    else {
        Serial.println(pourcentage);
    }
}