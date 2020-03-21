import json
class Board:
    boardState: []

    def __init__(self):
        self.boardState = []

    def readStateFromFile(self, path,state_to_read):
        with open(path, 'r') as f:
            json_board = json.load(f)
            string_state = json_board[state_to_read]
            self.boardState = [[int(r) for r in i.split(',')]for i in string_state.split("|")]
        # TODO: lift init position from file