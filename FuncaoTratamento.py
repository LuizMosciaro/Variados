import pytesseract as ps
import cv2
import numpy as np
from PIL import Image
from PIL import ImageFilter
import os

def tratamento():
    ps.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"
    pasta_origem = r"C:\Users\supor\PycharmProjects\pythonProject\screenshots"
    pasta_saida = r"C:\Users\supor\PycharmProjects\pythonProject\tratadas"

    for imagePath in os.listdir(pasta_origem):
        inputPath = os.path.join(pasta_origem, imagePath)
        fullOutPath = os.path.join(pasta_saida, 'tratada_' + imagePath)
        imagem = cv2.imread(inputPath)
        imagem2 = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        imagem3 = cv2.medianBlur(imagem2, 5)  # blur/suavizar (0 até 5)
        _, imagem4 = cv2.threshold(imagem3, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        kernel = np.ones((2, 2), np.uint8)
        erosion = cv2.erode(imagem4, kernel, iterations=1)
        dilation = cv2.dilate(erosion, kernel, iterations=1)
        opening = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)

        cv2.imwrite(fullOutPath, opening)





if __name__ == '__main__':
    tratamento()


