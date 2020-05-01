from Board import Board
from Compiler import Compiler
from ConditionalBlock import ConditionalBlock
from GameOperations import GameOperations
from Lift import Lift
from Program import Program
from ProgramBlocks import ProgramBlocks
from algorithm.parameters import params
from fitness.base_ff_classes.base_ff import base_ff


class cargobot_fitness(base_ff):
    """Fitness function for matching a string. Takes a string and returns
    fitness. Penalises output that is not the same length as the target.
    Penalty given to individual string components which do not match ASCII
    value of target."""

    def __init__(self):
        # Initialise base fitness function class.
        super().__init__()

        # Set target string.
        self.path = params['GAME_BOARD']

    def check_difference(self, final, actual):
        score = 0
        for state_a, state_b in zip(final.boardState, actual.boardState):
            if state_a != state_b:
                score += 1
        return score

    def evaluate(self, ind, **kwargs):
        guess = ind.phenotype
        compiler = Compiler()
        print(guess)
        program = compiler.compile(guess)
        initial_board = Board(self.path, "init")
        final_board = Board(self.path, "end")
        lift = Lift(self.path)
        game = GameOperations(initial_board, final_board, program, lift)
        game.runProgram()
        fitness = 0 if game.checkVictory() else self.check_difference(
            game.finalBoard, game.board)
        print(fitness)
        return fitness
