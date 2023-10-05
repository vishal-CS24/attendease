import cv2
faceClassifier=cv2.CascadeClassifier("attendese\haarcascade_frontalface_default.xml")
def faceCroped(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceClassifier.detectMultiScale(gray,1.3,5)
    #scaling factor 1.3
    #min Neighbour 5
    for(x,y,w,h) in faces:
            faceCrop=img[y:y+h,x:x+w]
            return faceCrop

cap=cv2.VideoCapture(0)
while True:
    ret,frame1=cap.read()
    c=faceCroped(frame1)
    face=cv2.resize(c,(450,450))
    cv2.imshow("Cropped Face",face)
    if cv2.waitKey(1)==13:
                         break
cap.release()
cv2.destroyAllWindows()