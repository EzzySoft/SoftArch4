import cv2


class MirrorFilterPipe:
    @staticmethod
    def process(frame):
        return cv2.flip(frame, 1)


class FishEyeEffect:
    @staticmethod
    def process(frame):
        return cv2.warpPolar(frame, (frame.shape[1], frame.shape[0]),
                             (frame.shape[1] // 2, frame.shape[0] // 2),
                             frame.shape[1] // 2, cv2.WARP_POLAR_LINEAR)
