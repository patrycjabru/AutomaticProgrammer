from antlr4 import *

from GameInterpreter.CargoBotListenerImpl import CargoBotListenerImpl
from GameInterpreter.Generated.cargobotLexer import cargobotLexer
from GameInterpreter.Generated.cargobotParser import cargobotParser
from Program import Program


class Compiler:
    def compile(self, code):
        codeStream = InputStream(code)
        lexer = cargobotLexer(codeStream)
        stream = CommonTokenStream(lexer)
        parser = cargobotParser(stream)
        tree = parser.start()
        program = Program()
        listener = CargoBotListenerImpl(program)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        return program
