import cv2
import time
camera = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

while True:
    success, frame = camera.read()

    if not success or frame is None:
        break

    detectou_sorriso = False
    detectou_olhos = False

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100, 100)
    )
    for (x, y, w, h) in faces:
        eyes_region_gray = gray[y:y + h // 2, x:x + w]   	
        face_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) 
    

    
    

    if not detectou_sorriso:
        print("Sorrisos? Nada ainda?")
    elif not detectou_olhos: 
        print("Olhos? Nada ainda???")
    else: 
        frame = gray 
    cv2.imshow("Visão Computacional em Python !! :D ", frame)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()