import json


class Board:
    boardState: list

    def __init__(self, path, state_to_read):
        self.boardState = self.readStateFromFile(path, state_to_read)

    def readStateFromFile(self, path, state_to_read):
        with open(path, 'r') as f:
            json_board = json.load(f)
            string_state = json_board[state_to_read]
            return [[int(r) for r in i.split(',')] for i in string_state.split("|")]

    def __repr__(self):
        string_repr = ""
        for i in self.boardState:
            string_repr+=str(i)+"\n"
        return  string_repr