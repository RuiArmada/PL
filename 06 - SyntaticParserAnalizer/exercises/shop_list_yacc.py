import ply.yacc as yacc

from shop_list_lex import tokens

def p_grammar(p):
    """"
        list : categories

        categories : categories category
        categories :

        category : STR ':' products

        products : product
        products : porducts product
        
        product : '-' cod_Product SEP name_Product SEP price SEP quantity ';'
        
        cod_Product : INT 

        name_Product : STR

        price : FLOAT

        quantity : INT
    """

def p_error(p):
    parser.success = False
    print('Syntax ERROR')

parser = yacc.yacc()
parser.success = True

import sys

for line in sys.stdin:
    parser.parse(line)

if parser.success:
    print('Parsing Complete')
