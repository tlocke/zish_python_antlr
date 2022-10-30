# Generated from Zish.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,64,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,1,1,1,1,1,1,1,3,1,20,8,1,1,2,1,2,1,3,1,3,1,3,1,3,5,3,28,
        8,3,10,3,12,3,31,9,3,1,3,3,3,34,8,3,1,3,1,3,1,3,1,3,3,3,40,8,3,1,
        4,1,4,1,4,1,4,5,4,46,8,4,10,4,12,4,49,9,4,1,4,3,4,52,8,4,1,4,1,4,
        1,4,1,4,3,4,58,8,4,1,5,1,5,1,5,1,5,1,5,0,0,6,0,2,4,6,8,10,0,1,1,
        0,9,14,66,0,12,1,0,0,0,2,19,1,0,0,0,4,21,1,0,0,0,6,39,1,0,0,0,8,
        57,1,0,0,0,10,59,1,0,0,0,12,13,3,2,1,0,13,14,5,0,0,1,14,1,1,0,0,
        0,15,20,3,4,2,0,16,20,3,6,3,0,17,20,3,8,4,0,18,20,5,8,0,0,19,15,
        1,0,0,0,19,16,1,0,0,0,19,17,1,0,0,0,19,18,1,0,0,0,20,3,1,0,0,0,21,
        22,7,0,0,0,22,5,1,0,0,0,23,24,5,1,0,0,24,29,3,2,1,0,25,26,5,3,0,
        0,26,28,3,2,1,0,27,25,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,
        1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,32,34,5,3,0,0,33,32,1,0,0,0,
        33,34,1,0,0,0,34,35,1,0,0,0,35,36,5,2,0,0,36,40,1,0,0,0,37,38,5,
        1,0,0,38,40,5,2,0,0,39,23,1,0,0,0,39,37,1,0,0,0,40,7,1,0,0,0,41,
        42,5,4,0,0,42,47,3,10,5,0,43,44,5,3,0,0,44,46,3,10,5,0,45,43,1,0,
        0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,51,1,0,0,0,49,47,
        1,0,0,0,50,52,5,3,0,0,51,50,1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,0,
        53,54,5,5,0,0,54,58,1,0,0,0,55,56,5,4,0,0,56,58,5,5,0,0,57,41,1,
        0,0,0,57,55,1,0,0,0,58,9,1,0,0,0,59,60,3,4,2,0,60,61,5,6,0,0,61,
        62,3,2,1,0,62,11,1,0,0,0,7,19,29,33,39,47,51,57
    ]

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
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(ZishParser.KeyContext,0)


        def list_type(self):
            return self.getTypedRuleContext(ZishParser.List_typeContext,0)


        def map_type(self):
            return self.getTypedRuleContext(ZishParser.Map_typeContext,0)


        def NULL(self):
            return self.getToken(ZishParser.NULL, 0)

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
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11, 12, 13, 14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.key()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.list_type()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 17
                self.map_type()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 18
                self.match(ZishParser.NULL)
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(ZishParser.BOOL, 0)

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
            self.state = 21
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 32256) != 0):
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
        __slots__ = 'parser'

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
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(ZishParser.LIST_START)
                self.state = 24
                self.element()
                self.state = 29
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 25
                        self.match(ZishParser.COMMA)
                        self.state = 26
                        self.element() 
                    self.state = 31
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 32
                    self.match(ZishParser.COMMA)


                self.state = 35
                self.match(ZishParser.LIST_FINISH)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.match(ZishParser.LIST_START)
                self.state = 38
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
        __slots__ = 'parser'

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
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(ZishParser.MAP_START)
                self.state = 42
                self.pair()
                self.state = 47
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 43
                        self.match(ZishParser.COMMA)
                        self.state = 44
                        self.pair() 
                    self.state = 49
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 50
                    self.match(ZishParser.COMMA)


                self.state = 53
                self.match(ZishParser.MAP_FINISH)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(ZishParser.MAP_START)
                self.state = 56
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
        __slots__ = 'parser'

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
            self.state = 59
            self.key()
            self.state = 60
            self.match(ZishParser.COLON)
            self.state = 61
            self.element()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





