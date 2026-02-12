#!/usr/bin/env python3
"""
Contrôle de 3 LEDs
Cours 243-413-SH, Semaine 2
"""
import RPi.GPIO as GPIO
import time

# Configuration des broches
LED_ROUGE = 17 # Pin 11
LED_VERTE = 27 # Pin 13
LED_JAUNE = 22 # Pin 15

# Initialisation
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_ROUGE, GPIO.OUT)
GPIO.setup(LED_VERTE, GPIO.OUT)
GPIO.setup(LED_JAUNE, GPIO.OUT)

# Éteindre toutes les LEDs au démarrage
GPIO.output(LED_ROUGE, GPIO.LOW)
GPIO.output(LED_VERTE, GPIO.LOW)
GPIO.output(LED_JAUNE, GPIO.LOW)

def allumer(led):
    """Allume une LED spécifique"""
    GPIO.output(led, GPIO.HIGH)

def eteindre(led):
    """Éteint une LED spécifique"""
    GPIO.output(led, GPIO.LOW)

def sequence_chenillard():
    """Effet chenillard sur les 3 LEDs"""
    leds = [LED_ROUGE, LED_VERTE, LED_JAUNE]
    noms = {LED_ROUGE: "Rouge", LED_VERTE: "Verte", LED_JAUNE: "Jaune"}
    for _ in range(3): # 3 tours complets
        for led in leds:
            allumer(led)
            print(f"LED {noms[led]} allumée")
            time.sleep(0.5)
            eteindre(led)
try:
    print("=== Démo LEDs RGB ===")
    print("Test individuel...")
    # Test individuel
    for led, nom in [(LED_ROUGE, "Rouge"), (LED_VERTE, "Verte"), (LED_JAUNE, "Jaune")]:
        print(f"Test LED {nom}")
        allumer(led)
        time.sleep(1)
        eteindre(led)
        time.sleep(0.5)

    print("\nEffet chenillard...")
    sequence_chenillard()
    print("\n=== Fin de la démo ===")
except KeyboardInterrupt:
    print("\nArrêt demandé")
finally:
    GPIO.cleanup()
    print("GPIO nettoyé !")