from capture import VideoCapturePipe
from display import DisplayPipe
from filters.fisheye_filter import FishEyeFilterPipe
from filters.mirror_filter import MirrorFilterPipe
from filters.tileaverage_filter import TileAverageFilterPipe


class VideoProcessingPipeline:
    def __init__(self):
        self.capture_pipe = VideoCapturePipe()

        self.mirror_filter = MirrorFilterPipe()
        self.fisheye_filter = FishEyeFilterPipe()
        self.tile_filter = TileAverageFilterPipe()

        self.original_display = DisplayPipe('Original Video')
        self.mirrored_display = DisplayPipe('Mirrored Video')
        self.fisheye_display = DisplayPipe('FishEye Video')
        self.tile_display = DisplayPipe('Tile Video')
        self.combined_display = DisplayPipe('Combined Filter Output')
        self.pixelated_display = DisplayPipe('Pixelated Output')

        self.connect_pipes()

    def connect_pipes(self):
        self.capture_pipe.set_next(self.original_display)
        self.original_display.set_next(self.mirror_filter)
        self.mirror_filter.set_next(self.mirrored_display)

        self.mirror_filter.set_next(self.fisheye_filter)
        self.fisheye_filter.set_next(self.fisheye_display)

        self.fisheye_filter.set_next(self.tile_filter)
        self.tile_filter.set_next(self.tile_display)

        self.tile_filter.set_next(self.combined_display)

        self.tile_filter.set_next(self.pixelated_display)

    def run(self):
        while True:
            frame = self.capture_pipe.capture()
            if frame is None:
                break

            self.capture_pipe.process(frame)

            mirrored_frame = self.mirror_filter.process(frame)
            if mirrored_frame is not None:
                fisheye_frame = self.fisheye_filter.process(mirrored_frame)
                if fisheye_frame is not None:
                    self.combined_display.process(fisheye_frame)

            tile_frame = self.tile_filter.process(frame)
            if tile_frame is not None:
                self.tile_display.process(tile_frame)

            fisheye_frame = self.fisheye_filter.process(frame)
            if fisheye_frame is not None:
                self.fisheye_display.process(fisheye_frame)

            mirrored_frame = self.mirror_filter.process(frame)
            if mirrored_frame is not None:
                self.mirrored_display.process(mirrored_frame)

        self.capture_pipe.release()


if __name__ == "__main__":
    pipeline = VideoProcessingPipeline()
    pipeline.run()