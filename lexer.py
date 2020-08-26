# TOKENS

_INT = 'INT'
_FLOAT = 'FLOAT'
_PLUS = 'PLUS'
_SUBTRACT = 'MINUS'
_DIVIDE = 'DIV'
_MULTIPLY = 'MUL'
_LPARENTHENSES = 'LPAREN'
_RPARENTHENSES = 'RPAREN'

# Constants

DIGITS = '0123456789'


# Error

class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        error = f'{self.error_name}: {self.details}\n'
        error += f'File {self.pos_start.fn}, line {self.pos_start.lineNum + 1}'
        return error


class IllegalCharacterError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, "Invalid Character found", details)


class Position:
    def __init__(self, idx, lineNum, colNum, fn, ftxt):
        self.idx = idx
        self.lineNum = lineNum
        self.colNum = colNum
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, curr_char):
        self.idx += 1
        self.colNum += 1

        if curr_char == '\n':
            self.lineNum += 1
            self.colNum = 0

        return self

    def copy(self):
        return Position(self.idx, self.lineNum, self.colNum, self.fn, self.ftxt)


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    # representation method for terminal window.
    def __repr__(self):
        if self.value:
            return f'{self.type}: {self.value}'
        return f'{self.type}'


class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.curr_position = Position(-1, 0, -1, fn, text)
        self.curr_char = None
        self.advance()

    # advancing to the next token method.
    def advance(self):
        self.curr_position.advance(self.curr_char)
        if self.curr_position.idx < len(self.text):
            self.curr_char = self.text[self.curr_position.idx]
        else:
            self.curr_char = None

    # making token method.
    def make_tokens(self):
        tokens = []
        # while None is not reached.
        while self.curr_char != None:
            # checking if character is space or tab.
            if self.curr_char in ' \t':
                self.advance()
            elif self.curr_char in DIGITS:
                tokens.append(self.make_number())
            elif self.curr_char == '+':
                tokens.append(Token(_PLUS))
                self.advance()
            elif self.curr_char == '-':
                tokens.append(Token(_SUBTRACT))
                self.advance()
            elif self.curr_char == '*':
                tokens.append(Token(_MULTIPLY))
                self.advance()
            elif self.curr_char == '/':
                tokens.append(Token(_DIVIDE))
                self.advance()
            elif self.curr_char == '(':
                tokens.append(Token(_LPARENTHENSES))
                self.advance()
            elif self.curr_char == ')':
                tokens.append(Token(_RPARENTHENSES))
                self.advance()
            else:
                pos_start = self.curr_position.copy()
                char = self.curr_char
                self.advance()
                return [], IllegalCharacterError(pos_start, self.curr_position, "'" + char + "'")

        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0  # for decimal

        while self.curr_char != None and self.curr_char in DIGITS + '.':
            if self.curr_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
                num_str += '.'

            else:
                num_str += self.curr_char

            self.advance()
        if dot_count == 0:
            return Token(_INT, int(num_str))
        else:
            return Token(_FLOAT, float(num_str))

# RUN


def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()

    return tokens, error
