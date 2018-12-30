from symbol_Table import *
from scanner import  *

import re

erroresSemanticos1 = []
erroresSemanticos2 = []

class Nodo():
    pass

class Program(Nodo):
    def __init__(self, statement_list_p):

        self.statement_list = statement_list_p
        self.nombre = 'Program '

    def accept(self, visitor):

        visitor.visit_program(self)

    def accept2(self,visitor,symbol_Table):

        visitor.visit_program(self,symbol_Table)

class nodoDeclaracionVar(Nodo):

    #global NUM_t

    def __init__(self,def_tipo_p,ID_t,thereis_num = False,NUM_t=None):

        self.def_tipo_p = def_tipo_p
        self.ID_t = ID_t
        self.thereis_num = thereis_num
        self.NUM_t = NUM_t
        self.nombre = 'Declaracion Var '
        self.patron = re.compile(r'vacuo',re.I)
        self.arreglo = self.patron.findall(self.def_tipo_p)
        self.nombre2 = 'Error Nodo Declaracion Var '

        #print(self.arreglo)

        if not self.arreglo:

            pass
            #print('pass')

        else:

            if self.def_tipo_p == self.arreglo[0]:

                erroresSemanticos1.append("Variable " + self.ID_t + " declarada no puede ser del tipo " + self.arreglo[0])

    def accept(self, visitor):
        visitor.visit_nodoDeclaracionVar(self)

    def accept2(self, visitor,symbol_Table):
        visitor.visit_nodoDeclaracionVar(self,symbol_Table)


class nodoDeclaracionFun(Nodo):

    def __init__(self,def_tipo_p,ID_t,parametros_p,sentencia_comp_p):

        self.def_tipo_p = def_tipo_p
        self.ID_t = ID_t
        self.parametros_p = parametros_p
        self.sentencia_comp_p = sentencia_comp_p
        self.nombre = 'Declaracion Fun '
        self.nombre2 = 'Error Nodo Declaracion Fun '

    def accept(self,visitor):

        visitor.visit_nodoDeclaracionFun(self)

    def accept2(self, visitor,symbol_Table):

        visitor.visit_nodoDeclaracionFun(self,symbol_Table)

class nodoParam(Nodo):

    def __init__(self,def_tipo_p,thereis_ID = False,ID_t = None,Lt_Rt = None):

        self.def_tipo_p = def_tipo_p
        self.ID_t = ID_t
        self.thereis_ID = thereis_ID
        self.Lt_Rt = Lt_Rt
        self.nombre = 'Param '
        self.nombre2 = 'Error Param '

    def accept(self,visitor):
        visitor.visit_nodoParam(self)

    def accept2(self, visitor,symbol_Table):

        visitor.visit_nodoParam(self,symbol_Table)


class nodoSentenciaComp(Nodo):

    def __init__(self,declaraciones_locales_p,lista_sentencias_p,is_vacio=False,vacio_t=None):

        self.declaraciones_locales_p = declaraciones_locales_p
        self.lista_sentencias_p = lista_sentencias_p
        self.is_vacio = is_vacio
        self.vacio_t = vacio_t
        self.nombre = 'Sentencia Comp '
        self.nombre2 = 'Error Sentencia Comp'

    def accept(self,visitor):
        visitor.visit_nodoSentenciaComp(self)

    def accept2(self, visitor,symbol_Table):

        visitor.visit_nodoSentenciaComp(self,symbol_Table)

class nodoSentenciaSeleccion(Nodo):

    def __init__(self,expresion_p,sentencia_p,is_else = False,sentencia_p2=None):
        self.expresion_p = expresion_p
        self.sentencia_p = sentencia_p
        self.is_else = is_else
        self.sentencia_p2 = sentencia_p2
        self.nombre = 'Sentencia Seleccion '

    def accept(self,visitor):
        visitor.visit_nodoSentenciaSeleccion(self)

    def accept2(self, visitor,symbol_Table):

        visitor.visit_nodoSentenciaSeleccion(self,symbol_Table)

class nodoSentenciaIteracion(Nodo):

    def __init__(self,thereis_expresion = False,expresion_p=None,thereis_sentencia = False,sentencia_p=None,
                 thereis_sentencia_comp = False,sentencia_comp_p = None):

        self.thereis_expresion = thereis_expresion
        self.expresion_p = expresion_p
        self.thereis_sentencia = thereis_sentencia
        self.sentencia_p = sentencia_p
        self.thereis_sentencia_comp = thereis_sentencia_comp
        self.sentencia_comp_p = sentencia_comp_p
        self.nombre = 'Sentencia Iteracion '

    def accept(self,visitor):
        visitor.visit_nodoSentenciaIteracion(self)

    def accept2(self, visitor,symbol_Table):

        visitor.visit_nodoSentenciaIteracion(self,symbol_Table)

class nodoSentenciaRetorno(Nodo):

    def __init__(self,thereis_expression = False, expresion_p = None):

        self.thereis_expression = thereis_expression
        self.expresion_p = expresion_p
        self.nombre = 'Sentencia Retorno '
        self.nombre2 =  'RET ;'

    def accept(self,visitor):
        visitor.visit_nodoSentenciaRetorno(self)

    def accept2(self, visitor,symbol_Table):

        visitor.visit_nodoSentenciaRetorno(self,symbol_Table)

class nodoExpresion(Nodo):

    def __init__(self,var_p = None,expresion_p = None , expresion_negada_p = None, semicolon_t = None):
        self.var_p = var_p
        self.expresion_p = expresion_p
        self.expresion_negada_p = expresion_negada_p
        self.semicolon_t = semicolon_t
        self.nombre = 'Expresion '

    def accept(self,visitor):
        visitor.visit_nodoExpresion(self)

    def accept2(self, visitor, symbol_Table):

        visitor.visit_nodoExpresion(self, symbol_Table)


class nodoVar(Nodo):

    def __init__(self,ID_t=None, is_vec_access=False, expresion_p=None):
    #def __init__(self, id_t, expresion_p):

        self.ID_t = ID_t
        self.is_vec_access = is_vec_access
        self.expresion_p = expresion_p
        self.nombre = 'Var '

    def accept(self,visitor):
        visitor.visit_nodoVar(self)

    def accept2(self, visitor, symbol_Table):

        visitor.visit_nodoVar(self, symbol_Table)

class nodoExpresionNegada(Nodo):

    def __init__(self,expresion_logica_p):

        #self.not_bracket = not_bracket
        self.expresion_logica_p = expresion_logica_p
        self.nombre = 'Expresion Negada '
        #self.nombre2 = 'Expresion Negada ![]'

    def accept(self,visitor):
        visitor.visit_nodoExpresionNegada(self)

    def accept2(self, visitor, symbol_Table):

        visitor.visit_nodoExpresionNegada(self, symbol_Table)

class nodoExpresionLogica(Nodo):

    def __init__(self,thereis_exp_log = False, expresion_logica_p = None , expresion_simple_p = None):

        self.thereis_exp_log =thereis_exp_log
        self.expresion_logica_p = expresion_logica_p
        #self.thereis_exp_sim = thereis_exp_sim
        self.expresion_simple_p = expresion_simple_p
        self.nombre = 'Expresion Logica '

    def accept(self,visitor):
        visitor.visit_nodoExpresionLogica(self)

    def accept2(self, visitor, symbol_Table):

        visitor.visit_nodoExpresionLogica(self, symbol_Table)

class nodoVacio():

    def __init__(self):

        self.nombre = 'vacio'

    def accept(self,visitor):
        visitor.visit_nodoVacio(self)

    def accept2(self, visitor, symbol_Table):

        visitor.visit_nodoVacio(self, symbol_Table)

class nodoBinarioOP(Nodo):

    def __init__(self,is_rama = False,ramaIzq_p=None, ramaDer_p=None, operacion_p=None,nombre2 = None):

        self.is_rama = is_rama
        self.ramaIzq_p = ramaIzq_p
        self.ramaDer_p = ramaDer_p
        self.operacion_p = operacion_p
        self.nombre = 'Nodo Binario Op '
        self.nombre2 = nombre2

    def accept(self,visitor):
        visitor.visit_nodoBinarioOP(self)

    def accept2(self, visitor, symbol_Table):

        visitor.visit_nodoBinarioOP(self, symbol_Table)

class nodoNUM(Nodo):

    def __init__(self, NUM_t):
        self.NUM_t = NUM_t
        self.nombre = 'NUM '

    def accept(self, visitor):
        visitor.visit_nodoNUM(self)

    def accept2(self, visitor, symbol_Table):

        visitor.visit_nodoNUM(self, symbol_Table)

class nodoInvocacion(Nodo):

    def __init__(self,ID_t, argumentos_p):

        self.ID_t = ID_t
        self.argumentos_p = argumentos_p
        self.nombre = 'Invocacion '

    def accept(self,visitor):
        visitor.visit_nodoInvocacion(self)

    def accept2(self, visitor, symbol_Table):

        visitor.visit_nodoInvocacion(self, symbol_Table)


def isDeclared(listSymbol, listaNodosActual, node):
    cont = 0
    for lna in listaNodosActual:
        if lna.identificador == node.ident:
            cont += 1
    if cont == 0:
        for ls in listSymbol:
            if ls.identificador == node.ident and ls.getsymbolTable() is None:
                cont += 1
                break
    if cont == 0:
        erroresSemanticos1.append("Error Semántico, variable "+node.ident+" no declarada")

def isInitialized(listaasignaciones, node):
    if len(listaasignaciones) > 0:
        cont = 0
        for la in listaasignaciones:
            if la.var.expression is not None:
                temp = nodoVar(None,False, None)
                temp.ident = la.var.ident + "["+la.var.expression.number+"]"

                if temp.ident == node.ident:
                    cont += 1
            else:
                if la.var.ident == node.ident:
                    cont += 1
        if cont == 0:
            erroresSemanticos2.append("Error de tipo, variable "+node.ident+" no inicializada")
    else:
        erroresSemanticos2.append("Error de tipo, variable "+node.ident+" no inicializada")


#def getTable():

 #   return st

def getesp():
    return erroresSemanticos1

def getess():
    return erroresSemanticos2

