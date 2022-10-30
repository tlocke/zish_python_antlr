from base64 import b64decode, b64encode
from collections.abc import Mapping
from datetime import datetime as Datetime, timezone as Timezone
from decimal import Decimal

from antlr4 import CommonTokenStream, InputStream
from antlr4.error import ErrorListener, Errors
from antlr4.tree.Tree import TerminalNodeImpl

import arrow

from zish.antlr.ZishLexer import ZishLexer
from zish.antlr.ZishParser import ZishParser

QUOTE = '"'
UTC_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


class ZishException(Exception):
    pass


class ThrowingErrorListener(ErrorListener.ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Errors.ParseCancellationException(f"line {line}: {column} {msg}")


def load(file_like):
    return loads(file_like.read())


def dump(obj, file_like):
    file_like.write(dumps(obj))


def loads(zish_str):
    lexer = ZishLexer(InputStream(zish_str))
    lexer.removeErrorListeners()
    lexer.addErrorListener(ThrowingErrorListener())
    stream = CommonTokenStream(lexer)
    parser = ZishParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ThrowingErrorListener())

    try:
        tree = parser.start()
    except Errors.ParseCancellationException as e:
        raise ZishException(str(e)) from e

    return parse(tree)


def parse(node):
    # print("parse start")
    # print(str(type(node)))
    # print("node text" + node.getText())
    if isinstance(node, ZishParser.Map_typeContext):
        val = {}
        for child in node.getChildren():
            if isinstance(child, ZishParser.PairContext):
                k, v = [
                    parse(c)
                    for c in child.getChildren()
                    if isinstance(c, (ZishParser.ElementContext, ZishParser.KeyContext))
                ]
                val[k] = v
        return val

    elif isinstance(node, ZishParser.List_typeContext):
        val = []
        for child in node.getChildren():
            if isinstance(child, ZishParser.ElementContext):
                val.append(parse(child))
        return tuple(val)

    elif isinstance(
        node,
        (ZishParser.StartContext, ZishParser.ElementContext, ZishParser.KeyContext),
    ):

        for c in node.getChildren():
            if (
                isinstance(c, TerminalNodeImpl)
                and c.getPayload().type == ZishParser.EOF
            ):
                continue
            return parse(c)

    elif isinstance(node, TerminalNodeImpl):
        token = node.getPayload()
        token_type = token.type
        token_text = token.text

        if token_type == ZishParser.TIMESTAMP:
            try:
                return arrow.get(token_text).datetime
            except arrow.parser.ParserError as e:
                raise ZishException(f"Can't parse the timestamp '{token.text}'.") from e

        elif token_type == ZishParser.NULL:
            return None

        elif token_type == ZishParser.BOOL:
            return token.text == "true"

        elif token_type == ZishParser.INTEGER:
            return int(token.text)

        elif token_type == ZishParser.DECIMAL:
            return Decimal(token.text)

        elif token_type == ZishParser.STRING:
            return unescape(token.text[1:-1])

        elif token_type == ZishParser.BLOB:
            return b64decode(token.text)

        else:
            raise ZishException(f"Don't recognize the token type: {token_type}.")
    else:
        raise ZishException(
            f"Don't know what to do with type {type(node)} with value {node}."
        )


ESCAPES = {
    "0": "\u0000",  # NUL
    "a": "\u0007",  # alert BEL
    "b": "\u0008",  # backspace BS
    "t": "\u0009",  # horizontal tab HT
    "n": "\u000A",  # linefeed LF
    "f": "\u000C",  # form feed FF
    "r": "\u000D",  # carriage return CR
    "v": "\u000B",  # vertical tab VT
    '"': "\u0022",  # double quote
    "'": "\u0027",  # single quote
    "?": "\u003F",  # question mark
    "\\": "\u005C",  # backslash
    "/": "\u002F",  # forward slash
    "\u000D\u000A": "",  # empty string
    "\u000D": "",  # empty string
    "\u000A": "",
}  # empty string


def unescape(escaped_str):
    i = escaped_str.find("\\")
    if i == -1:
        return escaped_str
    else:
        head_str = escaped_str[:i]
        tail_str = escaped_str[i + 1 :]
        for k, v in ESCAPES.items():
            if tail_str.startswith(k):
                return head_str + v + unescape(tail_str[len(k) :])

        for prefix, digits in (("x", 2), ("u", 4), ("U", 8)):
            if tail_str.startswith(prefix):
                hex_str = tail_str[1 : 1 + digits]
                v = chr(int(hex_str, 16))
                return head_str + v + unescape(tail_str[1 + digits :])

        raise ZishException(
            f"Can't find a valid string following the first backslash of "
            f"'{escaped_str}'."
        )


def dumps(obj):
    return _dump(obj, "")


def _dump(obj, indent):
    if isinstance(obj, Mapping):
        new_indent = f"{indent}  "
        b = "".join(
            f"\n{new_indent}{_dump(k, new_indent)}: {_dump(v, new_indent)},"
            for k, v in sorted(obj.items())
        )
        return "{}" if len(b) == 0 else "{" + b + "\n}"
    elif isinstance(obj, bool):
        return "true" if obj else "false"
    elif isinstance(obj, (list, tuple)):
        new_indent = f"{indent}  "
        b = "".join(f"\n{new_indent}{_dump(v, new_indent)}," for v in obj)

        return "[]" if len(b) == 0 else f"[{b}\n{indent}]"
    elif isinstance(obj, (int, float, Decimal)):
        return str(obj)
    elif obj is None:
        return "null"
    elif isinstance(obj, str):
        return QUOTE + obj + QUOTE
    elif isinstance(obj, (bytes, bytearray)):
        return f"'{b64encode(obj).decode()}'"
    elif isinstance(obj, Datetime):
        tzinfo = obj.tzinfo
        if tzinfo is None:
            return f"{obj.isoformat()}-00:00"
        elif tzinfo.utcoffset(obj) == Timezone.utc.utcoffset(obj):
            return obj.strftime(UTC_FORMAT)
        else:
            return obj.isoformat()
    else:
        raise ZishException(f"Type {type(obj)} not recognised.")
