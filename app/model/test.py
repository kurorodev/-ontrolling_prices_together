import cv2
import pytesseract
from ultralytics import YOLO
from PIL import Image, ImageEnhance
import numpy as np
from collections import Counter
import easyocr
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#pytesseract.pytesseract.tesseract_cmd = r'D:\yolo\hackt\tesseract\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
model = YOLO('best.pt')
reader = easyocr.Reader(["ru"])
def main(imgpath):
    inf = []
    def dominant_color(img):
        np_img = np.array(img)
        red, green, blue = np_img[:, :, 2], np_img[:, :, 1], np_img[:, :, 0]
        red_count, green_count, blue_count = np.sum(red), np.sum(green), np.sum(blue)
        max_color = max(red_count, green_count, blue_count)
        if (red_count > green_count * 1.20) and (red_count > blue_count * 1.20):
            return 1
        else:
            return 0

    
    image = cv2.imread(imgpath)
    results = model(image, conf=0.5, max_det=3)
    boxes = results[0].boxes
    redcount = 0
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        cropped_object = image[int(y1):int(y2), int(x1):int(x2)]
        #cv2.imwrite('cropped_object.jpg', cropped_object)
        redcount+=dominant_color(cropped_object)
        #cv2.imshow('Cropped Object', cropped_object)
        #cv2.waitKey(0)
        #data = (pytesseract.image_to_string(cropped_object, lang='rus+eng', config='--psm 13 --oem 1')).replace('\n', '')
        data = reader.readtext(cropped_object, detail=0, paragraph=False)
        print(data)
        inf.append(data)
    if redcount == 3:
        print('soc')
        inf.append(1)
    else:
        inf.append(0)
    return inf
print(main('train/IMG_5921.jpg'))