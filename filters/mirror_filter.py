import cv2
from pipeline import Pipe

class MirrorFilterPipe(Pipe):
    def process(self, frame):
        if frame is None or frame.size == 0:
            return None
        mirrored_frame = cv2.flip(frame, 1)
        return mirrored_frame