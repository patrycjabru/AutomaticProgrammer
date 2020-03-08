class Board:
    boardState: []

    def __init__(self):
        self.boardState = []

    def readStateFromFile(self, path):
        with open(path, 'r') as f:
            lines = f.readlines()
            for i in lines:
                rowAsChars = (i.split(','))
                rowAsInts = []
                for r in rowAsChars:
                    rowAsInts.append(int(r))
                self.boardState.append(rowAsInts)