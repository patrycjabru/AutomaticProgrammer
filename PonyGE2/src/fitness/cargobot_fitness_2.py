from Board import Board
from Compiler import Compiler
from ConditionalBlock import ConditionalBlock
from GameOperations import GameOperations
from Lift import Lift
from Program import Program
from ProgramBlocks import ProgramBlocks
from algorithm.parameters import params
from fitness.base_ff_classes.base_ff import base_ff


class cargobot_fitness_2(base_ff):
    """Fitness function for matching a string. Takes a string and returns
    fitness. Penalises output that is not the same length as the target.
    Penalty given to individual string components which do not match ASCII
    value of target."""

    def __init__(self):
        # Initialise base fitness function class.
        super().__init__()

        # Set target string.
        self.path = params['GAME_BOARD']

    def checkWrongBlocks(self, board, final_board):
        misplacedBlocks = [[0 for i in range(len(board[0]))] for j in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != final_board[i][j]:
                    misplacedBlocks[i][j] = 1

        return misplacedBlocks

    def calculateSumDistance(self, misplacedBlocks, board, final_board):
        dist = 0

        for i in range(len(board)):
            for j in range(len(board[i])):
                if misplacedBlocks[i][j]==1:
                    dist += self.findClosestNeighbour(i, j, board[i][j], final_board)

        return dist

    def calculateDistance(self, row, col, final_row, final_col):
        return abs(final_row-row) + abs(final_col - col)

    def findClosestNeighbour(self, row, col, block, final_board):
        neighour_dist = 100000

        for i in range(len(final_board)):
            for j in range(len(final_board[i])):
                if final_board[i][j] == block:
                    dist = self.calculateDistance(row, col, i, j)
                    if dist < neighour_dist:
                        neighour_dist = dist

        return  neighour_dist

    def evaluate(self, ind, **kwargs):
        fitness = 0
        guess = ind.phenotype
        compiler = Compiler()
        print(guess)
        program = compiler.compile(guess)
        initial_board = Board(self.path, "init")
        final_board = Board(self.path, "end")
        lift = Lift(self.path)
        game = GameOperations(initial_board, final_board, program, lift)
        game.runProgram()
        board = game.board.boardState

        #distance
        misplacedBlocks = self.checkWrongBlocks(board, final_board.boardState)
        distance = self.calculateSumDistance(misplacedBlocks, board, final_board.boardState)

        #down arrow count
        guess.count("down_arrow")

        fitness = distance * 100

        print(fitness)
        return fitness
