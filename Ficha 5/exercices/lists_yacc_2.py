import ply.yacc as yacc

from lists_lex import tokens

def p_inv_func(p):
    "inv_func : ID list"
    print('Parsing Completed!')
    print('Words   | ', p.parser.word)
    print('Numbers | ', p.parser.num)

def p_list(p):
    "list : PE inside PD"
    pass

def p_inside_empty(p):
    "inside : "
    pass

def p_inside_elements(p):
    "inside : elements"
    pass

def p_elements_element(p):
    "elements : element"
    pass

def p_elements_virg(p):
    "elements : elements VIRG element"
    pass

def p_element_ID(p):
    "element : ID"
    parser.word += 1
    pass

def p_element_NUM(p):
    "element : NUM"
    parser.num += 1
    pass

def p_error(p):
    print('Syntax ERROR')

parser = yacc.yacc()
parser.word = 0
parser.num = 0

import sys

for line in sys.stdin:
    parser.parse(line)
