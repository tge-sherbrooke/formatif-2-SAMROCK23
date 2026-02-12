#!/usr/bin/env python3
"""
Lecture du capteur DHT22 - Température et Humidité
Cours 243-413-SH, Semaine 2
IMPORTANT: Le DHT22 utilise le protocole one-wire sur GPIO 4, PAS I²C !
Il n'apparaît pas dans i2cdetect.
"""

import time
import board
import adafruit_dht

# Configuration du capteur DHT22 sur GPIO 4 (Pin 7)
# ATTENTION: board.D4 = GPIO 4 = Pin 7 (pas Pin 4 !)
dht = adafruit_dht.DHT22(board.D4)

print("=== Capteur DHT22 ===")
print("Protocole: One-wire sur GPIO 4 (Pin 7)")
print("Note: Le DHT22 peut parfois échouer, c'est normal.")
print()

try:
    lectures_reussies = 0

    # Faire 5 tentatives de lecture
    for i in range(5):
        try:
            temperature = dht.temperature
            humidite = dht.humidity
            if temperature is not None and humidite is not None:
                print(f"Lecture {i+1}/5 :")
                print(f" Température : {temperature:.1f} °C")
                print(f" Humidité : {humidite:.1f} % RH")
                print()
                lectures_reussies += 1
            else:
                print(f"Lecture {i+1}/5 : Données invalides")
                print()
        except RuntimeError as e:
            # Le DHT22 peut parfois échouer à cause du timing
            print(f"Lecture {i+1}/5 : Erreur - {e}")
            print(" (Ceci est normal pour le DHT22, réessai...)")
            print()
            # Attendre 2.5 secondes entre les lectures
            # Le DHT22 ne peut être lu qu'une fois toutes les 2 secondes
        if i < 4:
            time.sleep(2.5)

        print("=== Résumé ===")
        print(f"Lectures réussies: {lectures_reussies}/5")

        if lectures_reussies == 0:
            print("\nAucune lecture réussie. Vérifiez:")
            print(" 1. Le câblage (VCC→Pin1, DATA→Pin7, GND→Pin6)")
            print(" 2. La résistance pull-up (10kΩ entre VCC et DATA)")
            print(" 3. L'alimentation du capteur")

except Exception as e:
    print(f"ERREUR CRITIQUE: {e}")
    print("\nVérifications:")
    print(" 1. Le capteur est-il bien connecté ?")
    print(" 2. Le fil DATA est-il sur GPIO 4 (Pin 7) ?")
    print(" 3. La bibliothèque adafruit-circuitpython-dht est-elle installée ?")
finally:
    dht.exit()
    print("\n=== Lecture terminée ===")