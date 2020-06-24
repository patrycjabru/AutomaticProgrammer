class Program:
    subProgram1 = []
    subProgram2 = []
    subProgram3 = []
    subProgram4 = []

    executionSubProgramNumber = 1
    commandIndex = 0

    def __repr__(self):
        return str(self.subProgram1) + " " + str(self.subProgram2) + " " +\
               str(self.subProgram3) + " " + str(self.subProgram4) + " "

    def maxCurrentSubProgramLength(self):
        if self.executionSubProgramNumber == 1:
            return len(self.subProgram1)
        elif self.executionSubProgramNumber == 2:
            return len(self.subProgram2)
        elif self.executionSubProgramNumber == 3:
            return len(self.subProgram3)
        elif self.executionSubProgramNumber == 4:
            return len(self.subProgram4)

    def getCurrentCommand(self):
        if self.executionSubProgramNumber == 1:
            return self.subProgram1[self.commandIndex]
        elif self.executionSubProgramNumber == 2:
            return self.subProgram2[self.commandIndex]
        elif self.executionSubProgramNumber == 3:
            return self.subProgram3[self.commandIndex]
        elif self.executionSubProgramNumber == 4:
            return self.subProgram4[self.commandIndex]
