import cv2

from capture import VideoCapturePipe
from filters import MirrorFilterPipe, FishEyeFilterPipe, TileAverageFilterPipe
from display import DisplayPipe


def video_processing_pipeline():
    capture_pipe = VideoCapturePipe()
    mirror_filter = MirrorFilterPipe()
    fisheye_filter = FishEyeFilterPipe()
    tile_filter = TileAverageFilterPipe()

    mirrored_display_pipe = DisplayPipe('Mirrored Video')
    fisheye_display_pipe = DisplayPipe('FishEye Video')
    tile_display_pipe = DisplayPipe('Tile Video')
    original_display_pipe = DisplayPipe('Original Video')

    while True:
        frame = capture_pipe.capture()
        if frame is None:
            break

        mirrored_frame = mirror_filter.process(frame)
        fisheye_frame = fisheye_filter.process(frame)
        tile_frame = tile_filter.process(frame)

        if not original_display_pipe.display(frame) \
                or not mirrored_display_pipe.display(mirrored_frame) \
                or not fisheye_display_pipe.display(fisheye_frame) \
                or not tile_display_pipe.display(tile_frame):
            break

    capture_pipe.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video_processing_pipeline()
