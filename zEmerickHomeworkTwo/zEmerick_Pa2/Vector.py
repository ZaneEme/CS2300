class Vector:
    def __init__(self, start=None, end=None):
        # Declare Vector endpoints
        self.startPoint = [0, 0]
        self.endPoint = [0, 0]

        # Defaults
        if start is None:
            start = [0, 0]
        if end is None:
            end == [2, 2]
        else:
            self.startPoint[0] = start[0]
            self.startPoint[1] = start[1]
            self.endPoint[0] = end[0]
            self.endPoint[1] = end[1]

        self.slope = (self.endPoint[1] - self.startPoint[1]) / (
            self.endPoint[0] - self.startPoint[0]
        )

        self.midpoint = [
            (self.startPoint[0] + self.endPoint[0]) / 2,
            (self.startPoint[1] + self.endPoint[1]) / 2,
        ]
