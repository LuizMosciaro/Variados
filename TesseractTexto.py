import pytesseract as ps
import cv2
ps.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"

img = cv2.imread(r"C:\Users\supor\Downloads\poema3.jpg") #ler
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converter cinza
img2 = cv2.medianBlur(img1,1) #blur/suavizar (0 até 5)
_,img3 = cv2.threshold(img2,1,255,cv2.THRESH_BINARY +  cv2.THRESH_OTSU)

diminuir_largura = 300
diminuir_altura = 500
diminuicao = (diminuir_largura,diminuir_altura)
img_diminuida = cv2.resize(img3,diminuicao,interpolation=cv2.INTER_LINEAR)
cv2.imshow("Imagem",img_diminuida)
cv2.waitKey(0)
cv2.destroyAllWindows()

my_config = r"--psm 11 --oem 3"
r = ps.image_to_string(img3,config=my_config)
print(r)

