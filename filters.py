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


class TileAverageFilterPipe:
    @staticmethod
    def process(frame, num_tiles_x=10, num_tiles_y=10):
        height, width = frame.shape[:2]

        tile_width = width // num_tiles_x
        tile_height = height // num_tiles_y

        output_frame = np.zeros_like(frame)

        for i in range(num_tiles_y):
            for j in range(num_tiles_x):
                y1 = i * tile_height
                y2 = (i + 1) * tile_height if (i + 1) * tile_height <= height else height
                x1 = j * tile_width
                x2 = (j + 1) * tile_width if (j + 1) * tile_width <= width else width

                tile = frame[y1:y2, x1:x2]

                average_color = cv2.mean(tile)[:3]

                output_frame[y1:y2, x1:x2] = average_color

        return output_frame
