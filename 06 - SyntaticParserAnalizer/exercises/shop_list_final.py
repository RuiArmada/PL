import sys

import ply.yacc as yacc

from shop_list_lex import tokens

def p_list(p):
    "list : categories"
    print('Total Value: ', p[1])

def p_categories_category(p):
    "categories : categories category"
    p[0] = p[1] + p[2]

def p_categories_empty(p):
    "categories : "
    p[0] = 0

def p_category(p):
    "category : ID ':' products"
    p[0] = p[3]
    if p[1] in p.parser.categories:
        print('Notice: Multiple Categories: ' + p[1])
    else
        p.parser.categories.add(p[1])

def p_products_product(p):
    "products : product"
    p[0] = p[1]

def p_products_products(p):
    "products : products product"
    p[0] = p[1] + p[2]

def p_product(p):
    "product : '-' INT SEP ID SEP FLOAT SEP INT ';'"
    p[0] = p[6] * p[8]
    info = {
        'name' : p[4],
        'price' : p[6],
    }
    if p[2] in p.parser.products:
        if info == p.parser.products[p[2]]:
            print('Notice: Multiple Entries of Product: ', p[2])
        else:
            print('ERROR! Diferent Products with the SAME ID: ', p[2])
    else:
        p.parser.products[p[2]] = info

def p_error(p):
    print('Syntax ERROR')

parser = yacc.yacc()

parser.categories = set()
parser.products = set()

content = ""

for line in sys.stdin:
    content += line
parser.parse(content)