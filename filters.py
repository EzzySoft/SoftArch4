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

        watermark_text = "SENSITIVE"
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 2
        font_color = (255, 255, 255)
        thickness = 3

        text_size = cv2.getTextSize(watermark_text, font, font_scale, thickness)[0]

        # Position text in the center
        text_x = (width - text_size[0]) // 2
        text_y = (height + text_size[1]) // 2

        cv2.putText(output_frame, watermark_text, (text_x, text_y), font, font_scale, font_color, thickness)

        return output_frame
