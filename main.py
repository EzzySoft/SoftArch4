from capture import VideoCapturePipe
from filters import MirrorFilterPipe
from display import DisplayPipe

def video_processing_pipeline():
    capture_pipe = VideoCapturePipe()
    mirror_filter = MirrorFilterPipe()
    mirrored_display_pipe = DisplayPipe('Mirrored Video')
    original_display_pipe = DisplayPipe('Original Video')

    while True:
        frame = capture_pipe.capture()
        if frame is None:
            break

        mirrored_frame = mirror_filter.process(frame)

        if not original_display_pipe.display(frame) or not mirrored_display_pipe.display(mirrored_frame):
            break

    capture_pipe.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_processing_pipeline()
