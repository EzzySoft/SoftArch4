import cv2

class DisplayPipe:
    def __init__(self, window_name):
        self.window_name = window_name

    def display(self, frame):
        cv2.imshow(self.window_name, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return False
        return True
    