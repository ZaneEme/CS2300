
from Board import Board
class Vector:
    
    def __init__(self, start = None, end = None):
        self.start = [0, 0]
        self.end = [0, 0]
        if start is None:
            start = [0,0]
        if end is None:
            end == [2, 2]
        else:
            self.start[0] = start[0]
            self.start[1] = start[1]
            self.end[0] = end[0]
            self.end[1] = end[1]

        self.slope = (end[1] - start[1]) / (end[0] - start[0])
        self.midpoint = [(self.start[0] + self.end[0]) / 2, (self.start[1] + self.end[1]) / 2]

