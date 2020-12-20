import cv2
import numpy as np
from playsound import playsound

print("What do you wanna be?\n")
print("1:Happy Smiley \n2:Angry Smiley\n3:Harry Potter\n4:Hagrid\n5:Phineas\n6:Ferb\n")
val=input("Enter the no correspoding to the character you wanna be!  :  ")
printf("\nPress 'q' to quit")


face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml') 
replace=cv2.imread(val+'.png')

cap= cv2.VideoCapture(0)

while True:
   
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    
    for (x,y,w,h) in faces:
        
        m=img[y:y+h,x:x+w]
        replace1=cv2.resize(replace,(w,h), interpolation = cv2.INTER_CUBIC)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        a,b,c=replace1.shape
     
             
        img[y:y+h,x:x+w]=replace1
     
    cv2.imshow('img',img)
  
   
    if cv2.waitKey(30) == ord('q')  :
        break
  

cap.release()
cv2.destroyAllWindows()


 
