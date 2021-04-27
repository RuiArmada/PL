import ply.lex as lex

tokens = (
    'STR',
    'INT',
    'FLOAT',
    'SEP'
)

literals = ['-',',',':',';','*']

t_STR = r'\w+'
t_SEP = r'::'


def t_STR(t):
    r'\"[^\"]+\"'
    t.value = t.value[1:-1]

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \n\t'

def t_error(t):
    print(f"'Illegal caracter {t.value[0]}'")

lexer = lex.lex()

file = open('../files/2Buy.txt')
content = file.read()

lexer.input(content)
for tok in lexer:
    print(tok)
    pass

file.close()
