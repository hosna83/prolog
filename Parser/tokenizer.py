from typing import Self
import re

class Tokenizer:
    SPECIAL_TOKENS = [
        #('NUMBER',          r'\d+(\.\d*)?'),  # Integer or decimal number
        ('ASSIGN',          r'='),            # Assignment operator
        ('END',             r';'),            # Statement terminator
        ('FUNCTOR',         r'[a-zA-Z0-9_]+\('), # functors
        ('ID',              r'[a-zA-Z0-9]+'), # Identifiers
        ('L_BRACKET',        r'\['),           # L-Bracket
        ('R_BRACKET',        r'\]'),           # R-Bracket
        #('OP',              r'[+\-*/]'),      # Arithmetic operators
        ('IMPLY',           r'<-'),           # Imply roles
        ('EXCLAMATION',     r' !'),           # Exclamation mark
        ('QUESTION',        r'\?'),           # Question mark
        ('COMMA',           r','),            # Comma
        ('L_PARENTHES',   r'[(]'),            # L-Parentheses   
        ('R_PARENTHES',   r'[)]'),            # R-Parentheses
        ("SPACE",          r' '),             # Space
        ('MISMATCH',        r'.'),            # Any other character 
    ]
    
    def tokenize(self: Self, text: str):
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in self.SPECIAL_TOKENS)
        print(tok_regex)
        for mo in re.finditer(tok_regex, text):
            kind = mo.lastgroup
            value = mo.group()
            if kind == 'NUMBER':
                value = float(value) if '.' in value else int(value)
                yield (kind, value)
                continue
            elif kind == 'MISMATCH':
                raise RuntimeError(f'{value!r} unexpected')
            if kind == 'FUNCTOR':
                yield(kind, value[:-1])
            else:
                yield(kind, value)

def main():
    syntax = "Father1(x, y2)  <- Sister(x, y), 2;"
    tokenizer = Tokenizer()
    for token in tokenizer.tokenize(syntax):
        print(token)

if __name__ == "__main__":
    main()