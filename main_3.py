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
    kernel = np.ones((3, 3), np.uint8)
    imgPre = cv2.dilate(imgPre, kernel, iterations=1)
    imgPre = cv2.morphologyEx(imgPre, cv2.MORPH_CLOSE, kernel)
    imgContours, conFound = cv2.findContours(imgPre, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return imgPre, imgContours


def drawCircleAndSquare(img, contour):
    # Find the minimum enclosing circle
    (x, y), radius = cv2.minEnclosingCircle(contour)
    center = (int(x), int(y))
    radius = int(radius)

    # Draw the circle
    cv2.circle(img, center, radius, (0, 255, 0), 2)

    # Calculate square dimensions around the circle
    square_size = radius * 2
    x1 = int(x - radius)
    y1 = int(y - radius)
    x2 = x1 + square_size
    y2 = y1 + square_size

    # Draw the square
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Return center point for further use if needed
    return center


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

    if len(imgContours) > 0:
        # Iterate over contours found
        for contour in imgContours:
            center = drawCircleAndSquare(img_cropped, contour)
            print(f"Circle center: {center}")

    # Stack images horizontally
    stacked_img = np.hstack((img_cropped, cv2.cvtColor(imgPre, cv2.COLOR_GRAY2BGR)))

    # Display the stacked image
    cv2.imshow("Stacked Images", stacked_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
