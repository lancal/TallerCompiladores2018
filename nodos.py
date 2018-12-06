class Nodo():
    pass

class Program(Nodo):
    def __init__(self, statement_list_p):
        self.statement_list = statement_list_p

    def accept(self, visitor):
        visitor.visit_program(self)

# class Expression(Nodo):
#     def __init__(self, var_p, expression_p):
#         self.var_p = var_p
#         self.expression_p = expression_p
#
#     def accept(self, visitor):
#         visitor.visit_expression(self)
#
#
# class SimpleExpression(Nodo):
#     def __init__(self, additive_expression1_p, relop_t, additive_expression2_p):
#         self.additive_expression1_p = additive_expression1_p
#         self.relop_t = relop_t
#         self.additive_expression2_p = additive_expression2_p
#
#     def accept(self, visitor):
#         visitor.visit_simple_expression(self)
#
#
# class AdditiveExpression(Nodo):
#     def __init__(self, additive_expression_p, addop_t, term_p):
#         self.additive_expression_p = additive_expression_p
#         self.addop_t = addop_t
#         self.term_p = term_p
#
#     def accept(self, visitor):
#         visitor.visit_additive_expression(self)
#
#
# class Term(Nodo):
#     def __init__(self, term_p, mulop_t, factor_p):
#         self.term_p = term_p
#         self.mulop_t = mulop_t
#         self.factor_p = factor_p
#
#     def accept(self, visitor):
#         visitor.visit_term(self)
#
#
# class Num(Nodo):
#     def __init__(self, num_t):
#         self.num_t = num_t
#
#     def accept(self, visitor):
#         visitor.visit_num(self)


class nodoDeclaracionVar(Nodo):

    #global NUM_t

    def __init__(self,def_tipo_p,ID_t,NUM_t=None):

        self.def_tipo_p = def_tipo_p
        self.ID_t = ID_t
        self.NUM_t = NUM_t
        self.nombre = 'Declaracion Var '


    def accept(self, visitor):
        visitor.visit_nodoDeclaracionVar(self)


class nodoDeclaracionFun(Nodo):

    def __init__(self,def_tipo_p,ID_t,parametros_p,sentencia_comp_p):

        self.def_tipo_p = def_tipo_p
        self.ID_t = ID_t
        self.parametros_p = parametros_p
        self.sentencia_comp_p = sentencia_comp_p
        self.nombre = 'Declaracion Fun '

    def accept(self,visitor):

        visitor.visit_nodoDeclaracionFun(self)

# class nodoLista_parametros(Nodo):
#
#     def __init__(self,lista_parametros_p,param_p):
#
#         self.lista_parametros_p = lista_parametros_p
#         self.param_p = param_p
#
#     def accept(self,visitor):
#
#         visitor.visit_nodoLista_parametros(self)

class nodoParametros(Nodo):

    def __init__(self,def_tipo_p,ID_t = None, is_vector = False):

        self.def_tipo_p = def_tipo_p
        self.ID_t = ID_t
        self.is_vector = is_vector
        self.nombre = 'Parametros '

    def accept(self,visitor):
        visitor.visit_nodoParametros(self)


class nodoSentenciaComp(Nodo):

    def __init__(self,declaraciones_locales_p,lista_sentencias_p):

        self.declaraciones_locales_p = declaraciones_locales_p
        self.lista_sentencias_p = lista_sentencias_p
        self.nombre = 'Sentencia Comp '

    def accept(self,visitor):
        visitor.visit_nodoSentenciaComp(self)

class nodoSentenciaSeleccion(Nodo):

    def __init__(self,expresion_p,sentencia_p,is_else = False,sino_sentencia = None):
        self.expresion_p = expresion_p
        self.sentencia_p = sentencia_p
        self.is_else = is_else
        self.else_statement = sino_sentencia
        self.nombre = 'Sentencia Seleccion '

    def accept(self,visitor):
        visitor.visit_nodoSentenciaSeleccion(self)

class nodoSentenciaIteracion(Nodo):

    def __init__(self,expresion_p=None,sentencia_p=None,sentencia_comp_p = None):

        self.expresion_p = expresion_p
        self.sentencia_p = sentencia_p
        self.sentencia_comp_p = sentencia_comp_p
        self.nombre = 'Sentencia Iteracion '

    def accept(self,visitor):
        visitor.visit_nodoSentenciaSeleccion(self)

class nodoSentenciaRetorno(Nodo):

    def __init__(self,thereis_expression = False, expresion_p = None):

        self.thereis_expression = thereis_expression
        self.expresion_p = expresion_p
        self.nombre = 'Sentencia Retorno '

    def accept(self,visitor):
        visitor.visit_nodoSentenciaRetorno(self)

class nodoAssign(Nodo):

    def __init__(self,var_p,expresion_p):
        self.var_p = var_p
        self.expresion_p = expresion_p
        self.nombre = 'Assign '

    def accept(self,visitor):
        visitor.visit_nodoAssign(self)

class nodoVar(Nodo):

    def __init__(self,id_t, is_vec_access=False, expresion_p=None):

        self.id_t = id_t
        self.is_vec_access = is_vec_access
        self.expresion_p = expresion_p
        self.nombre = 'Var '

    def accept(self,visitor):
        visitor.visit_nodoVar(self)

class nodoExpresionNegada(Nodo):

    def __init__(self,expresion_negada_p):

        self.expresion_negada_p = expresion_negada_p
        self.nombre = 'Expresion Negada '

    def accept(self,visitor):
        visitor.visit_nodoExpresionNegada(self)

class nodoExpresionLogica(Nodo):

    def __init__(self,expresion_logica_p = None , expresion_simple_p = None):
        self.expresion_logica_p = expresion_logica_p
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

    def __init__(self,ramaIzq_p, ramaDer_p, operacion_p):

        self.ramaIzq_p = ramaIzq_p
        self.ramaDer_p = ramaDer_p
        self.operacion_p = operacion_p
        self.nombre = 'Nodo Binario Op '

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



