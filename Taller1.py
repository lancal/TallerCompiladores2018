import ply.lex as lex
import re


reserved = ['SINO','SI','ENT','RET','MIENTRAS','VACUO','REP','LT','EQ']

tokens = reserved + ['ID','PLUS','MINUS','TIMES','DIVIDE','ASSIGN','LPARENT','RPARENT','LBRACKET','RBRACKET',
                     'LTCOMMENT', 'RTCOMMENT','COMMA','SEMICOLON','AND','NOT','NUMBER','SLCOMMENT']

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




def t_SINO(t):
    r'(?i)sino'
    # El modificador (?i) es para aceptar mayusculas y minusculas.
    return t

def t_SI(t):
    r'(?i)si'
    # El modificador (?i) es para aceptar mayusculas y minusculas.
    return t

def t_ENT(t):
    r'(?i)ent'
    # El modificador (?i) es para aceptar mayusculas y minusculas.
    return t

def t_VACUO(t):
    r'(?i)vacuo'
    # El modificador (?i) es para aceptar mayusculas y minusculas.
    return t

def t_RET(t):
    r'(?i)ret'
    # El modificador (?i) es para aceptar mayusculas y minusculas.
    return t

def t_MIENTRAS(t):
    r'(?i)mientras'
    # El modificador (?i) es para aceptar mayusculas y minusculas.
    return t

def t_REP(t):
    r'(?i)rep'
    # El modificador (?i) es para aceptar mayusculas y minusculas.
    return t

# SLCOMMENT es un comentario de UNA linea.
contComment = 0
def t_SLCOMMENT(t):
    r'\#.+'
    global contComment
    contComment += 1
    return t

def t_NUMBER(t):

    #r'( ([0-7]+\#8) | ([0-9]+) | (([0-9]+)?([a-f]*[0-9]*)+\#16))'

    r'( ([0-7]+\#8) | (([0-9]+)?([a-f]*[0-9]*)+\#16 | ([0-9]+) )  )'

    return t

def t_ID(t):
    #r'([a-zA-Z]){1}([$a-zA-Z0-9])+'
    #r'([a-zA-Z])$?(([a-zA-Z])+$?)*(0-9)*'
    r'( ([a-z])(\$?)([a-zA-Z]+(\$?))*[0-9]* )'

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