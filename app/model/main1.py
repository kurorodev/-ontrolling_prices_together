from pathlib import Path
from PIL import Image
import numpy as np
from ultralytics import YOLO
import cv2

im1 = Image.open('train/IMG_5746.jpg')

model = YOLO('best.pt')
res = model.predict(im1)  # results list
for r in res:
    img = np.copy(r.orig_img)
    img_name = Path(r.path).stem

    for ci,c in enumerate(r):
        label = c.names[c.boxes.cls.tolist().pop()]

        b_mask = np.zeros(img.shape[:2], np.uint8)

        # Create contour mask 
        keypoints = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(keypoints)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
        _ = cv2.drawContours(b_mask, [contours], -1, (255, 255, 255), cv2.FILLED)

        # OPTION-1: Isolate object with black background
        mask3ch = cv2.cvtColor(b_mask, cv2.COLOR_GRAY2BGR)
        isolated = cv2.bitwise_and(mask3ch, img)

        _ = cv2.imwrite(f'{img_name}_{label}-{ci}.png', iso_crop)
 
while True:
    print('Detect')
    for r in res:
        im_array = r.plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        im.show()  # show image
        im.save(f'results.jpg')  # save image