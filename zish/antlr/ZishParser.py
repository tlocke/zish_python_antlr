# Generated from Zish.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("B\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\5\3\26\n\3\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\7\5\36\n\5\f\5\16\5!\13\5\3\5\5\5$\n\5\3\5\3\5")
        buf.write("\3\5\3\5\5\5*\n\5\3\6\3\6\3\6\3\6\7\6\60\n\6\f\6\16\6")
        buf.write("\63\13\6\3\6\5\6\66\n\6\3\6\3\6\3\6\3\6\5\6<\n\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\3\3\2\13\20\2D\2\16")
        buf.write("\3\2\2\2\4\25\3\2\2\2\6\27\3\2\2\2\b)\3\2\2\2\n;\3\2\2")
        buf.write("\2\f=\3\2\2\2\16\17\5\4\3\2\17\20\7\2\2\3\20\3\3\2\2\2")
        buf.write("\21\26\5\6\4\2\22\26\5\b\5\2\23\26\5\n\6\2\24\26\7\n\2")
        buf.write("\2\25\21\3\2\2\2\25\22\3\2\2\2\25\23\3\2\2\2\25\24\3\2")
        buf.write("\2\2\26\5\3\2\2\2\27\30\t\2\2\2\30\7\3\2\2\2\31\32\7\3")
        buf.write("\2\2\32\37\5\4\3\2\33\34\7\5\2\2\34\36\5\4\3\2\35\33\3")
        buf.write("\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 #\3\2\2\2")
        buf.write('!\37\3\2\2\2"$\7\5\2\2#"\3\2\2\2#$\3\2\2\2$%\3\2\2\2')
        buf.write("%&\7\4\2\2&*\3\2\2\2'(\7\3\2\2(*\7\4\2\2)\31\3\2\2\2")
        buf.write(")'\3\2\2\2*\t\3\2\2\2+,\7\6\2\2,\61\5\f\7\2-.\7\5\2\2")
        buf.write(".\60\5\f\7\2/-\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62")
        buf.write("\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2\64\66\7\5\2\2\65")
        buf.write("\64\3\2\2\2\65\66\3\2\2\2\66\67\3\2\2\2\678\7\7\2\28<")
        buf.write("\3\2\2\29:\7\6\2\2:<\7\7\2\2;+\3\2\2\2;9\3\2\2\2<\13\3")
        buf.write("\2\2\2=>\5\6\4\2>?\7\b\2\2?@\5\4\3\2@\r\3\2\2\2\t\25\37")
        buf.write("#)\61\65;")
        return buf.getvalue()


class ZishParser(Parser):

    grammarFileName = "Zish.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = [
        "<INVALID>",
        "'['",
        "']'",
        "','",
        "'{'",
        "'}'",
        "':'",
        "<INVALID>",
        "'null'",
    ]

    symbolicNames = [
        "<INVALID>",
        "LIST_START",
        "LIST_FINISH",
        "COMMA",
        "MAP_START",
        "MAP_FINISH",
        "COLON",
        "WS",
        "NULL",
        "BOOL",
        "TIMESTAMP",
        "INTEGER",
        "DECIMAL",
        "STRING",
        "BLOB",
    ]

    RULE_start = 0
    RULE_element = 1
    RULE_key = 2
    RULE_list_type = 3
    RULE_map_type = 4
    RULE_pair = 5

    ruleNames = ["start", "element", "key", "list_type", "map_type", "pair"]

    EOF = Token.EOF
    LIST_START = 1
    LIST_FINISH = 2
    COMMA = 3
    MAP_START = 4
    MAP_FINISH = 5
    COLON = 6
    WS = 7
    NULL = 8
    BOOL = 9
    TIMESTAMP = 10
    INTEGER = 11
    DECIMAL = 12
    STRING = 13
    BLOB = 14

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache
        )
        self._predicates = None

    class StartContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(ZishParser.ElementContext, 0)

        def EOF(self):
            return self.getToken(ZishParser.EOF, 0)

        def getRuleIndex(self):
            return ZishParser.RULE_start

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStart"):
                listener.enterStart(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStart"):
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
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(ZishParser.KeyContext, 0)

        def list_type(self):
            return self.getTypedRuleContext(ZishParser.List_typeContext, 0)

        def map_type(self):
            return self.getTypedRuleContext(ZishParser.Map_typeContext, 0)

        def NULL(self):
            return self.getToken(ZishParser.NULL, 0)

        def getRuleIndex(self):
            return ZishParser.RULE_element

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterElement"):
                listener.enterElement(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitElement"):
                listener.exitElement(self)

    def element(self):

        localctx = ZishParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_element)
        try:
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                ZishParser.BOOL,
                ZishParser.TIMESTAMP,
                ZishParser.INTEGER,
                ZishParser.DECIMAL,
                ZishParser.STRING,
                ZishParser.BLOB,
            ]:
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
            elif token in [ZishParser.NULL]:
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
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
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

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterKey"):
                listener.enterKey(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitKey"):
                listener.exitKey(self)

    def key(self):

        localctx = ZishParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_key)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            _la = self._input.LA(1)
            if not (
                (
                    ((_la) & ~0x3F) == 0
                    and (
                        (1 << _la)
                        & (
                            (1 << ZishParser.BOOL)
                            | (1 << ZishParser.TIMESTAMP)
                            | (1 << ZishParser.INTEGER)
                            | (1 << ZishParser.DECIMAL)
                            | (1 << ZishParser.STRING)
                            | (1 << ZishParser.BLOB)
                        )
                    )
                    != 0
                )
            ):
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
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIST_START(self):
            return self.getToken(ZishParser.LIST_START, 0)

        def element(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(ZishParser.ElementContext)
            else:
                return self.getTypedRuleContext(ZishParser.ElementContext, i)

        def LIST_FINISH(self):
            return self.getToken(ZishParser.LIST_FINISH, 0)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(ZishParser.COMMA)
            else:
                return self.getToken(ZishParser.COMMA, i)

        def getRuleIndex(self):
            return ZishParser.RULE_list_type

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterList_type"):
                listener.enterList_type(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitList_type"):
                listener.exitList_type(self)

    def list_type(self):

        localctx = ZishParser.List_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_list_type)
        self._la = 0  # Token type
        try:
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 3, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(ZishParser.LIST_START)
                self.state = 24
                self.element()
                self.state = 29
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 1, self._ctx)
                while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 25
                        self.match(ZishParser.COMMA)
                        self.state = 26
                        self.element()
                    self.state = 31
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input, 1, self._ctx)

                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == ZishParser.COMMA:
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
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAP_START(self):
            return self.getToken(ZishParser.MAP_START, 0)

        def pair(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(ZishParser.PairContext)
            else:
                return self.getTypedRuleContext(ZishParser.PairContext, i)

        def MAP_FINISH(self):
            return self.getToken(ZishParser.MAP_FINISH, 0)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(ZishParser.COMMA)
            else:
                return self.getToken(ZishParser.COMMA, i)

        def getRuleIndex(self):
            return ZishParser.RULE_map_type

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterMap_type"):
                listener.enterMap_type(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitMap_type"):
                listener.exitMap_type(self)

    def map_type(self):

        localctx = ZishParser.Map_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_map_type)
        self._la = 0  # Token type
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 6, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(ZishParser.MAP_START)
                self.state = 42
                self.pair()
                self.state = 47
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 4, self._ctx)
                while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 43
                        self.match(ZishParser.COMMA)
                        self.state = 44
                        self.pair()
                    self.state = 49
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input, 4, self._ctx)

                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == ZishParser.COMMA:
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
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(ZishParser.KeyContext, 0)

        def COLON(self):
            return self.getToken(ZishParser.COLON, 0)

        def element(self):
            return self.getTypedRuleContext(ZishParser.ElementContext, 0)

        def getRuleIndex(self):
            return ZishParser.RULE_pair

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterPair"):
                listener.enterPair(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitPair"):
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
