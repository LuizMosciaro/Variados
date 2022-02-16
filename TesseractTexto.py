import pytesseract as ps
import cv2
ps.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"

img = cv2.imread(r"C:\Users\supor\Downloads\texto-notepad.png") #ler
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converter cinza
img2 = cv2.medianBlur(img1,1) #blur/suavizar (0 até 5)
_,img3 = cv2.threshold(img2,0,255,cv2.THRESH_BINARY +  cv2.THRESH_OTSU)

cv2.imshow("Imagem",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

r = ps.image_to_string(img3)
print(r)
