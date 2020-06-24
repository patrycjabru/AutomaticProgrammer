import Game.Board as Board
from GameOperations import GameOperations
from Program import Program
from ProgramBlocks import ProgramBlocks
from Game.ConditionalBlock import ConditionalBlock
from Lift import Lift

path = "GameStates/3.json"
initialBoard = Board.Board(path, "init")

finalBoard = Board.Board(path, "end")
lift = Lift(path)
program = Program()
game = GameOperations(initialBoard, finalBoard, program,lift)


cond = ConditionalBlock(False, False, 1, ProgramBlocks.ARROW_RIGHT)
#program.subProgram1 = \
#    [ProgramBlocks.ARROW_RIGHT, ProgramBlocks.ARROW_RIGHT, ProgramBlocks.ARROW_DOWN, cond, ProgramBlocks.ARROW_DOWN]
#program.subProgram1 = [ProgramBlocks.ARROW_DOWN,ProgramBlocks.ARROW_RIGHT,ProgramBlocks.ARROW_DOWN,ProgramBlocks.ARROW_LEFT,ProgramBlocks.SUB_PROGRAM_2]
#program.subProgram2 = [ProgramBlocks.ARROW_DOWN,ProgramBlocks.ARROW_LEFT,ProgramBlocks.ARROW_DOWN,ProgramBlocks.ARROW_RIGHT,ProgramBlocks.SUB_PROGRAM_1]
program.subProgram1 = [ProgramBlocks.ARROW_LEFT,ProgramBlocks.ARROW_DOWN,ProgramBlocks.ARROW_LEFT,ProgramBlocks.ARROW_DOWN]

print(game.board.boardState)
game.runProgram()
print("Victory" if game.checkVictory() else "Defeat")
print(game.finalBoard.boardState)


