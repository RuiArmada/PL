import ply.tex as lex

tokens = [
    'ID',
    'NUM',
    'PE',
    'PD',
    'VIRG'
]

t_ID = r'\w+'
t_PE = r'\('
t_PD = r'\)'
t_VIRG = r','

def t_ID(t):
    r'\w+'
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = '\n\t'

def t_error(t):
    print('Illegal Character: ' + t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()



