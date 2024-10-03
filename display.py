import cv2
from pipeline import Pipe

class DisplayPipe(Pipe):
    def __init__(self, window_name):
        super().__init__()
        self.window_name = window_name

    def process(self, frame):
        cv2.imshow(self.window_name, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Shutting down...")
            exit(0)
        self.pass_data(frame)