import Board
import Lift


class GameOperations:
    lift: Lift
    board: Board
    finalBoard: Board
    isGameOver: bool

    def __init__(self, initialBoard, finalBoard):
        self.isGameOver = False
        self.lift = Lift.Lift()
        self.board = initialBoard
        self.finalBoard = finalBoard

    def arrowDown(self):
        if self.lift.liftedBlock == 0:
            self.__liftBlock()
        else:
            self.__placeBlock()

    def __liftBlock(self):
        numberOfRows = len(self.board.boardState)
        for i in range(numberOfRows):
            if self.board.boardState[i][self.lift.position] != 0:
                self.lift.liftedBlock = self.board.boardState[i][self.lift.position]
                self.board.boardState[i][self.lift.position] = 0
                break

    def __placeBlock(self):
        numberOfRows = len(self.board.boardState)
        for i in range(numberOfRows):
            if self.board.boardState[i][self.lift.position] != 0:
                if i-1 >= 0:
                    self.board.boardState[i-1][self.lift.position] = self.lift.liftedBlock
                    self.lift.liftedBlock = 0
                else:
                    self.isGameOver = True
                    return
        self.board.boardState[numberOfRows-1][self.lift.position] = self.lift.liftedBlock
        self.lift.liftedBlock = 0

    def rightArrow(self):
        numberOfColumns = len(self.board.boardState[0])
        if self.lift.position+1 == numberOfColumns:
            self.isGameOver = True
            return
        self.lift.position = self.lift.position + 1

    def leftArrow(self):
        if self.lift.position-1 < 0:
            self.isGameOver = True
            return
        self.lift.position = self.lift.position - 1