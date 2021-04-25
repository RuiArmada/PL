import ply.yacc as yacc

from shop_list_lex import tokens

def p_grammar(p):
    """"
        list : categories

        categories : category
                   | categories category

        category : name ':' products

        name : ID

        products : product
                 | products procuts

        product : '*' INT ';' STR ';' FLOAT ';' INT
    """

def p_error(p):
    print('Syntax ERROR')

parser = yacc.yacc()

import sys

for line in sys.stdin:
    parser.parse(line)
