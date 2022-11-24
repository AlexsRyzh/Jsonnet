from sly import Lexer


class FLexer(Lexer):
    tokens = {STRING, INTEGER, ID, START, LET, FOR, FROM, TO, LIST, ITEM}

    literals = {"(", ")"}

    INTEGER = r'\d+'
    STRING = r'"[^"]*"'
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['start'] = START
    ID['let'] = LET
    ID['for'] = FOR
    ID['from'] = FROM
    ID['to'] = TO
    ID['list'] = LIST
    ID['item'] = ITEM


    @_(r'\d+')
    def INTEGER(self, t):
        t.value = int(t.value)
        return t

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    ignore_space = r'\s'
    ignore_comment = r'\#.*'


    def error(self, t):
        self.index +=1
        raise Exception(f'Line {self.lineno}: Bad character {t.value[0]}')
