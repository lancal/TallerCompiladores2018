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
    p[0] = nodos.type_esp_id_num(p[1],p[2])

def p_declaracion_var2(p):
    """declaracion_var : def_tipo ID LTCOMMENT NUM RTCOMMENT SEMICOLON"""
    p[0] = nodos.type_esp_id_num(p[1],p[2],p[4])

def p_def_tipo(p):
    """def_tipo : VACUO"""
    p[0] = p[1]

def p_def_tipo2(p):
    """def_tipo : ENT"""
    p[0] = p[1]

def p_declaracion_fun(p):
    """declaracion_fun : def_tipo ID LBRACKET parametros RBRACKET sentencia_comp"""
    p[0] = nodos.def_tipo_id_parametros_sentencia_comp(p[1],p[2],p[4],p[6])

def p_parametros(p):
    """parametros : lista_parametros"""
    p[0] = p[1]

def p_parametros2(p):
    """parametros : VACUO"""
    p[0] = [nodos.nodoParametros(p[1])]


def p_lista_parametros(p):
    """lista_parametros : lista_parametros COMMA param"""
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    if isinstance(p[3], list):
        p[0].extend(p[3])
    else:
        p[0].extend([p[3]])

def p_lista_parametros2(p):
    """lista_parametros : param"""
    p[0] = p[1]

def p_param(p):
    """param : def_tipo ID"""
    p[0] = nodos.nodoParametros(p[1],p[2])

def p_param2(p):
    """param : def_tipo ID LTCOMMENT RTCOMMENT"""
    p[0] = nodos.nodoParametros(p[1], p[2], is_vector=True)

def p_sentencia_comp(p):
    """sentencia_comp : LPARENT declaraciones_locales lista_sentencias"""
    p[0] = nodos.nodoSentenciaComp(p[2],p[3])

def p_declaraciones_locales(p):
    """declaraciones_locales : declaraciones_locales declaraciones_variables"""
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    if isinstance(p[2], list):
        p[0].extend(p[2])
    else:
        p[0].extend([p[2]])

def p_declaraciones_locales2(p):
    """declaraciones_locales : vacio"""
    p[0] = [p[1]]

def p_lista_sentencias(p):
    """lista_sentencias : lista_sentencias sentencia"""
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    if isinstance(p[2], list):
        p[0].extend(p[2])
    else:
        p[0].extend([p[2]])

def p_lista_sentencias2(p):
    """lista_sentencias : vacio"""
    p[0] = [p[1]]

def p_sentencia(p):
    """sentencia : sentencia_expr"""
    p[0] = p[1]

def p_sentencia2(p):
    """sentencia : sentencia_comp"""
    p[0] = p[1]

def p_sentencia3(p):
    """sentencia : sentencia_seleccion"""
    p[0] = p[1]

def p_sentencia4(p):
    """sentencia : sentencia_iteracion"""
    p[0] = p[1]

def p_sentencia5(p):
    """sentencia : sentencia_retorno"""
    p[0] = p[1]

def p_sentencia_expr(p):
    """sentencia_expr : expresion SEMICOLON"""
    p[0] = p[1]

def p_sentencia_expr2(p):
    """sentencia_expr : SEMICOLON"""
    p[0] = p[1]


















def p_vacio(p):
    'vacio :'
    p[0] = nodos.nodoVacio()
    pass

# Errores en la sintaxis.
def p_error(p):
    print('Error de sintaxis! ')
    if p is not None:
        print('Error en el ' + str(p.type) + '\n')
    else:
        print('El archivo de entrada esta vacío\n')



# Build the parser
#parser = yacc.yacc()
parser = yacc.yacc(debug=True,start="programa")


treeFileDot = open('tree.dot', 'w')

with open('sample2.pp', 'r') as arch:
    contents = arch.read()
    result = parser.parse(contents)
    if result is not None:
        visitor_tipos = Visitor()
        nodos.Program.accept(result, visitor_tipos)
        treeFileDot.write(visitor_tipos.ast)
    else:
        treeFileDot.write('Error al realizar el parse.')