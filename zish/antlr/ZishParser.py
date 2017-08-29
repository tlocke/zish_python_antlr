# Generated from Zish.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("M\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\30\n\3\3\4\3\4\3")
        buf.write("\4\3\4\7\4\36\n\4\f\4\16\4!\13\4\3\4\3\4\3\4\3\4\5\4\'")
        buf.write("\n\4\3\5\3\5\3\5\3\5\7\5-\n\5\f\5\16\5\60\13\5\3\5\3\5")
        buf.write("\3\5\3\5\5\5\66\n\5\3\6\3\6\3\6\3\6\7\6<\n\6\f\6\16\6")
        buf.write("?\13\6\3\6\3\6\3\6\3\6\5\6E\n\6\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\2\2\t\2\4\6\b\n\f\16\2\3\3\2\f\23\2N\2\20\3\2\2")
        buf.write("\2\4\27\3\2\2\2\6&\3\2\2\2\b\65\3\2\2\2\nD\3\2\2\2\fF")
        buf.write("\3\2\2\2\16J\3\2\2\2\20\21\5\4\3\2\21\22\7\2\2\3\22\3")
        buf.write("\3\2\2\2\23\30\5\16\b\2\24\30\5\n\6\2\25\30\5\6\4\2\26")
        buf.write("\30\5\b\5\2\27\23\3\2\2\2\27\24\3\2\2\2\27\25\3\2\2\2")
        buf.write("\27\26\3\2\2\2\30\5\3\2\2\2\31\32\7\3\2\2\32\37\5\4\3")
        buf.write("\2\33\34\7\7\2\2\34\36\5\4\3\2\35\33\3\2\2\2\36!\3\2\2")
        buf.write("\2\37\35\3\2\2\2\37 \3\2\2\2 \"\3\2\2\2!\37\3\2\2\2\"")
        buf.write("#\7\4\2\2#\'\3\2\2\2$%\7\3\2\2%\'\7\4\2\2&\31\3\2\2\2")
        buf.write("&$\3\2\2\2\'\7\3\2\2\2()\7\5\2\2).\5\16\b\2*+\7\7\2\2")
        buf.write("+-\5\16\b\2,*\3\2\2\2-\60\3\2\2\2.,\3\2\2\2./\3\2\2\2")
        buf.write("/\61\3\2\2\2\60.\3\2\2\2\61\62\7\6\2\2\62\66\3\2\2\2\63")
        buf.write("\64\7\5\2\2\64\66\7\6\2\2\65(\3\2\2\2\65\63\3\2\2\2\66")
        buf.write("\t\3\2\2\2\678\7\b\2\28=\5\f\7\29:\7\7\2\2:<\5\f\7\2;")
        buf.write("9\3\2\2\2<?\3\2\2\2=;\3\2\2\2=>\3\2\2\2>@\3\2\2\2?=\3")
        buf.write("\2\2\2@A\7\t\2\2AE\3\2\2\2BC\7\b\2\2CE\7\t\2\2D\67\3\2")
        buf.write("\2\2DB\3\2\2\2E\13\3\2\2\2FG\5\16\b\2GH\7\n\2\2HI\5\4")
        buf.write("\3\2I\r\3\2\2\2JK\t\2\2\2K\17\3\2\2\2\t\27\37&.\65=D")
        return buf.getvalue()


class ZishParser ( Parser ):

    grammarFileName = "Zish.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'('", "')'", "','", "'{'", 
                     "'}'", "':'", "<INVALID>", "'null'" ]

    symbolicNames = [ "<INVALID>", "LIST_START", "LIST_FINISH", "SET_START", 
                      "SET_FINISH", "COMMA", "MAP_START", "MAP_FINISH", 
                      "COLON", "WS", "NULL", "BOOL", "TIMESTAMP", "INTEGER", 
                      "DECIMAL", "FLOAT", "STRING", "BLOB" ]

    RULE_start = 0
    RULE_element = 1
    RULE_list_type = 2
    RULE_set_type = 3
    RULE_map_type = 4
    RULE_pair = 5
    RULE_key = 6

    ruleNames =  [ "start", "element", "list_type", "set_type", "map_type", 
                   "pair", "key" ]

    EOF = Token.EOF
    LIST_START=1
    LIST_FINISH=2
    SET_START=3
    SET_FINISH=4
    COMMA=5
    MAP_START=6
    MAP_FINISH=7
    COLON=8
    WS=9
    NULL=10
    BOOL=11
    TIMESTAMP=12
    INTEGER=13
    DECIMAL=14
    FLOAT=15
    STRING=16
    BLOB=17

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
            self.state = 14
            self.element()
            self.state = 15
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


        def map_type(self):
            return self.getTypedRuleContext(ZishParser.Map_typeContext,0)


        def list_type(self):
            return self.getTypedRuleContext(ZishParser.List_typeContext,0)


        def set_type(self):
            return self.getTypedRuleContext(ZishParser.Set_typeContext,0)


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
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZishParser.NULL, ZishParser.BOOL, ZishParser.TIMESTAMP, ZishParser.INTEGER, ZishParser.DECIMAL, ZishParser.FLOAT, ZishParser.STRING, ZishParser.BLOB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.key()
                pass
            elif token in [ZishParser.MAP_START]:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.map_type()
                pass
            elif token in [ZishParser.LIST_START]:
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.list_type()
                pass
            elif token in [ZishParser.SET_START]:
                self.enterOuterAlt(localctx, 4)
                self.state = 20
                self.set_type()
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
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(ZishParser.LIST_START)
                self.state = 24
                self.element()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZishParser.COMMA:
                    self.state = 25
                    self.match(ZishParser.COMMA)
                    self.state = 26
                    self.element()
                    self.state = 31
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 32
                self.match(ZishParser.LIST_FINISH)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(ZishParser.LIST_START)
                self.state = 35
                self.match(ZishParser.LIST_FINISH)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Set_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET_START(self):
            return self.getToken(ZishParser.SET_START, 0)

        def key(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZishParser.KeyContext)
            else:
                return self.getTypedRuleContext(ZishParser.KeyContext,i)


        def SET_FINISH(self):
            return self.getToken(ZishParser.SET_FINISH, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZishParser.COMMA)
            else:
                return self.getToken(ZishParser.COMMA, i)

        def getRuleIndex(self):
            return ZishParser.RULE_set_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_type" ):
                listener.enterSet_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_type" ):
                listener.exitSet_type(self)




    def set_type(self):

        localctx = ZishParser.Set_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_set_type)
        self._la = 0 # Token type
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(ZishParser.SET_START)
                self.state = 39
                self.key()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZishParser.COMMA:
                    self.state = 40
                    self.match(ZishParser.COMMA)
                    self.state = 41
                    self.key()
                    self.state = 46
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 47
                self.match(ZishParser.SET_FINISH)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(ZishParser.SET_START)
                self.state = 50
                self.match(ZishParser.SET_FINISH)
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
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(ZishParser.MAP_START)
                self.state = 54
                self.pair()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZishParser.COMMA:
                    self.state = 55
                    self.match(ZishParser.COMMA)
                    self.state = 56
                    self.pair()
                    self.state = 61
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 62
                self.match(ZishParser.MAP_FINISH)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(ZishParser.MAP_START)
                self.state = 65
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
            self.state = 68
            self.key()
            self.state = 69
            self.match(ZishParser.COLON)
            self.state = 70
            self.element()
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

        def FLOAT(self):
            return self.getToken(ZishParser.FLOAT, 0)

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
        self.enterRule(localctx, 12, self.RULE_key)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZishParser.NULL) | (1 << ZishParser.BOOL) | (1 << ZishParser.TIMESTAMP) | (1 << ZishParser.INTEGER) | (1 << ZishParser.DECIMAL) | (1 << ZishParser.FLOAT) | (1 << ZishParser.STRING) | (1 << ZishParser.BLOB))) != 0)):
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





