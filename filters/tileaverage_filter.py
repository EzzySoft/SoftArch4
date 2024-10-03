import cv2
import numpy as np
from pipeline import Pipe

class TileAverageFilterPipe(Pipe):
    @staticmethod
    def process(frame, num_tiles_x=10, num_tiles_y=10):
        if frame is None or frame.size == 0:
            return None
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
