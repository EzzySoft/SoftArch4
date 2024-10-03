import numpy as np
from pipeline import Pipe

class FishEyeFilterPipe(Pipe):
    def process(self, frame):
        if frame is None or frame.size == 0:
            return None
        height, width = frame.shape[:2]
        center = (width // 2, height // 2)

        y_indices, x_indices = np.indices((height, width))
        x_normalized = (x_indices - center[0]) / center[0]
        y_normalized = (y_indices - center[1]) / center[1]
        radius = np.sqrt(x_normalized ** 2 + y_normalized ** 2)
        mask = radius <= 1.0

        distortion_factor = 4
        r = radius[mask] ** distortion_factor

        x_distorted = np.clip((center[0] + r * center[0] * x_normalized[mask]).astype(int), 0, width - 1)
        y_distorted = np.clip((center[1] + r * center[1] * y_normalized[mask]).astype(int), 0, height - 1)

        fisheye_frame = np.zeros_like(frame)
        fisheye_frame[y_indices[mask], x_indices[mask]] = frame[y_distorted, x_distorted]

        return fisheye_frame
