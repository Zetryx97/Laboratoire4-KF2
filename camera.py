#Gabriel Lessard - Samy Tétrault - Guillaume Légaré
#Laboratoire 4 KF2

import cv2
import numpy as np
from time import sleep
from deplacement_robot import Moteur


class Caméra:

    global PORT_CAMERA
    PORT_CAMERA = 0
    CADRAN_1_MIN = 0
    CADRAN_1_MAX = 106
    CADRAN_2_MIN = 107
    CADRAN_2_MAX = 212
    CADRAN_3_MIN = 213
    CADRAN_3_MAX = 319
    def __init__(self):
        self.vcap = cv2.VideoCapture(PORT_CAMERA)
        self.est_en_marche = True
        self.position_object = None
    
    def set_resolution_camera(self):
        self.vcap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
        self.vcap.set(cv2.CAP_PROP_FRAME_HEIGHT,240) 

    def detecter_orange(self):
        self.set_resolution_camera()
        while True:
            ok,image = self.vcap.read()
            if not ok:
                print("Erreur avec l'image")
                break
            #19,120,255,110,255,20
            imgae_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            image_binary = cv2.inRange(imgae_hsv, (19, 120, 110), (20, 255, 255))
            contours, _ = cv2.findContours(image_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            val_plus_grand_contour = 0
            position_plus_grand_contour = 0
            for c in contours:
                x, y, l, h = cv2.boundingRect(c)
                air_rect = l * h
                if(air_rect > val_plus_grand_contour):
                    val_plus_grand_contour = air_rect
                    position_plus_grand_contour = x

            if(position_plus_grand_contour < self.CADRAN_2_MIN):
                self.position_object = 'gauche'
            elif(position_plus_grand_contour > self.CADRAN_2_MAX):
                self.position_object = 'droite'
            elif(self.CADRAN_2_MIN < position_plus_grand_contour and position_plus_grand_contour < self.CADRAN_2_MAX):
                self.position_object = 'millieu'

            image_contour = cv2.drawContours(image_binary, contours, -1, (175, 175, 175), 3)
            cv2.imshow("Caméra", image_contour)
            choix = cv2.waitKey(33)

            if choix == ord('q'):
                self.est_en_marche = False
                break 
            
        self.vcap.release()
        cv2.destroyAllWindows()
    

    def convertir_image(self):
        return None
    
    

if __name__ == "__main__":
    cam = Caméra()

    cam.detecter_orange()

    