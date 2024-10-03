class Pipe:
    def __init__(self):
        self.next_pipe = None

    def set_next(self, next_pipe):
        self.next_pipe = next_pipe

    def process(self, data):
        raise NotImplementedError("Must be implemented by subclass")

    def pass_data(self, data):
        if self.next_pipe:
            self.next_pipe.process(data)