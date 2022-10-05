#Gabriel Lessard - Samy Tétrault - Guillaume Légaré
#Laboratoire 4 KF2

import cv2
import numpy as np
from time import sleep
from deplacement_robot import Moteur
from camera import Caméra
import threading

class Detecteur_Orange:
    def __init__(self):
        self.camera = Caméra()
        self.moteur = Moteur()
        
    def activer_robot(self):
        th_detecteur_robot = threading.Thread(target=self.camera.detecter_orange)
        th_deplacement_robot = threading.Thread(target=self.mouvement)
        th_detecteur_robot.start()
        th_deplacement_robot.start()

    def mouvement(self):
        while self.camera.est_en_marche:
            # Temps d'attente élever pour permettre à la caméra de detecter l'image
            sleep(3)
            if self.camera.position_object == 'gauche':
                self.moteur.tourner_gauche(0.1)
            elif self.camera.position_object == 'droite':
                self.moteur.tourner_droite(0.1)
            else:
                self.moteur.avancer(0.5)
            sleep(0.5)
            self.moteur.freiner()


if __name__ == "__main__":
    robot_detecteur_orange = Detecteur_Orange()
    robot_detecteur_orange.activer_robot()