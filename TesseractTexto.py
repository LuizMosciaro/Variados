import pytesseract as ps
import cv2
#Essa linha faz ter autorização ao aplicativo tesseract.exe
ps.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"

#lendo a imagem
imagem = cv2.imread(r'C:\Users\supor\Downloads\texto2.png')

#convertendo de BLUEGREENRED para RED GREEN BLUE
imagem_rgb = cv2.cvtColor(imagem,cv2.COLOR_BGR2RGB)

#convertendo de RGB pra Cinza
imagem_gray = cv2.cvtColor(imagem_rgb,cv2.COLOR_RGB2GRAY)

#cv2.imshow("Thresh",imagem_gray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#chamando a leitura
resultado1 = ps.image_to_string(imagem_rgb)
print(resultado1)

img_poema = cv2.imread(r'C:\Users\supor\Downloads\poema.png')
resultado2 = ps.image_to_string(img_poema)
print(resultado2)



