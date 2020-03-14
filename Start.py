import Game.Board as Board
from GameOperations import GameOperations
from Program import Program
from ProgramBlocks import ProgramBlocks
from Game.ConditionalBlock import ConditionalBlock

path = "GameStates/start_1"
initialBoard = Board.Board()
initialBoard.readStateFromFile(path)


path = "GameStates/end_1"
finalBoard = Board.Board()
finalBoard.readStateFromFile(path)


program = Program()
game = GameOperations(initialBoard, finalBoard, program)


cond = ConditionalBlock(False, False, 1, ProgramBlocks.ARROW_RIGHT);
program.subProgram1 = [ProgramBlocks.ARROW_RIGHT, ProgramBlocks.ARROW_RIGHT, ProgramBlocks.ARROW_DOWN, cond, ProgramBlocks.ARROW_DOWN]

game.runProgram()

print(game.board.boardState)
print(game.checkVictory())
print(game.finalBoard.boardState)


