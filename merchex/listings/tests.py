import cv2
import numpy as np
import face_recognition
import os

# Load images from the database (folder path)
path = 'media/images_admins'
images = []
classNames = []
personsList = os.listdir(path)

# Load and store images and corresponding class names
for cl in personsList:
    curPersonn = cv2.imread(f'{path}/{cl}')
    images.append(curPersonn)
    classNames.append(os.path.splitext(cl)[0])

# Function to encode images
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

# Encode known images
encodeListKnown = findEncodings(images)
print('Encoding Complete')

# Function to compare a given image to the known database
def compare_image_to_database(image_path):
    # Load the image taken from the browser
    img = cv2.imread(image_path)
    
    # Resize the image and convert to RGB
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # Find face locations and encodings in the image
    faceCurentFrame = face_recognition.face_locations(imgS)
    encodeCurentFrame = face_recognition.face_encodings(imgS, faceCurentFrame)

    # If no face is detected, return False
    if not encodeCurentFrame:
        return False

    # Compare the detected face to known encodings
    for encodeFace in encodeCurentFrame:
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        # Find the best match index
        matchIndex = np.argmin(faceDis)

        # Return True if a match is found
        if matches[matchIndex]:
            return True
            

    return False




 if not compare_image_to_database():
            # If image verification fails, add an error message
            print("face not reconized")
            