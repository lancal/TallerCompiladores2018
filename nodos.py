from symbol_Table import *
from scanner import  *

import re

erroresSemanticos1 = []
erroresSemanticos2 = []


st = symbolTable()

class Nodo():
    pass

class Program(Nodo):
    def __init__(self, statement_list_p):

        self.statement_list = statement_list_p
        self.nombre = 'Program '

    def accept(self, visitor):

        visitor.visit_program(self)

    def accept2(self,visitor2,symbol_Table):

       visitor2.visit_program(self,symbol_Table)

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

    def accept(self,visitor):
        visitor.visit_nodoSentenciaComp(self)

class nodoSentenciaSeleccion(Nodo):

    def __init__(self,expresion_p,sentencia_p,is_else = False,sentencia_p2=None):
        self.expresion_p = expresion_p
        self.sentencia_p = sentencia_p
        self.is_else = is_else
        self.sentencia_p2 = sentencia_p2
        self.nombre = 'Sentencia Seleccion '

    def accept(self,visitor):
        visitor.visit_nodoSentenciaSeleccion(self)

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

class nodoSentenciaRetorno(Nodo):

    def __init__(self,thereis_expression = False, expresion_p = None):

        self.thereis_expression = thereis_expression
        self.expresion_p = expresion_p
        self.nombre = 'Sentencia Retorno '
        self.nombre2 =  'RET ;'

    def accept(self,visitor):
        visitor.visit_nodoSentenciaRetorno(self)

class nodoExpresion(Nodo):

    def __init__(self,var_p = None,expresion_p2 = None , expresion_negada_p = None):
        self.var_p = var_p
        self.expresion_p2 = expresion_p2
        self.expresion_negada_p = expresion_negada_p
        self.nombre = 'Expresion '

    def accept(self,visitor):
        visitor.visit_nodoExpresion(self)

class nodoVar(Nodo):

    def __init__(self,id_t, is_vec_access=False, expresion_p=None):
    #def __init__(self, id_t, expresion_p):

        self.id_t = id_t
        self.is_vec_access = is_vec_access
        self.expresion_p = expresion_p
        self.nombre = 'Var '

    def accept(self,visitor):
        visitor.visit_nodoVar(self)

class nodoExpresionNegada(Nodo):

    def __init__(self,expresion_logica_p):

        #self.not_bracket = not_bracket
        self.expresion_logica_p = expresion_logica_p
        self.nombre = 'Expresion Negada '
        #self.nombre2 = 'Expresion Negada ![]'

    def accept(self,visitor):
        visitor.visit_nodoExpresionNegada(self)

class nodoExpresionLogica(Nodo):

    def __init__(self,thereis_exp_log = False, expresion_logica_p = None , expresion_simple_p = None):

        self.thereis_exp_log =thereis_exp_log
        self.expresion_logica_p = expresion_logica_p
        #self.thereis_exp_sim = thereis_exp_sim
        self.expresion_simple_p = expresion_simple_p
        self.nombre = 'Expresion Logica '

    def accept(self,visitor):
        visitor.visit_nodoExpresion_logica(self)

class nodoVacio():

    def __init__(self):

        self.nombre = 'vacio'

    def accept(self,visitor):
        visitor.visit_nodoVacio(self)

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

class nodoNUM(Nodo):

    def __init__(self, num_t):
        self.num_t = num_t
        self.nombre = 'NUM '

    def accept(self, visitor):
        visitor.visit_nodoNUM(self)

class nodoInvocacion(Nodo):

    def __init__(self,id_t, argumentos_p):

        self.id_t = id_t
        self.argumentos_p = argumentos_p
        self.nombre = 'Invocacion '

    def accept(self,visitor):
        visitor.visit_nodoInvocacion(self)

def getTable():

    return st

def getesp():
    return erroresSemanticos1

def getess():
    return erroresSemanticos2

