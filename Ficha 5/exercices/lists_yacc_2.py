import ply.yacc as yacc

from lists_lex import tokens

def p_inv_func(p):
    "inv_func : ID list"
    print('Parsing Completed!')
    #print('Words                   | ', p.parser.word)
    #print('Numbers                 | ', p.parser.num)
    #print('Toltal Sum of Numbers   | ', p.parser.sum)
    #print('List of Words           | ', p.parser.list_word)
    #print('List                    | ', p.parser.list)
    p[0] = p[2]

def p_list(p):
    "list : PE inside PD"
    p[0] = p[2]

def p_inside_empty(p):
    "inside : "
    p[0] = []

def p_inside_elements(p):
    "inside : elements"
    p[0] = p[1]

def p_elements_element(p):
    "elements : element"
    p[0] = [p[1]]

def p_elements_virg(p):
    "elements : elements VIRG element"
    p[0] = [p[1]] + p[3]

def p_element_ID(p):
    "element : ID"
    #parser.word += 1
    #parser.list_word.append([1])
    p[0] = p[1]

def p_element_NUM(p):
    "element : NUM"
    #parser.num += 1
    #valor = p[1]
    #p.parser.sum += valor
    #p.parser.list.appen([1])
    p[0] = p[1]

def p_error(p):
    print('Syntax ERROR')

parser = yacc.yacc()
#parser.word = 0
#parser.num = 0
#parser.sum = 0
#parser.list_word = []
#parser.list = []

import sys

for line in sys.stdin:
    result = parser.parse(line)
    print('Result of Parsing| ', result)
    #parser.word = 0
    #parser.num = 0
    #parser.sum = 0
    #parser.list_word = []
    #parser.list = []
