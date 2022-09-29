#Gabriel Lessard - Samy Tétrault - Guillaume Légaré
#Laboratoire 4 KF2

import cv2
import numpy as np
from time import sleep
from deplacement_robot import Moteur


class Caméra:

    global PORT_CAMERA
    PORT_CAMERA = 0
    def __init__(self):
        self.vcap = cv2.VideoCapture(PORT_CAMERA)
    
    def set_resolution_camera(self):
        self.vcap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
        self.vcap.set(cv2.CAP_PROP_FRAME_HEIGHT,240) 

    def captuer_image(self):
        self.set_resolution_camera()

        while True:
            ok,image = self.vcap.read()
            if not ok:
                print("Erreur avec l'image")
                break
       
            cv2.imshow("Caméra", image)
            choix = cv2.waitKey(33)

            if choix == ord('q'):
                break 
            
        self.vcap.release()
        cv2.destroyAllWindows()
    

    def convertir_image(self):
        return None
    
    

if __name__ == "__main__":
    cam = Caméra()

    cam.captuer_image()

    