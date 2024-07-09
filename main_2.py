import cv2
import cvzone
import numpy as np
# Replace the URL with the one provided by your IP webcam app
url = 'http://192.168.82.37:4747/video'

cap = cv2.VideoCapture(url)


def empty(a):
    pass


cv2.namedWindow("Settings")
cv2.resizeWindow("Settings", 640, 240)
cv2.createTrackbar("Threshold1", "Settings", 50, 255, empty)
cv2.createTrackbar("Threshold2", "Settings", 100, 255, empty)
cv2.createTrackbar("CropX", "Settings", 0, 640, empty)
cv2.createTrackbar("CropY", "Settings", 0, 480, empty)
cv2.createTrackbar("CropWidth", "Settings", 100, 640, empty)
cv2.createTrackbar("CropHeight", "Settings", 100, 480, empty)


def preProcessing(img):
    imgPre = cv2.GaussianBlur(img, (9, 9), 3)
    thresh1 = cv2.getTrackbarPos("Threshold1", "Settings")
    thresh2 = cv2.getTrackbarPos("Threshold2", "Settings")
    imgPre = cv2.Canny(imgPre, thresh1, thresh2)
    kernel = np.ones((3, 3), np.uint8)  # Adjusted kernel size and dtype
    imgPre = cv2.dilate(imgPre, kernel, iterations=1)
    imgPre=cv2.morphologyEx(imgPre,cv2.MORPH_CLOSE,kernel)
    imgContours, conFound = cvzone.findContours(img, imgPre, minArea=20)
    return imgPre, imgContours  # Return imgPre and imgContours


    return imgPre


while True:
    success, img = cap.read()
    if not success:
        break

    crop_x = cv2.getTrackbarPos("CropX", "Settings")
    crop_y = cv2.getTrackbarPos("CropY", "Settings")
    crop_width = cv2.getTrackbarPos("CropWidth", "Settings")
    crop_height = cv2.getTrackbarPos("CropHeight", "Settings")

    # Ensure the crop rectangle is within the image bounds
    crop_x = min(crop_x, img.shape[1] - 1)
    crop_y = min(crop_y, img.shape[0] - 1)
    crop_width = min(crop_width, img.shape[1] - crop_x)
    crop_height = min(crop_height, img.shape[0] - crop_y)

    img_cropped = img[crop_y:crop_y + crop_height, crop_x:crop_x + crop_width]

    # Process the cropped image
    imgPre, imgContours = preProcessing(img_cropped)



    # Convert imgPre to BGR for concatenation with img_cropped
    imgPreBGR = cv2.cvtColor(imgPre, cv2.COLOR_GRAY2BGR)

    # Display original image, cropped, processed images, and contours together
    combined_img = np.hstack((img_cropped, imgPreBGR, imgContours))

    cv2.imshow("Combined Images", combined_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()