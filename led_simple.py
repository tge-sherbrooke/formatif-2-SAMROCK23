#!/usr/bin/env python3
"""
Contrôle simple d'une LED
Cours 243-413-SH, Semaine 2
"""
import RPi.GPIO as GPIO
import time
# Configuration
LED_PIN = 17 # GPIO 17 = Pin 11
# Initialisation
GPIO.setmode(GPIO.BCM) # Utiliser les numéros GPIO (BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
print("Contrôle de LED - Ctrl+C pour quitter")
try:
    # Allumer la LED
    print("LED allumée")
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(2)
    # Éteindre la LED
    print("LED éteinte")
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(2)
    # Faire clignoter 5 fois
    for i in range(5):
        print(f"Clignotement {i+1}/5")
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nArrêt demandé par l'utilisateur")
finally:
    # Nettoyage (toujours important !)
    GPIO.cleanup()
    print("GPIO nettoyé, au revoir !")