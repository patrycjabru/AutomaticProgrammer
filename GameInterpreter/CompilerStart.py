from GameInterpreter.Compiler import Compiler
import Game.Board as Board
from GameOperations import GameOperations
from Program import Program
from ProgramBlocks import ProgramBlocks
from Game.ConditionalBlock import ConditionalBlock
from Lift import Lift


def check_difference_with_neighborhood(final, actual):
    score = 0
    for index_x, row_a in enumerate(actual.boardState):
        for index_y, state_a in enumerate(row_a):
            score += neighborhood(index_x, index_y, state_a,
                                       final.boardState)
    return score


def neighborhood(x, y, state, final):
    if state == final[x][y]:
        return 0
    neighbors = [(x2, y2) for x2 in range(max(0, x - 1), min(len(final), x + 2))
                 for y2 in range(max(0, y - 1), min(len(final[0]), y + 2))
                 if (x2, y2) != (x, y)]
    for a, b in neighbors:
        if state == final[a][b]:
            return 10
    return 100

compiler = Compiler()

program = compiler.compile("right_arrow right_arrow down_arrow right_arrow down_arrow left_arrow left_arrow left_arrow left_arrow left_arrow left_arrow left_arrow left_arrow left_arrow left_arrow down_arrow left_arrow down_arrow left_arrow left_arrow left_arrow left_arrow left_arrow down_arrow left_arrow down_arrow left_arrow left_arrow down_arrow left_arrow down_arrow right_arrow down_arrow right_arrow down_arrow separator separator separator")
path = "../GameStates/3.json"
initial_board = Board.Board(path, "init")

final_board = Board.Board(path, "end")
lift = Lift(path)

game = GameOperations(initial_board, final_board, program, lift)
game.runProgram()
print("Victory" if game.checkVictory() else "Defeat")
print(game.board)
print(program)
print(check_difference_with_neighborhood(
            game.finalBoard, game.board))
