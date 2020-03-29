# Generated from cargobot.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("\65\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write("\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3")
        buf.write("\34\n\3\3\4\3\4\3\4\5\4!\n\4\3\4\3\4\7\4%\n\4\f\4\16\4")
        buf.write("(\13\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t")
        buf.write("\2\3\6\n\2\4\6\b\n\f\16\20\2\4\3\2\n\20\3\2\4\t\2/\2\22")
        buf.write("\3\2\2\2\4\33\3\2\2\2\6 \3\2\2\2\b)\3\2\2\2\n,\3\2\2\2")
        buf.write("\f.\3\2\2\2\16\60\3\2\2\2\20\62\3\2\2\2\22\23\5\6\4\2")
        buf.write("\23\24\5\4\3\2\24\25\5\4\3\2\25\26\5\4\3\2\26\3\3\2\2")
        buf.write("\2\27\30\5\20\t\2\30\31\5\6\4\2\31\34\3\2\2\2\32\34\5")
        buf.write("\20\t\2\33\27\3\2\2\2\33\32\3\2\2\2\34\5\3\2\2\2\35\36")
        buf.write("\b\4\1\2\36!\5\f\7\2\37!\5\b\5\2 \35\3\2\2\2 \37\3\2\2")
        buf.write("\2!&\3\2\2\2\"#\f\5\2\2#%\5\6\4\6$\"\3\2\2\2%(\3\2\2\2")
        buf.write("&$\3\2\2\2&\'\3\2\2\2\'\7\3\2\2\2(&\3\2\2\2)*\5\16\b\2")
        buf.write("*+\5\n\6\2+\t\3\2\2\2,-\t\2\2\2-\13\3\2\2\2./\t\2\2\2")
        buf.write("/\r\3\2\2\2\60\61\t\3\2\2\61\17\3\2\2\2\62\63\7\3\2\2")
        buf.write("\63\21\3\2\2\2\5\33 &")
        return buf.getvalue()


class cargobotParser ( Parser ):

    grammarFileName = "cargobot.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'separator'", "'all'", "'empty'", "'color1'", 
                     "'color2'", "'color3'", "'color4'", "'left_arrow'", 
                     "'right_arrow'", "'down_arrow'", "'program1'", "'program2'", 
                     "'program3'", "'program4'" ]

    symbolicNames = [ "<INVALID>", "SEPARATOR", "ALL", "EMPTY", "COLOR1", 
                      "COLOR2", "COLOR3", "COLOR4", "LEFT_ARROW", "RIGHT_ARROW", 
                      "DOWN_ARROW", "PROGRAM1", "PROGRAM2", "PROGRAM3", 
                      "PROGRAM4", "WS" ]

    RULE_start = 0
    RULE_section = 1
    RULE_block = 2
    RULE_conditional_statement = 3
    RULE_conditional_action = 4
    RULE_action = 5
    RULE_condition = 6
    RULE_separator = 7

    ruleNames =  [ "start", "section", "block", "conditional_statement", 
                   "conditional_action", "action", "condition", "separator" ]

    EOF = Token.EOF
    SEPARATOR=1
    ALL=2
    EMPTY=3
    COLOR1=4
    COLOR2=5
    COLOR3=6
    COLOR4=7
    LEFT_ARROW=8
    RIGHT_ARROW=9
    DOWN_ARROW=10
    PROGRAM1=11
    PROGRAM2=12
    PROGRAM3=13
    PROGRAM4=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(cargobotParser.BlockContext,0)


        def section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cargobotParser.SectionContext)
            else:
                return self.getTypedRuleContext(cargobotParser.SectionContext,i)


        def getRuleIndex(self):
            return cargobotParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = cargobotParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.block(0)
            self.state = 17
            self.section()
            self.state = 18
            self.section()
            self.state = 19
            self.section()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SectionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def separator(self):
            return self.getTypedRuleContext(cargobotParser.SeparatorContext,0)


        def block(self):
            return self.getTypedRuleContext(cargobotParser.BlockContext,0)


        def getRuleIndex(self):
            return cargobotParser.RULE_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection" ):
                listener.enterSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection" ):
                listener.exitSection(self)




    def section(self):

        localctx = cargobotParser.SectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_section)
        try:
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.separator()
                self.state = 22
                self.block(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.separator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def action(self):
            return self.getTypedRuleContext(cargobotParser.ActionContext,0)


        def conditional_statement(self):
            return self.getTypedRuleContext(cargobotParser.Conditional_statementContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cargobotParser.BlockContext)
            else:
                return self.getTypedRuleContext(cargobotParser.BlockContext,i)


        def getRuleIndex(self):
            return cargobotParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)



    def block(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cargobotParser.BlockContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_block, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [cargobotParser.LEFT_ARROW, cargobotParser.RIGHT_ARROW, cargobotParser.DOWN_ARROW, cargobotParser.PROGRAM1, cargobotParser.PROGRAM2, cargobotParser.PROGRAM3, cargobotParser.PROGRAM4]:
                self.state = 28
                self.action()
                pass
            elif token in [cargobotParser.ALL, cargobotParser.EMPTY, cargobotParser.COLOR1, cargobotParser.COLOR2, cargobotParser.COLOR3, cargobotParser.COLOR4]:
                self.state = 29
                self.conditional_statement()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = cargobotParser.BlockContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_block)
                    self.state = 32
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 33
                    self.block(4) 
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Conditional_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(cargobotParser.ConditionContext,0)


        def conditional_action(self):
            return self.getTypedRuleContext(cargobotParser.Conditional_actionContext,0)


        def getRuleIndex(self):
            return cargobotParser.RULE_conditional_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_statement" ):
                listener.enterConditional_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_statement" ):
                listener.exitConditional_statement(self)




    def conditional_statement(self):

        localctx = cargobotParser.Conditional_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_conditional_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.condition()
            self.state = 40
            self.conditional_action()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_actionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_ARROW(self):
            return self.getToken(cargobotParser.LEFT_ARROW, 0)

        def RIGHT_ARROW(self):
            return self.getToken(cargobotParser.RIGHT_ARROW, 0)

        def DOWN_ARROW(self):
            return self.getToken(cargobotParser.DOWN_ARROW, 0)

        def PROGRAM1(self):
            return self.getToken(cargobotParser.PROGRAM1, 0)

        def PROGRAM2(self):
            return self.getToken(cargobotParser.PROGRAM2, 0)

        def PROGRAM3(self):
            return self.getToken(cargobotParser.PROGRAM3, 0)

        def PROGRAM4(self):
            return self.getToken(cargobotParser.PROGRAM4, 0)

        def getRuleIndex(self):
            return cargobotParser.RULE_conditional_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_action" ):
                listener.enterConditional_action(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_action" ):
                listener.exitConditional_action(self)




    def conditional_action(self):

        localctx = cargobotParser.Conditional_actionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_conditional_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cargobotParser.LEFT_ARROW) | (1 << cargobotParser.RIGHT_ARROW) | (1 << cargobotParser.DOWN_ARROW) | (1 << cargobotParser.PROGRAM1) | (1 << cargobotParser.PROGRAM2) | (1 << cargobotParser.PROGRAM3) | (1 << cargobotParser.PROGRAM4))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_ARROW(self):
            return self.getToken(cargobotParser.LEFT_ARROW, 0)

        def RIGHT_ARROW(self):
            return self.getToken(cargobotParser.RIGHT_ARROW, 0)

        def DOWN_ARROW(self):
            return self.getToken(cargobotParser.DOWN_ARROW, 0)

        def PROGRAM1(self):
            return self.getToken(cargobotParser.PROGRAM1, 0)

        def PROGRAM2(self):
            return self.getToken(cargobotParser.PROGRAM2, 0)

        def PROGRAM3(self):
            return self.getToken(cargobotParser.PROGRAM3, 0)

        def PROGRAM4(self):
            return self.getToken(cargobotParser.PROGRAM4, 0)

        def getRuleIndex(self):
            return cargobotParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)




    def action(self):

        localctx = cargobotParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cargobotParser.LEFT_ARROW) | (1 << cargobotParser.RIGHT_ARROW) | (1 << cargobotParser.DOWN_ARROW) | (1 << cargobotParser.PROGRAM1) | (1 << cargobotParser.PROGRAM2) | (1 << cargobotParser.PROGRAM3) | (1 << cargobotParser.PROGRAM4))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALL(self):
            return self.getToken(cargobotParser.ALL, 0)

        def EMPTY(self):
            return self.getToken(cargobotParser.EMPTY, 0)

        def COLOR1(self):
            return self.getToken(cargobotParser.COLOR1, 0)

        def COLOR2(self):
            return self.getToken(cargobotParser.COLOR2, 0)

        def COLOR3(self):
            return self.getToken(cargobotParser.COLOR3, 0)

        def COLOR4(self):
            return self.getToken(cargobotParser.COLOR4, 0)

        def getRuleIndex(self):
            return cargobotParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = cargobotParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cargobotParser.ALL) | (1 << cargobotParser.EMPTY) | (1 << cargobotParser.COLOR1) | (1 << cargobotParser.COLOR2) | (1 << cargobotParser.COLOR3) | (1 << cargobotParser.COLOR4))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeparatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEPARATOR(self):
            return self.getToken(cargobotParser.SEPARATOR, 0)

        def getRuleIndex(self):
            return cargobotParser.RULE_separator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeparator" ):
                listener.enterSeparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeparator" ):
                listener.exitSeparator(self)




    def separator(self):

        localctx = cargobotParser.SeparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_separator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(cargobotParser.SEPARATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.block_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def block_sempred(self, localctx:BlockContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




