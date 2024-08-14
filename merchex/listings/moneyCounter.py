import cv2
import cvzone
import numpy as np
from cvzone.ColorModule import ColorFinder

# Replace the URL with the one provided by your IP webcam app
url = 'http://192.168.0.144:4747/video'

cap = cv2.VideoCapture(url)
cap.set(3, 640)
cap.set(4, 480)
myColorFinder = ColorFinder(False)
# Custom Orange Color
hsvVals = {'hmin': 22, 'smin': 42, 'vmin': 158, 'hmax': 129, 'smax': 177, 'vmax': 255}

def empty(a):
    pass

cv2.namedWindow("Settings")
cv2.resizeWindow("Settings", 640, 240)
cv2.createTrackbar("Threshold1", "Settings", 219, 255, empty)
cv2.createTrackbar("Threshold2", "Settings", 233, 255, empty)

def preProcessing(img):
    imgPre = cv2.GaussianBlur(img, (9, 9), 3)
    thresh1 = cv2.getTrackbarPos("Threshold1", "Settings")
    thresh2 = cv2.getTrackbarPos("Threshold2", "Settings")
    imgPre = cv2.Canny(imgPre, thresh1, thresh2)
    kernel = np.ones((3, 3), np.uint8)
    imgPre = cv2.dilate(imgPre, kernel, iterations=1)
    imgPre = cv2.morphologyEx(imgPre, cv2.MORPH_CLOSE, kernel)
    return imgPre

while True:
    success, img = cap.read()
    imgPre = preProcessing(img)
    imgContours, conFound = cvzone.findContours(img, imgPre, minArea=20)
    totalMoney = 0


    if conFound:
        for count, contour in enumerate(conFound):
            peri = cv2.arcLength(contour['cnt'], True)
            approx = cv2.approxPolyDP(contour['cnt'], 0.02 * peri, True)
            if len(approx) > 5:
                area = contour['area']
                x, y, w, h = contour['bbox']
                imgCrop = img[y:y + h, x:x + w]
                #cv2.imshow('Cropped Image', imgCrop)  # Use a single window for cropped images
                imgColor, mask = myColorFinder.update(imgCrop, hsvVals)
                whitePixelCount = cv2.countNonZero(mask)
                #print(f"Contour {count} area: {area}, white pixel count: {whitePixelCount}")

                if 13000 < area < 16000:
                    # 1dh or 0.2dh
                    if whitePixelCount > 20:
                        totalMoney += 0.2
                    else:
                        totalMoney += 1

                elif 16000 <= area < 19000:
                    # 5dh or 2dh
                    if whitePixelCount >20:
                        totalMoney += 5
                    else:
                        totalMoney+=2
                elif area >= 19000 and whitePixelCount>20:
                    totalMoney += 10
                elif area <= 13000:
                    # 0.1 or 0.5
                    if whitePixelCount >20:
                        totalMoney += 0.1
                    else:
                        totalMoney += 0.5
                else:
                    totalMoney += 0
            else:
                print(" ")
    else:
        print(" ")

    imgStacked = cvzone.stackImages([img, imgPre, imgContours], 2, 1)
    cvzone.putTextRect(imgStacked, f'Total = {totalMoney} DH', (50, 50))

    # Resize the stacked image
    imgStacked = cv2.resize(imgStacked, (640, 480))
    cv2.imshow("Image", imgStacked)
    #cv2.imshow("Image Color", imgColor)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
