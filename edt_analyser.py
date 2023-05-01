from PIL import Image
from pytesseract import pytesseract as t
import cv2
import numpy as np
import os

input_path = r""
output_path = r""

target_text = input("target text: ")

tpath = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
t.tesseract_cmd = tpath

def analyse(input_path, target_text):
    num = 0
    for image_path in os.listdir(input_path):
        num += 1
        image_path = os.path.join(input_path, image_path)
        
        img = cv2.imread(image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((1, 1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
        os.chdir(output_path)	
        cv2.imwrite("modified" + str(num ) + ".png", img)
        
        modified = Image.open(output_path + "\modified" + str(num) + ".png")

        #modified.show()
        text = t.image_to_string(img, config ='--oem 1 --psm 12')
        #print(text, sep= ' ')
        
        if target_text in text:
            print(image_path)
        else:
            print("No match")

analyse(input_path, target_text)
