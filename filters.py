import cv2
import numpy as np


class MirrorFilterPipe:
    @staticmethod
    def process(frame):
        return cv2.flip(frame, 1)


class FishEyeFilterPipe:
    @staticmethod
    def process(frame):
        height, width = frame.shape[:2]
        center = (width // 2, height // 2)

        fisheye_frame = np.zeros((height, width, 3), dtype=np.uint8)

        distortion_factor = 4

        for y in range(height):
            for x in range(width):
                x_normalized = (x - center[0]) / center[0]
                y_normalized = (y - center[1]) / center[1]

                radius = np.sqrt(x_normalized**2 + y_normalized**2)

                if radius <= 1.0:
                    r = radius ** distortion_factor
                    x_distorted = int(center[0] + r * center[0] * x_normalized)
                    y_distorted = int(center[1] + r * center[1] * y_normalized)

                    if 0 <= x_distorted < width and 0 <= y_distorted < height:
                        fisheye_frame[y, x] = frame[y_distorted, x_distorted]

        mask = np.zeros((height, width), dtype=np.uint8)
        cv2.circle(mask, center, min(center), (255), thickness=-1)

        fisheye_frame = cv2.bitwise_and(fisheye_frame, fisheye_frame, mask=mask)

        return fisheye_frame
