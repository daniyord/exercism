class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = []

    def read(self):
        if len(self.store) == 0:
            raise BufferEmptyException("Circular buffer is empty")

        return self.store.pop(0)

    def write(self, data):
        if len(self.store) == self.capacity:
            raise BufferFullException("Circular buffer is full")

        self.store.append(data)

    def overwrite(self, data):
        if len(self.store) == self.capacity:
            self.store.pop(0)

        self.store.append(data)

    def clear(self):
        self.store.clear()
