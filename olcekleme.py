import cv2, os

def resim_olcekle():
    resim_nu = 1
    for klasor in ['p']:
        for resim_list in os.listdir(klasor):
            try:
                resim_adresi= str(klasor)+ "/" + str(resim_list)
                resim = cv2.imread(resim_adresi)
                yeniden_olcekle= cv2.resize(resim, (100,100))
                cv2.imwrite("p/"+str(resim_nu)+"_"+ ".jpg", yeniden_olcekle)
                resim_nu +=1
            except Exception as e:
                print(str(e))
resim_olcekle()                