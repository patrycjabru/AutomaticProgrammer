from ProgramBlocks import ProgramBlocks


class ConditionalBlock:
    isNone: False
    isAll: False
    colorNumber: None
    operation: ProgramBlocks
    value = 9

    def __init__(self, isNone, isAll, colorNumber, operation):
        self.isNone = isNone
        self.isAll = isAll
        self.colorNumber = colorNumber
        self.operation = operation
