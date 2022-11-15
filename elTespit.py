import cv2
from cvzone.HandTrackingModule import HandDetector
kamera = cv2.VideoCapture(0)
detector = HandDetector()

while True:
    ret,kare=kamera.read()
    kare=cv2.flip(kare,1)
    hands,kare=detector.findHands(kare,flipType=False)
    cv2.imshow("kamera",kare)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()