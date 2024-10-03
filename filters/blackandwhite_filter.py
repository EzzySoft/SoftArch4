import cv2
from pipeline import Pipe

class BlackAndWhiteFilterPipe(Pipe):
    def process(self, frame):
        if frame is None or frame.size == 0:
            return None
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        bw_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)
        return bw_frame