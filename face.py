from cvzone.FaceDetectionModule import FaceDetector

import cv2

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16) 


cap = cv2.VideoCapture(0)
detector = FaceDetector()

position=90
b=5
kit.servo[0].angle = position   
while True:
    success, img = cap.read()
    img=cv2.flip(img,-1)
    img=cv2.flip(img,1)
    
    img, bboxs = detector.findFaces(img)
#    kit.servo[0].angle = position  
    if bboxs:
        # bboxInfo - "id","bbox","score","center"
       
        center1 = bboxs[0]["center"]
        x_medium=center1[0]
       
        a=x_medium//62
        print(a)
        if 5 < a < 20:
            position+=1.5
        elif 1 < a < 4:
            position-=1.5
        print(position)
        kit.servo[0].angle = position    
        
        
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
       
cap.release()

cv2.destroyAllWindows()