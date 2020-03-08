import Game.Board as Board
from GameOperations import GameOperations

path = "GameStates/start_1"
initialBoard = Board.Board()
initialBoard.readStateFromFile(path)
print(initialBoard.boardState)

path = "GameStates/end_1"
finalBoard = Board.Board()
finalBoard.readStateFromFile(path)
print(finalBoard.boardState)

game = GameOperations(initialBoard, finalBoard)
game.arrowDown()

print(game.board.boardState)

game.arrowDown()

print(game.board.boardState)

