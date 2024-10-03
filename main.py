import cv2


class VideoCapturePipe:
    def __init__(self, source=0):
        self.cap = cv2.VideoCapture(source)

    def capture(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def release(self):
        self.cap.release()


class MirrorFilterPipe:
    @staticmethod
    def process(frame):
        return cv2.flip(frame, 1)


class DisplayPipe:
    def __init__(self, window_name):
        self.window_name = window_name

    def display(self, frame):
        cv2.imshow(self.window_name, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return False
        return True


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
