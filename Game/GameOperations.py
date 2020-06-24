import Board
import Game.ConditionalBlock
import Lift
from Program import Program
from ProgramBlocks import ProgramBlocks


class GameOperations:
    lift: Lift
    board: Board
    finalBoard: Board
    isGameOver: bool
    outOfBoard: bool
    program: Program
    moves: int
    max_moves: int
    changed_blocks: int

    def __init__(self, initialBoard, finalBoard, program, lift):
        self.isGameOver = False
        self.outOfBoard = False
        self.lift = lift
        self.board = initialBoard
        self.finalBoard = finalBoard
        self.program = program
        self.moves = 0
        self.max_moves = 500
        self.changed_blocks = 0

    def arrowDown(self):
        if self.lift.liftedBlock == 0:
            self.__liftBlock()
        else:
            self.__placeBlock()


    def __liftBlock(self):
        numberOfRows = len(self.board.boardState)
        for i in range(numberOfRows):
            if self.board.boardState[i][self.lift.position] != 0:
                self.lift.liftedBlock = self.board.boardState[i][
                    self.lift.position]
                self.board.boardState[i][self.lift.position] = 0
                break

    def __placeBlock(self):
        if self.lift.liftedBlock==0:
            return
        numberOfRows = len(self.board.boardState)
        for i in range(numberOfRows):
            if self.board.boardState[i][self.lift.position] != 0:
                if i - 1 >= 0:
                    self.board.boardState[i - 1][
                        self.lift.position] = self.lift.liftedBlock
                    self.lift.liftedBlock = 0
                    self.changed_blocks += 1
                    return
                else:
                    self.isGameOver = True
                    return
        self.board.boardState[numberOfRows - 1][
            self.lift.position] = self.lift.liftedBlock
        self.lift.liftedBlock = 0

    def rightArrow(self):
        numberOfColumns = len(self.board.boardState[0])
        if self.lift.position + 1 == numberOfColumns:
            self.lift.position = 0
            return
        self.lift.position = self.lift.position + 1

    def leftArrow(self):
        numberOfColumns = len(self.board.boardState[0])
        if self.lift.position - 1 < 0:
            self.lift.position = numberOfColumns - 1
            return
        self.lift.position = self.lift.position - 1

    def conditional(self, colorNumber, command):
        if colorNumber == -1 and self.lift.liftedBlock != 0:
            self.runCommand(command)
        elif self.lift.liftedBlock == colorNumber:
            self.runCommand(command)

    def changeSubProgram(self, numberOfSubProgram):
        if numberOfSubProgram == 1 or numberOfSubProgram == 2 or numberOfSubProgram == 3 or numberOfSubProgram == 4:
            self.program.executionSubProgramNumber = numberOfSubProgram
            self.program.commandIndex = 0

    def runProgram(self):
        while self.program.commandIndex < self.program.maxCurrentSubProgramLength() \
                and not self.checkVictory() and not self.isGameOver and self.moves < self.max_moves:
            self.moves += 1
            command = self.program.getCurrentCommand()
            self.runCommand(command)
            if command.value not in \
                    [ProgramBlocks.SUB_PROGRAM_1.value,
                     ProgramBlocks.SUB_PROGRAM_2.value,
                     ProgramBlocks.SUB_PROGRAM_3.value,
                     ProgramBlocks.SUB_PROGRAM_4.value]:
                self.program.commandIndex = self.program.commandIndex + 1

    def runCommand(self, command):
        if command == ProgramBlocks.ARROW_DOWN:
            self.arrowDown()
        elif command == ProgramBlocks.ARROW_LEFT:
            self.leftArrow()
        elif command == ProgramBlocks.ARROW_RIGHT:
            self.rightArrow()
        elif type(command) is Game.ConditionalBlock.ConditionalBlock:
            if command.isNone:
                self.conditional(0, command.operation)
            elif command.isAll:
                self.conditional(-1, command.operation)
            else:
                self.conditional(command.colorNumber, command.operation)
        elif command == ProgramBlocks.SUB_PROGRAM_1:
            self.changeSubProgram(1)
        elif command == ProgramBlocks.SUB_PROGRAM_2:
            self.changeSubProgram(2)
        elif command == ProgramBlocks.SUB_PROGRAM_3:
            self.changeSubProgram(3)
        elif command == ProgramBlocks.SUB_PROGRAM_4:
            self.changeSubProgram(4)

    def checkVictory(self):
        if self.board.boardState == self.finalBoard.boardState:
            return True
        return False
