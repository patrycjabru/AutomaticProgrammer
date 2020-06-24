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
        for row_a, row_b in zip(final.boardState, actual.boardState):
            for state_a, state_b in zip(row_a, row_b):
                if state_a != state_b:
                    score += 1
        return score

    def check_difference_with_neighborhood(self, final, actual):
        score = 0
        for index_x, row_a in enumerate(actual.boardState):
            for index_y, state_a in enumerate(row_a):
                score += self.neighborhood(index_x, index_y, state_a,
                                          final.boardState)
        return score

    def neighborhood(self, x, y, state, final):
        if state == final[x][y]:
            return 0
        neighbors = [(x2, y2) for x2 in range(max(0, x-1), min(len(final), x+2))
                    for y2 in range(max(0, y-1), min(len(final[0]), y+2))
                    if (x2, y2) != (x, y)]
        for a, b in neighbors:
            if state == final[a][b]:
                return 10
        return 100

    def evaluate(self, ind, **kwargs):
        fitness = 0
        guess = ind.phenotype
        compiler = Compiler()
        print(guess)
        if guess.count("down_arrow")<2:
            fitness += 10000
        if len(guess.split()) > 140:
        #    print("so big")
            return 10000
        program = compiler.compile(guess)
        initial_board = Board(self.path, "init")
        final_board = Board(self.path, "end")
        lift = Lift(self.path)
        game = GameOperations(initial_board, final_board, program, lift)
        #print(game.board)
        game.runProgram()
        fitness += 0 if game.checkVictory() else self.check_difference_with_neighborhood(
            game.finalBoard, game.board)
        #fitness -= game.changed_blocks*10 if fitness > 100 else 0
        fitness += 20 if lift.liftedBlock != 0 else 0
        #
        # if fitness<40:
        #     print(game.board)
        #     print(fitness)
        return fitness
