import cv2
import winsound as sd


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        faces=face_cascade.detectMultiScale(image_gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(image, (x,y),(x+w,y+h),(255,0,0),2)
            roi_gray=image_gray[y:y+h, x:x+w]
            roi_color=image[y:y+h, x:x+w]
            if (w > 260 or h > 260):
                fr = 2000
                du = 1000
                sd.Beep(fr, du)

        ret, jpeg = cv2.imencode('.jpg', image)

        return jpeg.tobytes()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')