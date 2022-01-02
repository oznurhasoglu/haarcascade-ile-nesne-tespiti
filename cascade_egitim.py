import cv2
 
objectName = "Kozalak"   
frameWidth = 280
frameHeight = 360
color = (255,0,0)        

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

def empty(a): pass


#multiScale fonksiyonunun parametrelerini kolayca degistirmek icin trackbar ekliyorum pencereye
cv2.namedWindow("Sonuc")
cv2.resizeWindow("Sonuc", frameWidth, frameHeight + 100)
cv2.createTrackbar("Scale", "Sonuc", 250, 1000, empty)
cv2.createTrackbar("Neighbor", "Sonuc", 3, 50, empty)

cascade = cv2.CascadeClassifier("cascade.xml")

while True:
    success, img = cap.read()
    if success:
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    
        #parametreler    
        scaleVal = 1 + (cv2.getTrackbarPos("Scale", "Sonuc")/1000)
        neighbor = cv2.getTrackbarPos("Neighbor", "Sonuc")
        #tespit
        rects = cascade.detectMultiScale(gray, scaleVal, neighbor)
        for (x,y,w,h) in rects:
            cv2.rectangle(img, (x,y),(x+w,y+h), color, 2)
            cv2.putText(img, objectName, (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
        cv2.imshow("Sonuc",img)
    if cv2.waitKey(1) & 0xFF == ord("q"): break    
