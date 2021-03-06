from symbol_Table import *

import nodos

#from nodos import *

import re

st = symbolTable()


listAsignaciones = []
listFunciones = []

cont = 0


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
        self.id_nodoSentenciaIteracion = 0
        self.id_nodoVacio = 0

        self.id_nodoParam = 0

    def visit_program(self, program):
        self.id_program += 1
        id_program = self.id_program

        if program.statement_list is not None:

            if isinstance(program.statement_list,list):

                aux = program.statement_list

            else:

                aux = [program.statement_list]

            for stmt in aux:

                if stmt is not None:
                    self.ast += '\t"Programa ' + str(id_program) +  '" ' + '-> '
                    stmt.accept(self)
        self.ast = 'digraph G {\n' + self.ast + '}'

    def manyTimes(self,p1,p2,p3):


        if p1 is not None:

            if isinstance(p1, list):

                aux = p1

            else:

                aux = [p1]

            for x in aux:

                if isinstance(x, str):

                    self.id_nodo += 1
                    id_nodo = self.id_nodo

                    self.ast += '\t' + str(id_nodo) + ' [label="' + x + '"]\n'

                    self.ast += '\t"' + p3 + str(p2) + '" ' + '-> ' + str(id_nodo) + '\n'

                else:

                    if x.nombre == "vacio":
                        self.id_nodo += 1
                        id_nodo = self.id_nodo

                        self.ast += '\t' + str(id_nodo) + ' [label="' + x.nombre + '"]\n'
                        self.ast += '\t"' + p3 + str(p2) + '" ' + '-> ' + str(id_nodo) + '\n'

                    else:

                        self.ast += '\t"' + p3 + str(p2) + '" ' + '-> '
                        x.accept(self)

    def visit_nodoDeclaracionVar(self,declaracion_var_p):


        self.id_declaracion_var+= 1
        id_declaracion_var = self.id_declaracion_var

        self.ast += '"Declaracion Var ' + str(id_declaracion_var) + '"' + '\n'

        if declaracion_var_p.thereis_num == False:

            self.manyTimes(declaracion_var_p.def_tipo_p, id_declaracion_var, declaracion_var_p.nombre)
            self.manyTimes(declaracion_var_p.ID_t, id_declaracion_var, declaracion_var_p.nombre)

        else:

            self.manyTimes(declaracion_var_p.def_tipo_p, id_declaracion_var, declaracion_var_p.nombre)
            self.manyTimes(declaracion_var_p.ID_t, id_declaracion_var, declaracion_var_p.nombre)
            self.manyTimes(declaracion_var_p.NUM_t, id_declaracion_var,declaracion_var_p.nombre)



    def visit_nodoDeclaracionFun(self,declaracion_fun_p):

        # completar
        self.id_declaracion_fun +=1
        id_declaracion_fun = self.id_declaracion_fun

        self.ast += '"Declaracion Fun ' + str(id_declaracion_fun) + '"' + '\n'

        self.manyTimes(declaracion_fun_p.def_tipo_p,id_declaracion_fun,declaracion_fun_p.nombre)
        self.manyTimes(declaracion_fun_p.ID_t,id_declaracion_fun,declaracion_fun_p.nombre)
        self.manyTimes(declaracion_fun_p.parametros_p,id_declaracion_fun,declaracion_fun_p.nombre)
        self.manyTimes(declaracion_fun_p.sentencia_comp_p,id_declaracion_fun,declaracion_fun_p.nombre)


    def visit_nodoParam(self,param_p):


        self.id_nodoParam += 1
        id_nodoParam = self.id_nodoParam

        self.ast += '"Param ' + str(id_nodoParam) + '"' + '\n'

        if param_p.thereis_ID == False:

            #print("dentro de param_p.thereis_ID == False")

            self.manyTimes(param_p.def_tipo_p,id_nodoParam,param_p.nombre)

        else:

            self.manyTimes(param_p.def_tipo_p, id_nodoParam, param_p.nombre)
            self.manyTimes(param_p.ID_t, id_nodoParam, param_p.nombre)


    def visit_nodoVacio(self,vacio_t):

        self.id_nodoVacio += 1
        id_nodoVacio = self.id_nodoVacio

        self.ast += '"Nodo Vacio ' + str(id_nodoVacio) + '"' + '\n'

        self.manyTimes(vacio_t.vacio_t,id_nodoVacio,vacio_t.nombre)

    def visit_nodoSentenciaComp(self,sentencia_comp_p):


        self.id_sentencia_comp +=1

        id_sentencia_comp = self.id_sentencia_comp

        self.ast += '"Sentencia Comp ' + str(id_sentencia_comp) + '"' + '\n'


        self.manyTimes(sentencia_comp_p.declaraciones_locales_p,id_sentencia_comp,sentencia_comp_p.nombre)
        self.manyTimes(sentencia_comp_p.lista_sentencias_p, id_sentencia_comp, sentencia_comp_p.nombre)

    def visit_nodoSentenciaSeleccion(self,sentencia_seleccion_p):


        self.id_nodoSentenciaSeleccion += 1
        id_nodoSentenciaSeleccion = self.id_nodoSentenciaSeleccion

        self.ast += '"Sentencia Seleccion ' + str(id_nodoSentenciaSeleccion) + '"' + '\n'


        if sentencia_seleccion_p.is_else == False:

            self.manyTimes(sentencia_seleccion_p.expresion_p, id_nodoSentenciaSeleccion, sentencia_seleccion_p.nombre)
            self.manyTimes(sentencia_seleccion_p.sentencia_p, id_nodoSentenciaSeleccion, sentencia_seleccion_p.nombre)

        else:

            self.manyTimes(sentencia_seleccion_p.expresion_p, id_nodoSentenciaSeleccion, sentencia_seleccion_p.nombre)
            self.manyTimes(sentencia_seleccion_p.sentencia_p, id_nodoSentenciaSeleccion, sentencia_seleccion_p.nombre)
            self.manyTimes(sentencia_seleccion_p.sentencia_p2, id_nodoSentenciaSeleccion, sentencia_seleccion_p.nombre)


    def visit_nodoSentenciaIteracion(self,sentencia_iteracion_p):

        self.id_nodoSentenciaIteracion += 1
        id_nodoSentenciaIteracion = self.id_nodoSentenciaIteracion

        self.ast += '"Sentencia Iteracion ' + str(id_nodoSentenciaIteracion) + '"' + '\n'

        if sentencia_iteracion_p.thereis_expresion == True and sentencia_iteracion_p.thereis_sentencia == True:

            self.manyTimes(sentencia_iteracion_p.expresion_p, id_nodoSentenciaIteracion, sentencia_iteracion_p.nombre)
            self.manyTimes(sentencia_iteracion_p.sentencia_p, id_nodoSentenciaIteracion, sentencia_iteracion_p.nombre)

        if sentencia_iteracion_p.thereis_sentencia_comp == True:

            self.manyTimes(sentencia_iteracion_p.sentencia_comp_p, id_nodoSentenciaIteracion, sentencia_iteracion_p.nombre)


    def visit_nodoSentenciaRetorno(self,sentencia_retorno_p):

        self.id_nodoSentenciaRetorno += 1
        id_nodoSentenciaRetorno = self.id_nodoSentenciaRetorno

        self.ast += '"Sentencia Retorno ' + str(id_nodoSentenciaRetorno) + '"' + '\n'

        if sentencia_retorno_p.thereis_expression == True:

            self.manyTimes(sentencia_retorno_p.expresion_p,id_nodoSentenciaRetorno,sentencia_retorno_p.nombre)

        else:

            self.manyTimes(sentencia_retorno_p.nombre2, id_nodoSentenciaRetorno, sentencia_retorno_p.nombre)


    def visit_nodoExpresion(self,expresion_p):

        self.id_nodoExpresion += 1
        id_nodoExpresion = self.id_nodoExpresion

        self.ast += '"Expresion ' + str(id_nodoExpresion) + '"' + '\n'


        if expresion_p.var_p is not None and expresion_p.expresion_p2 is not None:

            self.manyTimes(expresion_p.var_p, id_nodoExpresion, expresion_p.nombre)

            self.manyTimes(expresion_p.expresion_p2, id_nodoExpresion, expresion_p.nombre)

        else:

            self.manyTimes(expresion_p.expresion_negada_p, id_nodoExpresion, expresion_p.nombre)

            if expresion_p.expresion_p2:

                #self.manyTimes(expresion_p.var_p, id_nodoExpresion, expresion_p.nombre)

                self.manyTimes(expresion_p.expresion_p2,id_nodoExpresion,expresion_p.nombre)

            else:

                self.manyTimes(expresion_p.semicolon_t, id_nodoExpresion, expresion_p.nombre)


    def visit_nodoVar(self,var_p):

        self.id_nodoVar += 1
        id_nodoVar = self.id_nodoVar

        self.ast += '"Var ' + str(id_nodoVar) + '"' + '\n'

        if var_p.is_vec_access == False and var_p.expresion_p == None:

            self.manyTimes(var_p.id_t, id_nodoVar, var_p.nombre)

        else:

            self.manyTimes(var_p.id_t, id_nodoVar, var_p.nombre)
            self.manyTimes(var_p.expresion_p, id_nodoVar, var_p.nombre)


    def visit_nodoExpresionNegada(self,expresion_negada_p):


        self.id_nodoExpresionNegada += 1
        id_nodoExpresionNegada = self.id_nodoExpresionNegada

        self.ast += '"Expresion Negada ' + str(id_nodoExpresionNegada) + '"' + '\n'

        self.manyTimes(expresion_negada_p.expresion_logica_p,id_nodoExpresionNegada,expresion_negada_p.nombre)

    def visit_nodoExpresionLogica(self,expresion_logica_p):


        self.id_nodoExpresionLogica += 1
        id_nodoExpresionLogica = self.id_nodoExpresionLogica

        self.ast += '"Expresion Logica ' + str(id_nodoExpresionLogica) + '"' + '\n'

        if expresion_logica_p.thereis_exp_log == True:

            self.manyTimes(expresion_logica_p.expresion_logica_p, id_nodoExpresionLogica, expresion_logica_p.nombre)
            self.manyTimes(expresion_logica_p.expresion_simple_p, id_nodoExpresionLogica, expresion_logica_p.nombre)

        else:

            self.manyTimes(expresion_logica_p.expresion_simple_p, id_nodoExpresionLogica, expresion_logica_p.nombre)

    def visit_nodoBinarioOP(self,nodoBinarioOP_p):


        self.id_nodoBinarioOP += 1
        id_nodoBinarioOP = self.id_nodoBinarioOP

        self.ast += '"Nodo Binario Op ' + str(id_nodoBinarioOP) + '"' + '\n'

        if nodoBinarioOP_p.is_rama == False:

            #print("entro if")

            self.manyTimes(nodoBinarioOP_p.ramaDer_p, id_nodoBinarioOP, nodoBinarioOP_p.nombre)



        else:

            #print("entro else")

            self.manyTimes(nodoBinarioOP_p.ramaIzq_p, id_nodoBinarioOP, nodoBinarioOP_p.nombre)
            self.manyTimes(nodoBinarioOP_p.operacion_p, id_nodoBinarioOP, nodoBinarioOP_p.nombre)
            self.manyTimes(nodoBinarioOP_p.ramaDer_p, id_nodoBinarioOP, nodoBinarioOP_p.nombre)


    def visit_nodoNUM(self,nodoNum_p):


        self.id_nodoNum += 1
        id_nodoNum = self.id_nodoNum

        self.ast += '"NUM ' + str(id_nodoNum) + '"' + '\n'

        self.manyTimes(nodoNum_p.num_t, id_nodoNum, nodoNum_p.nombre)


    def visit_nodoInvocacion(self,invocacion_p):

        self.id_nodoInvocacion += 1
        id_nodoInvocacion = self.id_nodoInvocacion

        self.ast += '"Invocacion ' + str(id_nodoInvocacion) + '"' + '\n'

        self.manyTimes(invocacion_p.id_t, id_nodoInvocacion, invocacion_p.nombre)
        self.manyTimes(invocacion_p.argumentos_p, id_nodoInvocacion, invocacion_p.nombre)

class Visitor2(object):



    def incrementarContador(self):
        global cont
        cont += 1
        return "%d" % cont


    def __init__(self):

        self.ast = ''
        self.id_nodo = 0
        self.id_program = 0
        self.id_declaracion_var = 0
        self.id_declaracion_fun = 0
        self.id_nodoParam = 0
        self.id_sentencia_comp = 0
        self.id_sentencia_expr = 0
        self.idCont = 0


    def visit_program(self,program,symbol_Table):

        #print("dentro de visit_program")

        self.id_program += 1
        id_program = self.id_program
        self.idCont += 1
        idCont = self.idCont

        id = self.incrementarContador()
        # if program.statement_list is not None:
        #
        #     if isinstance(program.statement_list,list):
        #
        #         aux = program.statement_list
        #
        #     else:
        #
        #         aux = [program.statement_list]
        #
        #     for stmt in aux:
        #
        #         if stmt is not None:
        #             #stmt.accept2(self, symbol_Table)
        #             #self.ast += str(id_program) + '-> '
        #             #stmt.accept2(self,symbol_Table)
        #
        #             self.ast += '\t"Programa ' + str(id_program) + '" ' + '-> '
        #             stmt.accept2(self,symbol_Table)
        #
        #
        #     self.ast = 'digraph G {\n' + self.ast + '}'

        for dl in program.statement_list:

            dl = dl.accept2(self,symbol_Table)

            self.ast += str(id) + "->" + str(id+"1") + "\n\t"

            print(dl)
            print("dl")

        self.ast += str(id) + "[label= " + program.nombre + "];" + "\n\t"

        self.ast = 'digraph G {\n\t' + self.ast + '}'


    def manyTimes(self, p1, p2, p3,st):

        if p1 is not None:

            if isinstance(p1, list):

                aux = p1

            else:

                aux = [p1]

            for x in aux:

                if isinstance(x, str):

                    self.id_nodo += 1
                    id_nodo = self.id_nodo

                    self.ast += '\t' + str(id_nodo) + ' [label="' + x + '"]\n'

                    self.ast += '\t"' + p3 + str(p2) + '" ' + '-> ' + str(id_nodo) + '\n'

                else:

                    if x.nombre == "vacio":
                        self.id_nodo += 1
                        id_nodo = self.id_nodo

                        self.ast += '\t' + str(id_nodo) + ' [label="' + x.nombre + '"]\n'
                        self.ast += '\t"' + p3 + str(p2) + '" ' + '-> ' + str(id_nodo) + '\n'

                    else:

                        self.ast += '\t"' + p3 + str(p2) + '" ' + '-> '
                        x.accept2(self,st)


        # for dl in program.statement_list:
        #
        #     dl = dl.accept2(self,symbol_Table)
        #
        #     self.ast += str(id_program) + "->" + str(dl) + "\n\t"
        #
        # self.ast += str(id_program) + "[label= " + program.nombre + "];" + "\n\t"
        #
        # self.ast = 'digraph G {\n' + self.ast + '}'


            #self.ast += str(id_program) + "[label= " + program.nombre + "];"


        #for x in program.statement_list:

         #   x = x.accept2(st)




    def visit_nodoDeclaracionVar(self,declaracion_var_p, symbol_Table):

        print("\ndentro de visit_nodoDeclaracionVar")

        self.id_declaracion_var += 1
        id_declaracion_var = self.id_declaracion_var

        self.idCont += 1
        idCont = self.idCont

        id = incrementarContador()

        #self.ast += '"Error Nodo Declaracion Var ' + str(id_declaracion_var) + '"' + '\n'

        #print(declaracion_var_p.NUM_t)
        #print("declaracion_var_p.NUM_t")

        #print(id_declaracion_var)

        #if declaracion_var_p.NUM_t is None:

        if declaracion_var_p.NUM_t is None:
            #print("dentro de declaracion_var_p.NUM_t")
            vardec = Nodo(declaracion_var_p.def_tipo_p, declaracion_var_p.ID_t, None)
            vardec.setPadre(symbol_Table)
            symbol_Table.agregar(vardec)
            #a = symbol_Table.getNodos()
            #print(str(a))
            #print("symbol_Table.getNodos dentro del if declaracion_var_p.NUM.t")
            self.ast += str(id) + '[label= "'+declaracion_var_p.nombre+': '+declaracion_var_p.def_tipo_p+' '+declaracion_var_p.ID_t+'" ];\n\t'

            #self.ast += '"Error Nodo Declaracion Var ' + str(id_declaracion_var) + '"' + '\n'

            #self.manyTimes(declaracion_var_p.def_tipo_p, id_declaracion_var, declaracion_var_p.nombre2,symbol_Table)
            #self.manyTimes(declaracion_var_p.ID_t, id_declaracion_var, declaracion_var_p.nombre2,symbol_Table)

        else:
            vardec = Nodo(declaracion_var_p.def_tipo_p, declaracion_var_p.ID_t + "<>" , None)

            #print(vardec.tipo)
            #print("vardec.tipo")

            #print(vardec.identificador)
            #print("vardec")
            vardec.setPadre(symbol_Table)
            symbol_Table.agregar(vardec)
            #a = symbol_Table.getNodos()
            #print(a)
            #print("symbol_Table.getNodos")
            self.ast += str(id) + '[label= "'+declaracion_var_p.nombre+': '+declaracion_var_p.def_tipo_p+'<> '+declaracion_var_p.ID_t+'" ];\n\t'
            #self.ast += '"Error Nodo Declaracion Var ' + str(id_declaracion_var) + '"' + '\n'
            #self.manyTimes(declaracion_var_p.def_tipo_p, id_declaracion_var, declaracion_var_p.nombre2,symbol_Table)
            #self.manyTimes(declaracion_var_p.ID_t, id_declaracion_var, declaracion_var_p.nombre2,symbol_Table)
            #self.manyTimes(declaracion_var_p.NUM_t, id_declaracion_var, declaracion_var_p.nombre2,symbol_Table)


    def visit_nodoDeclaracionFun(self,declaracion_fun_p,symbol_Table):


        print("\ndentro visit_nodoDeclaracionFun")

        print(symbol_Table)
        print("symbol_Table en visit_nodoDeclaracionFun")

        self.id_declaracion_fun += 1
        id_declaracion_fun = self.id_declaracion_fun

        self.idCont +=1
        idCont = self.idCont

        id = self.incrementarContador()

        #self.ast += '"Error Nodo Declaracion Fun ' + str(id_declaracion_fun) + '"' + '\n'

        #print(declaracion_fun_p.parametros_p)

        fun = Nodo(declaracion_fun_p.def_tipo_p, declaracion_fun_p.ID_t, None)

        # print(fun.tipo)
        # print("fun.tipo")
        # print(fun.identificador)
        # print("fun.identificador")
        #
        # print(fun)
        # print("fun")
        #
        # listFunciones.append(fun)
        # #agregado pero nose bn
        # #listAsignaciones.append(fun)
        # print(listFunciones)
        # print("listFunciones")

        fun.setPadre(symbol_Table)

        print(symbol_Table)
        print("symbol_Table")

        st2 = symbolTable()

        # print(st2)
        # print("st2 valores")

        self.patron = re.compile(r'vacuo|ent', re.I)
        self.arreglo = self.patron.findall(declaracion_fun_p.def_tipo_p)

        # self.patron = re.compile(r'ent', re.I)
        # self.arreglo2 = self.patron.findall(declaracion_fun_p.def_tipo_p)

        print(declaracion_fun_p.def_tipo_p)
        print("declaracion_fun_p.def_tipo_")

        print(declaracion_fun_p.parametros_p)
        print("declaracion_fun_p.parametros_p")

        # print(self.arreglo2)
        # print("self.arreglo2")

        #print(self.arreglo)
        #print("self.arreglo")

        #print(st)
        #print("st")

        #listSymbol = st.getNodos()
        #print(listSymbol)
        #print("listSymbol[0]")
        #listaNodosActual = symbol_Table.getNodos()

        #print(listSymbol)
        #print("listSymbol")

        #print(listaNodosActual)
        #print("listaNodosActual")


        if declaracion_fun_p.parametros_p != self.arreglo[0] :

            print("algo")
            print(declaracion_fun_p.parametros_p)
            print ("declaracion_fun_p.parametros_p")

            for ps in declaracion_fun_p.parametros_p:

                print(ps)
                print("ps")



                ps = ps.accept2(self,st2)

                self.ast += str(id) + "->" + str(id+"1") + "\n\t"

                print("paso ps")
            #self.ast += '"Error Nodo Declaracion Fun ' + str(id_declaracion_fun) + '"' + '\n'
            #self.manyTimes(declaracion_fun_p.def_tipo_p, id_declaracion_fun, declaracion_fun_p.nombre2,st2)
            #self.manyTimes(declaracion_fun_p.ID_t, id_declaracion_fun, declaracion_fun_p.nombre2,st2)
            #self.manyTimes(declaracion_fun_p.parametros_p, id_declaracion_fun, declaracion_fun_p.nombre2,st2)

        fun.setsymbolTable(st2)
        symbol_Table.agregar(fun)

        compound = declaracion_fun_p.sentencia_comp_p.accept2(self,st2)
        #self.ast += '"Error Nodo Declaracion Fun ' + str(id_declaracion_fun) + '"' + '\n'
        #self.manyTimes(declaracion_fun_p.sentencia_comp_p, id_declaracion_fun, declaracion_fun_p.nombre2,st2)

        self.ast += str(id) + "->" + str(id+"2") + "\n\t"
        self.ast += str(id) + '[label= "' + declaracion_fun_p.nombre+ ': ' + declaracion_fun_p.def_tipo_p + ' ' + declaracion_fun_p.ID_t + '" ];\n\t'

    def visit_nodoParam(self,param_p, symbol_Table):

        print("\ndentro de visit_nodoParam")

        self.id_nodoParam += 1
        id_nodoParam = self.id_nodoParam

        self.idCont += 1
        idCont = self.idCont

        id = self.incrementarContador()

        print(param_p.def_tipo_p)
        print("param_p.def_tipo_p")

        #listSymbol = st.getNodos()

        #listNodoActual = symbol_Table.getNodos

        #nodos.isDeclared(listSymbol,li)

        if param_p.Lt_Rt is None:

            param = Nodo(param_p.def_tipo_p,param_p.ID_t,None)
            param.setPadre(symbol_Table)
            symbol_Table.agregar(param)
            symbol_Table.agregarParam(param)
            self.ast += str(id) + '[label= "' + param_p.nombre + ': ' + param_p.def_tipo_p + ' ' + param_p.ID_t + '" ];\n\t'
            #self.ast += '"Error Param ' + str(id_nodoParam) + '"' + '\n'

        else:

            param = Nodo(param_p.def_tipo_p + param_p.Lt_Rt, param_p.ID_t, None)
            param.setPadre(symbol_Table)
            symbol_Table.agregar(param)
            symbol_Table.agregarParam(param)
            self.ast += str(id) + '[label= "' + param_p.nombre + ': ' + param_p.def_tipo_p + param_p.Lt_Rt + ' ' + param_p.ID_t + '" ];\n\t'
            #self.ast += '"Error Param ' + str(id_nodoParam) + '"' + '\n'


    def visit_nodoSentenciaComp(self,sentencia_comp_p,symbol_Table):

        print("\ndentro de visit_nodoSentenciaComp")

        self.id_sentencia_comp += 1

        id_sentencia_comp = self.id_sentencia_comp

        self.idCont += 1
        idCont = self.idCont

        id = self.incrementarContador()

        for local in sentencia_comp_p.declaraciones_locales_p:

            #print(local)
            #print("local")
            if local.nombre != "vacio":

                #sentencia_comp_p = sentencia_comp_p.accept2(self,symbol_Table)

                print("local.nombre")

                local = local.accept2(self,symbol_Table)

                #self.ast += str(id_sentencia_comp) + "->" + str(sentencia_comp_p) + "\n\t"
                self.ast += str(id) + "->" + str(local) + "\n\t"

                #print("relleno local.nombre")

            for state in sentencia_comp_p.lista_sentencias_p:
                print("soy un while o if")
                #print(state.nombre)
                if state.nombre != "vacio":
                    print("dentro if state.nombre")
                    state = state.accept2(self,symbol_Table)
                    self.ast += str(id) + "->" + str(state) + "\n\t"
            self.ast += str(id) + "[label= " + sentencia_comp_p.nombre+ "];" + "\n\t"

    def visit_nodoVacio(self, vacio_t,symbol_Table):

        self.idCont += 1
        idCont = self.idCont

        id = self.incrementarContador()

    def visit_nodoExpresion(self,expresion_p,symbol_Table):

        self.id_sentencia_expr += 1

        id_sentencia_expr = self.id_sentencia_expr

        listSymbol = st.getNodos()

        listaNodosActual = symbol_Table.getNodos()

        if isinstance(expresion_p.expresion_p2,expresion_p.var_p):

            listAsignaciones.append(expresion_p.expresion_p2)

            idvar = expresion_p.var_p

            if idvar.expresion_p is None:

                nodos.isDeclared(listSymbol,listaNodosActual,idvar)

            else:
                temp = nodos.nodoVar(None,False,None)

                temp.id_t = idvar.id_t + "<>"
                nodos.isDeclared(listSymbol,listaNodosActual,temp)

            if not isinstance(expresion_p.expresion_p2,nodos.nodoExpresionNegada):

                idvar = expresion_p.expresion_p2

                #print(idvar)

                if not isinstance(idvar,nodos.nodoExpresionNegada):

                    if idvar.expresion_p is None:

                        nodos.isDeclared(listSymbol,listaNodosActual,idvar)
                        nodos.isInitialized(listAsignaciones,idvar)

                    else:

                        temp = nodos.nodoVar(None,False,None)
                        temp.id_t = idvar.id_t + "<>"
                        nodos.isDeclared(listSymbol,listaNodosActual,temp)
                        temp.id_t = idvar.id_t + "<"+idvar.expresion_p.number+">"




def getTable():
    return st




