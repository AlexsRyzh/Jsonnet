import json

from Flexer import FLexer
from FParser import FParser

"""
lessons = lesson lessons | empty
lesson ::= "(" "L" name groups students ")"
group_list ::= "(" "G" groups ")"
groups ::= name groups | empty
student_list ::= "(" "S" students ")"
students ::= student students | empty
student ::= "(" age name name ")"
"""


if __name__ == '__main__':
    lexer = FLexer()
    parser = FParser()

    filename = 'F:\Jsonnet\\new.txt'  # new.txt

    program = open(filename, encoding='utf-8').read()

    tokens = lexer.tokenize(program)
    # for item in tokens:
    #     print(item)

    result = parser.parse(tokens)

    print(parser.parametr)

    print(json.dumps(result, indent=2, ensure_ascii=False))