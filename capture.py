import cv2


class VideoCapturePipe:
    def __init__(self, source=0):
        self.cap = cv2.VideoCapture(source)

    def capture(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def release(self):
        self.cap.release()
