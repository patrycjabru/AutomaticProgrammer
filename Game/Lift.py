import json


class Lift:
    position: int
    liftedBlock: int

    def __init__(self, path):
        self.position = self.readInitPositionFromFile(path)
        self.liftedBlock = 0

    def readInitPositionFromFile(self, path):
        with open(path, 'r') as f:
            json_board = json.load(f)
            return json_board["liftPosition"]
