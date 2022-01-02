import cv2
import os

path = "images" 
imgWidth = 100      
imgHeight = 100

#bilgisayar kamerasindan goruntu aliyoruz. cap.set ile kameranin boyutlarini ve parlakliğini ayarliyoruz.
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,180)

#videodan alacağımız goruntuleri tutacağimiz klasörü olusturma
global countFolder
def saveDataFunc():
    global countFolder
    countFolder = 0
    while os.path.exists(path + str(countFolder)):
        countFolder += 1
    os.makedirs(path + str(countFolder))
saveDataFunc()    

#klasöre görüntüleri kaydetme
count = 0
countSave = 0
while True:
    success,img = cap.read()
    if success:
        img = cv2.resize(img,(imgWidth,imgHeight)) #yakalanan görüntüyü yeniden boyutlandiriyoruz
        #her 5 resimdem sadece birini depolamak için, hepsine gerek yok
        if count % 5 == 0:
            cv2.imwrite(path + str(countFolder) + "/" + str(countSave) + "_" + ".png",img)
            countSave += 1
            print(countSave)
        count += 1
        cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord("q"): break
cap.release()
cv2.destroyAllWindows()   
