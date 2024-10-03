import cv2
from pipeline import Pipe

class VideoCapturePipe(Pipe):
    def __init__(self, source=0):
        super().__init__()
        self.cap = cv2.VideoCapture(source)

    def capture(self):
        ret, frame = self.cap.read()
        return frame if ret else None

    def process(self, frame):
        self.pass_data(frame)

    def release(self):
        self.cap.release()