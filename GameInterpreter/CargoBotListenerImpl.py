from Board import Board
from ConditionalBlock import ConditionalBlock
from GameInterpreter.Generated.cargobotListener import cargobotListener
from GameInterpreter.Generated.cargobotParser import cargobotParser
from GameOperations import GameOperations
from Lift import Lift
from Program import Program
from ProgramBlocks import ProgramBlocks


class CargoBotListenerImpl(cargobotListener):
    program: Program
    programNumber = 1

    condition: cargobotParser.ConditionContext
    conditionalAction: ProgramBlocks

    def __init__(self, program):
        self.program = program

    def enterSeparator(self, ctx:cargobotParser.SeparatorContext):
        self.programNumber = self.programNumber + 1

    def enterAction(self, ctx:cargobotParser.ActionContext):
        if ctx.DOWN_ARROW():
            self.__addActionToList(ProgramBlocks.ARROW_DOWN)
        elif ctx.LEFT_ARROW():
            self.__addActionToList(ProgramBlocks.ARROW_LEFT)
        elif ctx.RIGHT_ARROW():
            self.__addActionToList(ProgramBlocks.ARROW_RIGHT)
        elif ctx.PROGRAM1():
            self.__addActionToList(ProgramBlocks.SUB_PROGRAM_1)
        elif ctx.PROGRAM2():
            self.__addActionToList(ProgramBlocks.SUB_PROGRAM_2)
        elif ctx.PROGRAM3():
            self.__addActionToList(ProgramBlocks.SUB_PROGRAM_3)
        elif ctx.PROGRAM4():
            self.__addActionToList(ProgramBlocks.SUB_PROGRAM_4)

    def __addActionToList(self, action):
        if self.programNumber == 1:
            self.program.subProgram1.append(action)
        elif self.programNumber == 2:
            self.program.subProgram2.append(action)
        elif self.programNumber == 3:
            self.program.subProgram3.append(action)
        elif self.programNumber == 4:
            self.program.subProgram4.append(action)

    def enterCondition(self, ctx:cargobotParser.ConditionContext):
        self.condition = ctx

    def enterConditional_action(self, ctx:cargobotParser.Conditional_actionContext):
        if ctx.DOWN_ARROW():
            self.conditionalAction = ProgramBlocks.ARROW_DOWN
        elif ctx.LEFT_ARROW():
            self.conditionalAction = ProgramBlocks.ARROW_LEFT
        elif ctx.RIGHT_ARROW():
            self.conditionalAction = ProgramBlocks.ARROW_RIGHT
        elif ctx.PROGRAM1():
            self.conditionalAction = ProgramBlocks.SUB_PROGRAM_1
        elif ctx.PROGRAM2():
            self.conditionalAction = ProgramBlocks.SUB_PROGRAM_2
        elif ctx.PROGRAM3():
            self.conditionalAction = ProgramBlocks.SUB_PROGRAM_3
        elif ctx.PROGRAM4():
            self.conditionalAction = ProgramBlocks.SUB_PROGRAM_4

    def exitConditional_statement(self, ctx:cargobotParser.Conditional_statementContext):
        cond = None
        if self.condition.ALL():
            cond = ConditionalBlock(False, True, None, self.conditionalAction)
        elif self.condition.EMPTY():
            cond = ConditionalBlock(True, False, None, self.conditionalAction)
        elif self.condition.COLOR1():
            cond = ConditionalBlock(False, False, 1, self.conditionalAction)
        elif self.condition.COLOR2():
            cond = ConditionalBlock(False, False, 2, self.conditionalAction)
        elif self.condition.COLOR3():
            cond = ConditionalBlock(False, False, 3, self.conditionalAction)
        elif self.condition.COLOR4():
            cond = ConditionalBlock(False, False, 4, self.conditionalAction)

        self.__addActionToList(cond)
        self.conditionalAction = None
        self.condition = None
