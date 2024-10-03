import cv2


class MirrorFilterPipe:
    @staticmethod
    def process(frame):
        return cv2.flip(frame, 1)
