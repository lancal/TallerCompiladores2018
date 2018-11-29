# coding=utf-8
import ply.yacc as yacc

from scanner import tokens

import nodos

from dibujar_AST_visitor import Visitor

def p_programa(p):
    """programa : lista_decl """
    p[0] = nodos.Program(p[1])

def p_lista_decl(p):
    """lista_decl : lista_decl declaracion"""
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    if isinstance(p[2], list):
        p[0].extend(p[2])
    else:
        p[0].extend([p[2]])

def p_lista_decl2(p):
    """lista_decl : declaracion"""
    p[0] = p[1]

def p_declaracion(p):
    """declaracion : declaracion_var"""
    p[0] = p[1]

def p_declaracion2(p):
    """declaracion : declaracion_fun"""
    p[0] = p[1]

def p_declaracion_var(p):
    """declaracion_var : def_tipo ID SEMICOLON"""
    p[0] = nodos





# Build the parser
parser = yacc.yacc()

treeFileDot = open('tree.dot', 'w')

with open('sample.pp', 'r') as arch:
    contents = arch.read()
    result = parser.parse(contents)
    if result is not None:
        visitor_tipos = Visitor()
        nodos.Program.accept(result, visitor_tipos)
        treeFileDot.write(visitor_tipos.ast)
    else:
        treeFileDot.write('Error al realizar el parse.')