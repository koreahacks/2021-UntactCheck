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
            roi_gray=image_gray[y:y+h, x:x+w]
            roi_color=image[y:y+h, x:x+w]
            if (w > 240 or h > 240):
                fr = 2000
                du = 1000
                sd.Beep(fr, du)
                cv2.rectangle(image, (x, y), (x + w, y + h), (61,61,204), 2)
            else:
                cv2.rectangle(image, (x, y), (x + w, y + h), (127,229,134), 2)

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')