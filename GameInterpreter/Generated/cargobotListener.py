# Generated from cargobot.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cargobotParser import cargobotParser
else:
    from cargobotParser import cargobotParser

# This class defines a complete listener for a parse tree produced by cargobotParser.
class cargobotListener(ParseTreeListener):

    # Enter a parse tree produced by cargobotParser#start.
    def enterStart(self, ctx:cargobotParser.StartContext):
        pass

    # Exit a parse tree produced by cargobotParser#start.
    def exitStart(self, ctx:cargobotParser.StartContext):
        pass


    # Enter a parse tree produced by cargobotParser#section.
    def enterSection(self, ctx:cargobotParser.SectionContext):
        pass

    # Exit a parse tree produced by cargobotParser#section.
    def exitSection(self, ctx:cargobotParser.SectionContext):
        pass


    # Enter a parse tree produced by cargobotParser#block.
    def enterBlock(self, ctx:cargobotParser.BlockContext):
        pass

    # Exit a parse tree produced by cargobotParser#block.
    def exitBlock(self, ctx:cargobotParser.BlockContext):
        pass


    # Enter a parse tree produced by cargobotParser#conditional_statement.
    def enterConditional_statement(self, ctx:cargobotParser.Conditional_statementContext):
        pass

    # Exit a parse tree produced by cargobotParser#conditional_statement.
    def exitConditional_statement(self, ctx:cargobotParser.Conditional_statementContext):
        pass


    # Enter a parse tree produced by cargobotParser#conditional_action.
    def enterConditional_action(self, ctx:cargobotParser.Conditional_actionContext):
        pass

    # Exit a parse tree produced by cargobotParser#conditional_action.
    def exitConditional_action(self, ctx:cargobotParser.Conditional_actionContext):
        pass


    # Enter a parse tree produced by cargobotParser#action.
    def enterAction(self, ctx:cargobotParser.ActionContext):
        pass

    # Exit a parse tree produced by cargobotParser#action.
    def exitAction(self, ctx:cargobotParser.ActionContext):
        pass


    # Enter a parse tree produced by cargobotParser#condition.
    def enterCondition(self, ctx:cargobotParser.ConditionContext):
        pass

    # Exit a parse tree produced by cargobotParser#condition.
    def exitCondition(self, ctx:cargobotParser.ConditionContext):
        pass


    # Enter a parse tree produced by cargobotParser#separator.
    def enterSeparator(self, ctx:cargobotParser.SeparatorContext):
        pass

    # Exit a parse tree produced by cargobotParser#separator.
    def exitSeparator(self, ctx:cargobotParser.SeparatorContext):
        pass



del cargobotParser