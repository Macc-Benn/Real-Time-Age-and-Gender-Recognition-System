import cv2
import Webcam

faceProto = "opencv_face_detector.pbtxt"
faceModel = "opencv_face_detector_uint8.pb"

faceNet = cv2.dnn.readNet(faceModel, faceProto)

url = "http://10.43.82.5:8080/shot.jpg"
video = cv2.VideoCapture(0)
video.open(url)

while True:
    check, frame = video.read()
    cv2.imshow("Age-Gender", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
