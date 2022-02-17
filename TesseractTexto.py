import pytesseract as ps
import cv2
import numpy as np
ps.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"

img = cv2.imread(r"C:\Users\supor\PycharmProjects\pythonProject\screenshots\3.png") #ler
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converter cinza
img2 = cv2.medianBlur(img1,3) #blur/suavizar (0 até 5)
_,img3 = cv2.threshold(img2,0,255,cv2.THRESH_BINARY+  cv2.THRESH_OTSU)

kernel = np.ones((2,2),np.uint8)
erosion = cv2.erode(img3,kernel,iterations = 1)
dilation = cv2.dilate(erosion,kernel,iterations = 1)
opening = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
#diminuir_largura = 300
#diminuir_altura = 500
#diminuicao = (diminuir_largura,diminuir_altura)
#img_diminuida = cv2.resize(img3,diminuicao,interpolation=cv2.INTER_LINEAR)

my_config = r"--psm 11 --oem 3"
r = ps.image_to_string(opening,config=my_config)
print(r)

cv2.imshow("Imagem",opening)
cv2.waitKey(0)
cv2.destroyAllWindows()



