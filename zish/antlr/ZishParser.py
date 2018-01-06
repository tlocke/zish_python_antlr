# Generated from Zish.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("=\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\31\n\3\3\4\3")
        buf.write("\4\3\4\3\4\7\4\37\n\4\f\4\16\4\"\13\4\3\4\3\4\3\4\3\4")
        buf.write("\5\4(\n\4\3\5\3\5\3\5\3\5\7\5.\n\5\f\5\16\5\61\13\5\3")
        buf.write("\5\3\5\3\5\3\5\5\5\67\n\5\3\6\3\6\3\6\3\6\3\6\2\2\7\2")
        buf.write("\4\6\b\n\2\2\2C\2\f\3\2\2\2\4\30\3\2\2\2\6\'\3\2\2\2\b")
        buf.write("\66\3\2\2\2\n8\3\2\2\2\f\r\5\4\3\2\r\16\7\2\2\3\16\3\3")
        buf.write("\2\2\2\17\31\7\13\2\2\20\31\7\n\2\2\21\31\7\f\2\2\22\31")
        buf.write("\7\r\2\2\23\31\7\16\2\2\24\31\7\17\2\2\25\31\7\20\2\2")
        buf.write("\26\31\5\6\4\2\27\31\5\b\5\2\30\17\3\2\2\2\30\20\3\2\2")
        buf.write("\2\30\21\3\2\2\2\30\22\3\2\2\2\30\23\3\2\2\2\30\24\3\2")
        buf.write("\2\2\30\25\3\2\2\2\30\26\3\2\2\2\30\27\3\2\2\2\31\5\3")
        buf.write("\2\2\2\32\33\7\3\2\2\33 \5\4\3\2\34\35\7\5\2\2\35\37\5")
        buf.write("\4\3\2\36\34\3\2\2\2\37\"\3\2\2\2 \36\3\2\2\2 !\3\2\2")
        buf.write("\2!#\3\2\2\2\" \3\2\2\2#$\7\4\2\2$(\3\2\2\2%&\7\3\2\2")
        buf.write("&(\7\4\2\2\'\32\3\2\2\2\'%\3\2\2\2(\7\3\2\2\2)*\7\6\2")
        buf.write("\2*/\5\n\6\2+,\7\5\2\2,.\5\n\6\2-+\3\2\2\2.\61\3\2\2\2")
        buf.write("/-\3\2\2\2/\60\3\2\2\2\60\62\3\2\2\2\61/\3\2\2\2\62\63")
        buf.write("\7\7\2\2\63\67\3\2\2\2\64\65\7\6\2\2\65\67\7\7\2\2\66")
        buf.write(")\3\2\2\2\66\64\3\2\2\2\67\t\3\2\2\289\5\4\3\29:\7\b\2")
        buf.write("\2:;\5\4\3\2;\13\3\2\2\2\7\30 \'/\66")
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
    RULE_list_type = 2
    RULE_map_type = 3
    RULE_pair = 4

    ruleNames =  [ "start", "element", "list_type", "map_type", "pair" ]

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
            self.state = 10
            self.element()
            self.state = 11
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
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZishParser.BOOL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.match(ZishParser.BOOL)
                pass
            elif token in [ZishParser.NULL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(ZishParser.NULL)
                pass
            elif token in [ZishParser.TIMESTAMP]:
                self.enterOuterAlt(localctx, 3)
                self.state = 15
                self.match(ZishParser.TIMESTAMP)
                pass
            elif token in [ZishParser.INTEGER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 16
                self.match(ZishParser.INTEGER)
                pass
            elif token in [ZishParser.DECIMAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 17
                self.match(ZishParser.DECIMAL)
                pass
            elif token in [ZishParser.STRING]:
                self.enterOuterAlt(localctx, 6)
                self.state = 18
                self.match(ZishParser.STRING)
                pass
            elif token in [ZishParser.BLOB]:
                self.enterOuterAlt(localctx, 7)
                self.state = 19
                self.match(ZishParser.BLOB)
                pass
            elif token in [ZishParser.LIST_START]:
                self.enterOuterAlt(localctx, 8)
                self.state = 20
                self.list_type()
                pass
            elif token in [ZishParser.MAP_START]:
                self.enterOuterAlt(localctx, 9)
                self.state = 21
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
        self.enterRule(localctx, 4, self.RULE_list_type)
        self._la = 0 # Token type
        try:
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.match(ZishParser.LIST_START)
                self.state = 25
                self.element()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZishParser.COMMA:
                    self.state = 26
                    self.match(ZishParser.COMMA)
                    self.state = 27
                    self.element()
                    self.state = 32
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 33
                self.match(ZishParser.LIST_FINISH)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(ZishParser.LIST_START)
                self.state = 36
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
        self.enterRule(localctx, 6, self.RULE_map_type)
        self._la = 0 # Token type
        try:
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(ZishParser.MAP_START)
                self.state = 40
                self.pair()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZishParser.COMMA:
                    self.state = 41
                    self.match(ZishParser.COMMA)
                    self.state = 42
                    self.pair()
                    self.state = 47
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 48
                self.match(ZishParser.MAP_FINISH)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(ZishParser.MAP_START)
                self.state = 51
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

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZishParser.ElementContext)
            else:
                return self.getTypedRuleContext(ZishParser.ElementContext,i)


        def COLON(self):
            return self.getToken(ZishParser.COLON, 0)

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
        self.enterRule(localctx, 8, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.element()
            self.state = 55
            self.match(ZishParser.COLON)
            self.state = 56
            self.element()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





