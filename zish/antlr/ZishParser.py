# Generated from Zish.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write(";\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\5\3\25\n\3\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\7\5\35\n\5\f\5\16\5 \13\5\3\5\3\5\3\5\3\5\5\5&\n\5")
        buf.write("\3\6\3\6\3\6\3\6\7\6,\n\6\f\6\16\6/\13\6\3\6\3\6\3\6\3")
        buf.write("\6\5\6\65\n\6\3\7\3\7\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2")
        buf.write("\3\3\2\n\20\2:\2\16\3\2\2\2\4\24\3\2\2\2\6\26\3\2\2\2")
        buf.write("\b%\3\2\2\2\n\64\3\2\2\2\f\66\3\2\2\2\16\17\5\4\3\2\17")
        buf.write("\20\7\2\2\3\20\3\3\2\2\2\21\25\5\6\4\2\22\25\5\b\5\2\23")
        buf.write("\25\5\n\6\2\24\21\3\2\2\2\24\22\3\2\2\2\24\23\3\2\2\2")
        buf.write("\25\5\3\2\2\2\26\27\t\2\2\2\27\7\3\2\2\2\30\31\7\3\2\2")
        buf.write("\31\36\5\4\3\2\32\33\7\5\2\2\33\35\5\4\3\2\34\32\3\2\2")
        buf.write("\2\35 \3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37!\3\2\2\2")
        buf.write(" \36\3\2\2\2!\"\7\4\2\2\"&\3\2\2\2#$\7\3\2\2$&\7\4\2\2")
        buf.write("%\30\3\2\2\2%#\3\2\2\2&\t\3\2\2\2\'(\7\6\2\2(-\5\f\7\2")
        buf.write(")*\7\5\2\2*,\5\f\7\2+)\3\2\2\2,/\3\2\2\2-+\3\2\2\2-.\3")
        buf.write("\2\2\2.\60\3\2\2\2/-\3\2\2\2\60\61\7\7\2\2\61\65\3\2\2")
        buf.write("\2\62\63\7\6\2\2\63\65\7\7\2\2\64\'\3\2\2\2\64\62\3\2")
        buf.write("\2\2\65\13\3\2\2\2\66\67\5\6\4\2\678\7\b\2\289\5\4\3\2")
        buf.write("9\r\3\2\2\2\7\24\36%-\64")
        return buf.getvalue()


class ZishParser ( Parser ):

    grammarFileName = "Zish.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "','", "'{'", "'}'", "':'", 
                     "<INVALID>", "'null'" ]

    symbolicNames = [ "<INVALID>", "LIST_START", "LIST_FINISH", "COMMA", 
                      "MAP_START", "MAP_FINISH", "COLON", "WS", "NULL", 
                      "BOOL", "TIMESTAMP", "INTEGER", "DECIMAL", "STRING", 
                      "BLOB" ]

    RULE_start = 0
    RULE_element = 1
    RULE_key = 2
    RULE_list_type = 3
    RULE_map_type = 4
    RULE_pair = 5

    ruleNames =  [ "start", "element", "key", "list_type", "map_type", "pair" ]

    EOF = Token.EOF
    LIST_START=1
    LIST_FINISH=2
    COMMA=3
    MAP_START=4
    MAP_FINISH=5
    COLON=6
    WS=7
    NULL=8
    BOOL=9
    TIMESTAMP=10
    INTEGER=11
    DECIMAL=12
    STRING=13
    BLOB=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(ZishParser.ElementContext,0)


        def EOF(self):
            return self.getToken(ZishParser.EOF, 0)

        def getRuleIndex(self):
            return ZishParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = ZishParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.element()
            self.state = 13
            self.match(ZishParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(ZishParser.KeyContext,0)


        def list_type(self):
            return self.getTypedRuleContext(ZishParser.List_typeContext,0)


        def map_type(self):
            return self.getTypedRuleContext(ZishParser.Map_typeContext,0)


        def getRuleIndex(self):
            return ZishParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)




    def element(self):

        localctx = ZishParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_element)
        try:
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZishParser.NULL, ZishParser.BOOL, ZishParser.TIMESTAMP, ZishParser.INTEGER, ZishParser.DECIMAL, ZishParser.STRING, ZishParser.BLOB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.key()
                pass
            elif token in [ZishParser.LIST_START]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.list_type()
                pass
            elif token in [ZishParser.MAP_START]:
                self.enterOuterAlt(localctx, 3)
                self.state = 17
                self.map_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KeyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(ZishParser.BOOL, 0)

        def NULL(self):
            return self.getToken(ZishParser.NULL, 0)

        def TIMESTAMP(self):
            return self.getToken(ZishParser.TIMESTAMP, 0)

        def INTEGER(self):
            return self.getToken(ZishParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(ZishParser.DECIMAL, 0)

        def STRING(self):
            return self.getToken(ZishParser.STRING, 0)

        def BLOB(self):
            return self.getToken(ZishParser.BLOB, 0)

        def getRuleIndex(self):
            return ZishParser.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)




    def key(self):

        localctx = ZishParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_key)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZishParser.NULL) | (1 << ZishParser.BOOL) | (1 << ZishParser.TIMESTAMP) | (1 << ZishParser.INTEGER) | (1 << ZishParser.DECIMAL) | (1 << ZishParser.STRING) | (1 << ZishParser.BLOB))) != 0)):
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

    class List_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIST_START(self):
            return self.getToken(ZishParser.LIST_START, 0)

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZishParser.ElementContext)
            else:
                return self.getTypedRuleContext(ZishParser.ElementContext,i)


        def LIST_FINISH(self):
            return self.getToken(ZishParser.LIST_FINISH, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZishParser.COMMA)
            else:
                return self.getToken(ZishParser.COMMA, i)

        def getRuleIndex(self):
            return ZishParser.RULE_list_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_type" ):
                listener.enterList_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_type" ):
                listener.exitList_type(self)




    def list_type(self):

        localctx = ZishParser.List_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_list_type)
        self._la = 0 # Token type
        try:
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(ZishParser.LIST_START)
                self.state = 23
                self.element()
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZishParser.COMMA:
                    self.state = 24
                    self.match(ZishParser.COMMA)
                    self.state = 25
                    self.element()
                    self.state = 30
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 31
                self.match(ZishParser.LIST_FINISH)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.match(ZishParser.LIST_START)
                self.state = 34
                self.match(ZishParser.LIST_FINISH)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Map_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAP_START(self):
            return self.getToken(ZishParser.MAP_START, 0)

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZishParser.PairContext)
            else:
                return self.getTypedRuleContext(ZishParser.PairContext,i)


        def MAP_FINISH(self):
            return self.getToken(ZishParser.MAP_FINISH, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZishParser.COMMA)
            else:
                return self.getToken(ZishParser.COMMA, i)

        def getRuleIndex(self):
            return ZishParser.RULE_map_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMap_type" ):
                listener.enterMap_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMap_type" ):
                listener.exitMap_type(self)




    def map_type(self):

        localctx = ZishParser.Map_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_map_type)
        self._la = 0 # Token type
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.match(ZishParser.MAP_START)
                self.state = 38
                self.pair()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZishParser.COMMA:
                    self.state = 39
                    self.match(ZishParser.COMMA)
                    self.state = 40
                    self.pair()
                    self.state = 45
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 46
                self.match(ZishParser.MAP_FINISH)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(ZishParser.MAP_START)
                self.state = 49
                self.match(ZishParser.MAP_FINISH)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(ZishParser.KeyContext,0)


        def COLON(self):
            return self.getToken(ZishParser.COLON, 0)

        def element(self):
            return self.getTypedRuleContext(ZishParser.ElementContext,0)


        def getRuleIndex(self):
            return ZishParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)




    def pair(self):

        localctx = ZishParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.key()
            self.state = 53
            self.match(ZishParser.COLON)
            self.state = 54
            self.element()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





