class Visitor(object):
    def __init__(self):
        self.ast = ''
        self.id_program = 0
        self.id_expression_stmt = 0
        self.id_expression = 0
        self.id_simple_expression = 0
        self.id_additive_expression = 0
        self.id_term = 0
        self.id_num = 0
        self.id_ID = 0
        self.id_ID2 = 0
        self.id_declaracion_var= 0
        self.id_def_tipo = 0
        self.id_NUM = 0
        self.id_declaracion_fun = 0
        self.id_parametros = 0
        self.id_sentencia_comp = 0
        self.id_nodo = 0
        self.id_nodoListaParametros = 0
        self.id_nodoSentenciaSeleccion = 0
        self.id_nodoExpresion = 0
        self.id_nodoVar = 0
        self.id_nodoSentenciaRetorno = 0
        self.id_nodoExpresionNegada = 0
        self.id_nodoExpresionLogica = 0
        self.id_nodoBinarioOP = 0
        self.id_nodoNum = 0
        self.id_nodoInvocacion = 0

        self.id_nodoParam = 0

    def visit_program(self, program):
        self.id_program += 1
        id_program = self.id_program

        #print(program.statement_list)
        #print("asdf")

        if program.statement_list is not None:

            if isinstance(program.statement_list,list):

                aux = program.statement_list

            else:

                aux = [program.statement_list]

            #print(aux)
            #print("aux")

            for stmt in aux:

                #print(stmt)
                #print("stmt")

                if stmt is not None:
                    self.ast += '\t"Lista ' + str(id_program) +  '" ' + '-> '
                    stmt.accept(self)
        self.ast = 'digraph G {\n' + self.ast + '}'



    # def visit_expression(self, expression):
    #     self.id_expression += 1
    #     id_expression = self.id_expression
    #     self.ast += '-> "' + 'Asignacion ' + str(id_expression) + '"' + '\n'
    #     self.ast += '\t"' + 'Asignacion ' + str(id_expression) + '" '
    #     expression.var_p.accept(self)
    #     self.ast += '\t"' + 'Asignacion ' + str(id_expression) + '" '
    #     expression.expression_p.accept(self)
    #
    # def visit_simple_expression(self, simple_expresion):
    #     self.id_simple_expression += 1
    #     id_simple_expression = self.id_simple_expression
    #     self.ast += '-> "Comparador ' + str(id_simple_expression) + ': ' + simple_expresion.relop_t + '"' + '\n'
    #     self.ast += '\t"Comparador ' + str(id_simple_expression) + ': ' + simple_expresion.relop_t + '" '
    #     simple_expresion.additive_expression1_p.accept(self)
    #     self.ast += '\t"Comparador ' + str(id_simple_expression) + ': ' + simple_expresion.relop_t + '" '
    #     simple_expresion.additive_expression2_p.accept(self)
    #
    # def visit_additive_expression(self, additive_expresion):
    #     self.id_additive_expression += 1
    #     id_additive_expression = self.id_additive_expression
    #     self.ast += '-> "Signo ' + str(id_additive_expression) + ': ' + additive_expresion.addop_t + '"' + '\n'
    #     self.ast += '\t"Signo ' + str(id_additive_expression) + ': ' + additive_expresion.addop_t + '" '
    #     additive_expresion.additive_expression_p.accept(self)
    #     self.ast += '\t"Signo ' + str(id_additive_expression) + ': ' + additive_expresion.addop_t + '" '
    #     additive_expresion.term_p.accept(self)
    #
    # def visit_term(self, term):
    #     self.id_term += 1
    #     id_term = self.id_term
    #     self.ast += '-> "Signo ' + str(id_term) + ': ' + term.mulop_t + '"' + '\n'
    #     self.ast += '\t"Signo ' + str(id_term) + ': ' + term.mulop_t + '" '
    #     term.term_p.accept(self)
    #     if term.factor_p is not None:
    #         self.ast += '\t"Signo ' + str(id_term) + ': ' + term.mulop_t + '" '
    #         term.factor_p.accept(self)
    #
    # def visit_num(self, num):
    #     self.id_num += 1
    #     id_num = self.id_num
    #     self.ast += '-> "NUM' + str(id_num) + ': ' + num.num_t + '"' + '\n'

    def manyTimes(self,p1,p2,p3):

        #print(p1)
        #print("afuera if many times")

        if p1 is not None:

            #print("adentro if many times")

            if isinstance(p1, list):

                aux = p1

            else:

                aux = [p1]

            print(aux)
            print("aux")

            for x in aux:

                print(x)
                print("x")

                if isinstance(x, str):

                    self.id_nodo += 1
                    id_nodo = self.id_nodo

                    self.ast += '\t' + str(id_nodo) + ' [label="' + x + '"]\n'

                    self.ast += '\t"' + p3 + str(p2) + '" ' + '-> ' + str(id_nodo) + '\n'

                else:

                    print("entro else manytimes")

                    if x.nombre == "vacio":

                        pass

                    else:

                        print(p1)

                        print("entro segundo else instance")
                        self.ast += '\t"' + p3 + str(p2) + '" ' + '-> '
                        x.accept(self)
                    # self.ast += '\t"Declaracion Var ' + str(id_declaracion_var) + '" '\
                    # '-> "def tipo ' + str(id_def_tipo) + ': ' + declaracion_var_p.def_tipo_p + '" ' + '\n'




    def visit_nodoDeclaracionVar(self,declaracion_var_p):


        self.id_declaracion_var+= 1
        id_declaracion_var = self.id_declaracion_var

        self.ast += '"Declaracion Var ' + str(id_declaracion_var) + '"' + '\n'

        #self.id_def_tipo += 1
        #id_def_tipo = self.id_def_tipo


        self.manyTimes(declaracion_var_p.def_tipo_p,id_declaracion_var,declaracion_var_p.nombre)
        self.manyTimes(declaracion_var_p.ID_t, id_declaracion_var,declaracion_var_p.nombre)
        self.manyTimes(declaracion_var_p.NUM_t, id_declaracion_var,declaracion_var_p.nombre)

        # if declaracion_var_p.def_tipo_p is not None:
        #     if isinstance(declaracion_var_p.def_tipo_p, list):
        #
        #         aux = declaracion_var_p.def_tipo_p
        #
        #     else:
        #
        #         aux = [declaracion_var_p.def_tipo_p]
        #
        #     for x in aux:
        #
        #         if isinstance(x, str):
        #
        #             self.id_nodo += 1
        #             id_nodo = self.id_nodo
        #
        #             self.ast += '\t' + str(id_nodo) + ' [label="' + x + '"]\n'
        #
        #             self.ast += '\t"Declaracion Var ' + str(id_declaracion_var)+ '" ' + '-> ' + str(id_nodo) + '\n'
        #
        #         else:
        #
        #             self.ast += '\t"Declaracion Var ' + str(id_declaracion_var) + '" '
        #             x.accept(self)
                    #self.ast += '\t"Declaracion Var ' + str(id_declaracion_var) + '" '\
                    #'-> "def tipo ' + str(id_def_tipo) + ': ' + declaracion_var_p.def_tipo_p + '" ' + '\n'

        # if declaracion_var_p.ID_t is not None:
        #     if isinstance(declaracion_var_p.ID_t, list):
        #
        #         aux = declaracion_var_p.ID_t
        #
        #     else:
        #
        #         aux = [declaracion_var_p.ID_t]
        #
        #     for x in aux:
        #
        #         if isinstance(x, str):
        #
        #             self.id_nodo += 1
        #             id_nodo = self.id_nodo
        #
        #             self.ast += '\t' + str(id_nodo) + ' [label="' + x + '"]\n'
        #
        #             self.ast += '\t"Declaracion Var ' + str(id_declaracion_var)+ '" ' + '-> ' + str(id_nodo) + '\n'
        #
        #         else:
        #
        #             self.ast += '\t"Declaracion Var ' + str(id_declaracion_var) + '" '
        #             x.accept(self)
        #
        # if declaracion_var_p.NUM_t is not None:
        #     if isinstance(declaracion_var_p.NUM_t,list):
        #
        #         aux = declaracion_var_p.NUM_t
        #
        #     else:
        #
        #         aux = [declaracion_var_p.NUM_t]
        #
        #
        #     for x in aux:
        #
        #         if isinstance(x, str):
        #
        #             self.id_nodo += 1
        #             id_nodo = self.id_nodo
        #
        #             self.ast += '\t' + str(id_nodo) + ' [label="' + x + '"]\n'
        #
        #             self.ast += '\t"Declaracion Var ' + str(id_declaracion_var)+ '" ' + '-> ' + str(id_nodo) + '\n'
        #
        #         else:
        #
        #             self.ast += '\t"Declaracion Var ' + str(id_declaracion_var) + '" '
        #             x.accept(self)



        # self.id_ID += 1
        # id_ID = self.id_ID
        #
        # self.ast += '\t"Declaracion Var ' + str(id_declaracion_var) + '" '\
        #             '-> "ID ' + str(id_ID) + ': ' + declaracion_var_p.ID_t + '" ' + '\n'
        #
        # if declaracion_var_p.NUM_t is not None:
        #
        #     self.id_NUM += 1
        #     id_NUM = self.id_NUM
        #     self.ast += '\t"Declaracion Var ' + str(id_declaracion_var) + '" ' \
        #                 '-> "NUM ' + str(id_NUM) + ': ' + declaracion_var_p.NUM_t + '" ' + '\n'


    def visit_nodoDeclaracionFun(self,declaracion_fun_p):

        # completar
        self.id_declaracion_fun +=1
        id_declaracion_fun = self.id_declaracion_fun

        self.ast += '"Declaracion Fun ' + str(id_declaracion_fun) + '"' + '\n'

        self.manyTimes(declaracion_fun_p.def_tipo_p,id_declaracion_fun,declaracion_fun_p.nombre)
        self.manyTimes(declaracion_fun_p.ID_t,id_declaracion_fun,declaracion_fun_p.nombre)
        self.manyTimes(declaracion_fun_p.parametros_p,id_declaracion_fun,declaracion_fun_p.nombre)
        self.manyTimes(declaracion_fun_p.sentencia_comp_p,id_declaracion_fun,declaracion_fun_p.nombre)


        # self.id_def_tipo += 1
        # id_def_tipo = self.id_def_tipo
        #
        # self.ast += '\t"Declaracion Fun ' + str(id_declaracion_fun) + '" ' \
        #             '-> "def tipo ' + str(id_def_tipo) + ': ' + declaracion_fun_p.def_tipo_p + '" ' + '\n'

        # self.id_ID += 1
        # id_ID = self.id_ID
        #
        # self.ast += '\t"Declaracion Fun ' + str(id_declaracion_fun) + '" ' \
        #             '-> "ID ' + str(id_ID) + ': ' + declaracion_fun_p.ID_t + '" ' + '\n'

        #print(id_parametros)
        #print(declaracion_fun_p.parametros_p)


        #for x in declaracion_fun_p.parametros_p :

        # if declaracion_fun_p.parametros_p is not None:
        #     for param in declaracion_fun_p.parametros_p:
        #         param.accept(self)


        #    if isinstance(declaracion_fun_p.parametros_p,list) :

        #        aux = declaracion_fun_p.parametros_p

        #    else:

        #         aux = [declaracion_fun_p.parametros_p]

        #    for x in aux:

        #        print(x)

        #        if x is not None:
        #            if isinstance(x,str):
        #                print("entra if")

        #                self.ast += '\t"Declaracion Fun ' + str(id_declaracion_fun) + '" ' \
        #                            '-> "Parametros ' + str(id_parametros) + ': ' + str(x) + '" ' + '\n'

        # if declaracion_fun_p.parametros_p is not None:
        #
        #     if isinstance(declaracion_fun_p.parametros_p,list) :
        #
        #         aux = declaracion_fun_p.parametros_p
        #
        #     else:
        #
        #         aux = [declaracion_fun_p.parametros_p]
        #
        #     for x in aux:
        #
        #         print(x)
        #
        #         print("x")
        #
        #         self.id_nodo += 1
        #         id_nodo = self.id_nodo
        #
        #         if x is not None:
        #
        #             if isinstance(x,str):
        #
        #                 self.ast += '\t' + str(id_nodo) + ' [label="' + x + '"]\n'
        #
        #                 self.ast += '\t"Declaracion Fun122 ' + str(id_declaracion_fun) + '" ' \
        #                             #'-> "Parametros ' + str(id_nodo) + '" ' + '\n'
        #
        #             else:
        #
        #                 self.ast += '\t"Declaracion Fun ' + str(id_declaracion_fun) + '" ' \
        #                             #'-> "Parametros ' + str(id_nodo) + '" ' + '\n'
        #
        #                 x.accept(self)

        #self.id_sentencia_comp += 1
        #id_sentencia_comp = self.id_sentencia_comp

        #self.ast += '\t"Declaracion Fun ' + str(id_declaracion_fun) + '" ' + '-> ' \
                    #'-> "Sentencia Comp ' + str(id_sentencia_comp) + ': ' + declaracion_fun_p.sentencia_comp_p + '" ' + '\n'

        #declaracion_fun_p.sentencia_comp_p.accept(self)

        #self.id_sentencia_comp += 1
        #id_sentencia_comp = self.id_sentencia_comp

        #self.ast += '\t"Declaracion Fun ' + str(id_declaracion_fun) + '" ' \
         #           '-> "ID ' + str(id_sentencia_comp) + ': ' + declaracion_fun_p.sentencia_comp_p + '" ' + '\n'

        #print(declaracion_fun_p)

    # def visit_nodoLista_Parametros(self,lista_parametros_p):
    #
    #     # completar
    #     print(lista_parametros_p)
    #     print("asd")
    #
    #     self.id_nodoListaParametros += 1
    #     id_nodoParametros = self.id_nodoListaParametros


    def visit_nodoParam(self,param_p):

        #completar
        #print(param_p)

        self.id_nodoParam += 1
        id_nodoParam = self.id_nodoParam

        self.ast += '"Param ' + str(id_nodoParam) + '"' + '\n'

        self.manyTimes(param_p.def_tipo_p,id_nodoParam,param_p.nombre)
        self.manyTimes(param_p.ID_t, id_nodoParam, param_p.nombre)

        #if param_p.is_vector:


         #   self.manyTimes(param_p.ID_t,id_nodoParam,param_p.nombre)

        # if param_p.ID_t == None:
        #
        #     self.ast += '-> "Parametros ' + str(id_nodoParam) + ': VACUO' + '" ' + '\n'
        #
        # else:
        #
        #     if param_p.is_vector:
        #
        #         self.ast += '-> "ParamIF ' + str(id_nodoParam) + ': ' + param_p.def_tipo_p + ' ' + param_p.ID_t + ' < >"\n'
        #
        #     else:
        #
        #         self.ast += '-> "ParamElse ' + str(id_nodoParam) + ': ' + param_p.def_tipo_p + ' ' + param_p.ID_t + '"\n'

    def visit_nodoVacio(self,vacio_t):

        # completar
        #print(vacio_t)
        pass

    def visit_nodoSentenciaComp(self,sentencia_comp_p):

        #completar
        #print(sentencia_comp_p)

        #print(sentencia_comp_p.lista_sentencias_p)

        self.id_sentencia_comp +=1

        id_sentencia_comp = self.id_sentencia_comp

        #self.ast += '\t"Declaracion Fun ' + str(id_declaracion_fun) + '" ' + '-> '

        #print(sentencia_comp_p.declaraciones_locales_p)


        self.ast += '"Sentencia Comp ' + str(id_sentencia_comp) + '"' + '\n'

        self.manyTimes(sentencia_comp_p.declaraciones_locales_p,id_sentencia_comp,sentencia_comp_p.nombre)
        self.manyTimes(sentencia_comp_p.lista_sentencias_p, id_sentencia_comp, sentencia_comp_p.nombre)
        #self.manyTimes(sentencia_comp_p.lista_sentencias_p, id_sentencia_comp, sentencia_comp_p.nombre)

        # for x in sentencia_comp_p.declaraciones_locales_p:
        #
        #     print(x)
        #
        #     if x == "vacio":
        #
        #         continue
        #
        #     else:
        #
        #         self.ast += '\t"Sentencia compp ' + str(id_sentencia_comp) + '" ' + '-> ' + '\n'
        #
        #         #self.ast += '"Sentencia comp ' + str(id_sentencia_comp) + ': ' + '"\n'
        #
        #     x.accept(self)



        #sentencia_comp_p.accept(self)
                #
        # for y in sentencia_comp_p.lista_sentencias_p:
        #     self.ast += '-> "Sentencia comp ' + str(id_sentencia_comp) + ': ' + sentencia_comp_p.lista_sentencias_p + '"\n'
        #     y.accept(self)

    def visit_nodoSentenciaSeleccion(self,sentencia_seleccion_p):

        # completar
        #print(sentencia_seleccion_p)

        self.id_nodoSentenciaSeleccion += 1
        id_nodoSentenciaSeleccion = self.id_nodoSentenciaSeleccion

        self.ast += '"Sentencia Seleccion ' + str(id_nodoSentenciaSeleccion) + '"' + '\n'

        #print(sentencia_seleccion_p.sentencia_p)
        #print("sentencia seleccion_p")

        #print(sentencia_seleccion_p.is_else)

        if sentencia_seleccion_p.is_else == False:

            self.manyTimes(sentencia_seleccion_p.expresion_p, id_nodoSentenciaSeleccion, sentencia_seleccion_p.nombre)
            self.manyTimes(sentencia_seleccion_p.sentencia_p, id_nodoSentenciaSeleccion, sentencia_seleccion_p.nombre)

        else:

            self.manyTimes(sentencia_seleccion_p.expresion_p, id_nodoSentenciaSeleccion, sentencia_seleccion_p.nombre)
            self.manyTimes(sentencia_seleccion_p.sentencia_p, id_nodoSentenciaSeleccion, sentencia_seleccion_p.nombre)
            self.manyTimes(sentencia_seleccion_p.sentencia_p, id_nodoSentenciaSeleccion, sentencia_seleccion_p.nombre)


    def visit_nodoSentenciaIteracion(self,sentencia_iteracion_p):
        # completar
        print(sentencia_iteracion_p)



    def visit_nodoSentenciaRetorno(self,sentencia_retorno_p):
        # completar
        #print(sentencia_retorno_p)
        self.id_nodoSentenciaRetorno += 1
        id_nodoSentenciaRetorno = self.id_nodoSentenciaRetorno

        self.ast += '"Sentencia Retorno ' + str(id_nodoSentenciaRetorno) + '"' + '\n'

        if sentencia_retorno_p.thereis_expression == True:

            self.manyTimes(sentencia_retorno_p.expresion_p,id_nodoSentenciaRetorno,sentencia_retorno_p.nombre)

        else:

            self.manyTimes(sentencia_retorno_p.nombre2, id_nodoSentenciaRetorno, sentencia_retorno_p.nombre)


    def visit_nodoExpresion(self,expresion_p):
        # completar
        #print(expresion_p)
        self.id_nodoExpresion += 1
        id_nodoExpresion = self.id_nodoExpresion

        self.ast += '"Expresion ' + str(id_nodoExpresion) + '"' + '\n'

        #self.manyTimes(expresion_p.var_p, id_nodoExpresion, expresion_p.nombre)

        print(expresion_p)

        print(expresion_p.var_p)
        print("ex")

        print(expresion_p.expresion_p2)
        print("exx")

        print(expresion_p.expresion_negada_p)
        print("exxx")

        #if isinstance(expresion_p.var_p) and isinstance(expresion_p.expresion_p2):

         #   print("entro if instance")

          #  self.manyTimes(expresion_p.var_p, id_nodoExpresion, expresion_p.nombre)
          #  self.manyTimes(expresion_p.expresion_p2, id_nodoExpresion, expresion_p.nombre)

        if expresion_p.var_p is not None and expresion_p.expresion_p2 is not None:

            print("entro ")

            #self.manyTimes(expresion_p.expresion_p2, id_nodoExpresion, expresion_p.nombre)

            self.manyTimes(expresion_p.var_p, id_nodoExpresion, expresion_p.nombre)

            self.manyTimes(expresion_p.expresion_p2, id_nodoExpresion, expresion_p.nombre)

            #expresion_p.expresion_p2.accept(self)

            # self.manyTimes(expresion_p.var_p, id_nodoExpresion, expresion_p.nombre)



        else:

            print("entro else expresion negada")

            self.manyTimes(expresion_p.expresion_negada_p, id_nodoExpresion, expresion_p.nombre)

            #self.manyTimes(expresion_p.expresion_p, id_nodoExpresion, expresion_p.nombre)
            #self.manyTimes(expresion_p.var_p, id_nodoExpresion, expresion_p.nombre)
            #self.manyTimes(expresion_p.expresion_p2, id_nodoExpresion, expresion_p.nombre)


    def visit_nodoVar(self,var_p):
        # completar
        #print(var_p)

        self.id_nodoVar += 1
        id_nodoVar = self.id_nodoVar

        self.ast += '"Var ' + str(id_nodoVar) + '"' + '\n'

        if var_p.is_vec_access == False and var_p.expresion_p == None:

            self.manyTimes(var_p.id_t, id_nodoVar, var_p.nombre)

        else:

            self.manyTimes(var_p.id_t, id_nodoVar, var_p.nombre)
            self.manyTimes(var_p.expresion_p, id_nodoVar, var_p.nombre)


    def visit_nodoExpresionNegada(self,expresion_negada_p):

        #completar
        #print(expresion_negada_p)
        #print("aaaaasdf")

        self.id_nodoExpresionNegada += 1
        id_nodoExpresionNegada = self.id_nodoExpresionNegada

        self.ast += '"Expresion Negada ' + str(id_nodoExpresionNegada) + '"' + '\n'

        if expresion_negada_p.not_bracket == False:

            #print("entro True")

            self.manyTimes(expresion_negada_p.expresion_logica_p,id_nodoExpresionNegada,expresion_negada_p.nombre)

        #else:

         #   print("asfdasdfasfa")

          #  self.manyTimes(expresion_negada_p.nombre2, id_nodoExpresionNegada, expresion_negada_p.nombre)

    def visit_nodoExpresion_logica(self,expresion_logica_p):

        # completar
        #print(expresion_logica_p)

        self.id_nodoExpresionLogica += 1
        id_nodoExpresionLogica = self.id_nodoExpresionLogica

        self.ast += '"Expresion Logica ' + str(id_nodoExpresionLogica) + '"' + '\n'

        self.manyTimes(expresion_logica_p.expresion_logica_p, id_nodoExpresionLogica, expresion_logica_p.nombre)
        self.manyTimes(expresion_logica_p.expresion_simple_p, id_nodoExpresionLogica, expresion_logica_p.nombre)

    def visit_nodoBinarioOP(self,nodoBinarioOP_p):

        # completar
        #print(ramaIzq_p)

        self.id_nodoBinarioOP += 1
        id_nodoBinarioOP = self.id_nodoBinarioOP

        self.ast += '"Nodo Binario OP ' + str(id_nodoBinarioOP) + '"' + '\n'

        self.manyTimes(nodoBinarioOP_p.ramaIzq_p, id_nodoBinarioOP, nodoBinarioOP_p.nombre)
        self.manyTimes(nodoBinarioOP_p.operacion_p, id_nodoBinarioOP, nodoBinarioOP_p.nombre)
        self.manyTimes(nodoBinarioOP_p.ramaDer_p, id_nodoBinarioOP, nodoBinarioOP_p.nombre)

    def visit_nodoNUM(self,nodoNum_p):

        # completar
        #print(num_t)

        self.id_nodoNum += 1
        id_nodoNum = self.id_nodoNum

        self.ast += '"NUM ' + str(id_nodoNum) + '"' + '\n'

        self.manyTimes(nodoNum_p.num_t, id_nodoNum, nodoNum_p.nombre)
        self.manyTimes(nodoNum_p.argumentos_p, id_nodoNum, nodoNum_p.nombre)

    def visit_nodoInvocacion(self,invocacion_p):

        #completar
        #print(invocacion_p)

        self.id_nodoInvocacion += 1
        id_nodoInvocacion = self.id_nodoInvocacion

        self.ast += '"Invocacion ' + str(id_nodoInvocacion) + '"' + '\n'

        self.manyTimes(invocacion_p.id_t, id_nodoInvocacion, invocacion_p.nombre)
        self.manyTimes(invocacion_p.argumentos_p, id_nodoInvocacion, invocacion_p.nombre)




