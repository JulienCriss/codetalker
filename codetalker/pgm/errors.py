#!/usr/bin/env python


class CodeTalkerException(Exception):
    pass


class LineError(CodeTalkerException):
    def __init__(self, text, lineno, charno):
        Exception.__init__(self, text + ' at (%d, %d)' % (lineno, charno))
        self.lineno = lineno
        self.charno = charno


class ParseError(LineError):
    pass


class TokenError(LineError):
    def __init__(self, msg, text, lineno, charno):
        tease = b''
        lines = text.splitlines()
        if lineno - 1 < len(lines):
            tease = lines[lineno - 1][charno - 1:charno + 30]
        tease = str(tease)
        Exception.__init__(self, str(msg) + ' at (%d, %d) \'%s\'' % (lineno, charno, tease.encode('unicode_escape')))
        self.lineno = lineno
        self.charno = charno

    pass


class AstError(CodeTalkerException):
    pass


class RuleError(CodeTalkerException):
    pass


class IndentError(CodeTalkerException):
    pass

# vim: et sw=4 sts=4
