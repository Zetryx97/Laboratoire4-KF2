import cv2
import numpy as np

def track_bar_cb(x):
    pass

vcap = cv2.VideoCapture(0)
if not vcap.isOpened():
    print("Impossible d'ouvrir la caméra")
    exit()

vcap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

titre_fenetre = "HSV Tester"
cv2.namedWindow(titre_fenetre)
cv2.createTrackbar('Teinte', titre_fenetre, 0, 360, track_bar_cb)
cv2.createTrackbar('Saturation min', titre_fenetre, 0,255, track_bar_cb)
cv2.createTrackbar('Saturation max', titre_fenetre, 0,255, track_bar_cb)
cv2.createTrackbar('Valeur min', titre_fenetre, 0, 255, track_bar_cb)
cv2.createTrackbar('Valeur max', titre_fenetre, 0, 255, track_bar_cb)
cv2.createTrackbar('Delta teinte', titre_fenetre, 0, 30, track_bar_cb)

teinte = cv2.getTrackbarPos('Teinte', titre_fenetre)
sat_min = cv2.getTrackbarPos('Saturation min', titre_fenetre)
sat_max = cv2.getTrackbarPos('Saturation max', titre_fenetre)
val_min = cv2.getTrackbarPos('Valeur min', titre_fenetre)
val_max = cv2.getTrackbarPos('Valeur max', titre_fenetre)
delta = cv2.getTrackbarPos('Delta teinte', titre_fenetre)

print(f"Pour quitter appuyer sur la touche 'q'.")

while True:    
    teinte_min = np.array([teinte - delta, sat_min, val_min])
    teinte_max = np.array([teinte + delta, sat_max, val_max])

    ret_sts, frame_bgr = vcap.read() 

    frame_hsv = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2HSV)
    frame_disc = cv2.inRange(frame_hsv, teinte_min, teinte_max)

    cv2.imshow("Image BGR", frame_bgr)
    cv2.imshow("HSV", frame_hsv)
    cv2.imshow("Image disc", frame_disc)

    choix = cv2.waitKey(125)
    if  choix == ord('q'):
        break    

    teinte = cv2.getTrackbarPos('Teinte', titre_fenetre)
    sat_min = cv2.getTrackbarPos('Saturation min', titre_fenetre)
    sat_max = cv2.getTrackbarPos('Saturation max', titre_fenetre)
    val_min = cv2.getTrackbarPos('Valeur min', titre_fenetre)
    val_max = cv2.getTrackbarPos('Valeur max', titre_fenetre)
    delta = cv2.getTrackbarPos('Delta teinte', titre_fenetre)

vcap.release()
cv2.destroyAllWindows()

print(f"Voilà")