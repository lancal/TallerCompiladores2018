import ply.lex as lex
import re
import os
import codecs

reserved = ['ELSE','IF','INT','RETURN','WHILE']

tokens = reserved + ['ID','PLUS','MINUS','TIMES','DIVIDE','LT','EQ','ASSIGN','LPARENT','RPARENT','LBRACKET','RBRACKET',
                     'LTCOMMENT', 'RTCOMMENT','COMMA','SEMICOLON','AND','NOT']

t_ignore = ' \t\n'  # Ignorar esto!
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\++'
t_DIVIDE = r'\--'
t_LT = r'LT'
t_EQ = r'EQ'
t_ASSIGN = r'='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LTCOMMENT = r'<'
t_RTCOMMENT = r'>'
t_COMMA = r','
t_SEMICOLON = r';'
t_AND = '&&'
t_NOT = '!'




def t_ELSE(t):
    r'(?i)else'
    # El modificador (?i) es para aceptar mayusculas y minusculas.
    return t

def t_IF(t):
    r'(?i)if'
    # El modificador (?i) es para aceptar mayusculas y minusculas.
    return t

def t_INT(t):
    r'(?i)int'
    # El modificador (?i) es para aceptar mayusculas y minusculas.
    return t

def t_VOID(t):
    r'(?i)void'
    # El modificador (?i) es para aceptar mayusculas y minusculas.
    return t

def t_RETURN(t):
    r'(?i)return'
    # El modificador (?i) es para aceptar mayusculas y minusculas.
    return t

def t_WHILE(t):
    r'(?i)while'
    # El modificador (?i) es para aceptar mayusculas y minusculas.
    return t

def t_ID(t):
    r'([a-zA-Z]){1}([$a-zA-Z0-9])+'
    #r'([a-zA-Z]$)?(([a-zA-Z])+($)?)*(0-9)*'
    if t.value.upper() in reserved:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    # Salto de linea (contar)
    return t



def t_error(t):
    print("Illegal character '{0}' at line {1}".format(t.value[0], t.lineno))
    # Tratamiento de errores.
    t.lexer.skip(1)


lexer = lex.lex()

with open('sample.txt', 'r') as f:
    contents = f.read()
    lex.input(contents)
    for tok in iter(lex.token, None):
        print( repr(tok.type), repr(tok.value))