# coding=utf-8
import ply.yacc as yacc

from scanner import tokens

import nodos

from dibujar_AST_visitor import Visitor

def p_programa(p):
    """programa : lista-decl """
    