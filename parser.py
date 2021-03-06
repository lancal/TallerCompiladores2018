# coding=utf-8
import ply.yacc as yacc

from scanner import tokens

from os import listdir

import os.path

#import dibujar_AST_visitor

import nodos

from dibujar_AST_visitor import *

from symbol_Table import *

es = []

def p_programa(p):
    #Regla 1
    """programa : lista_decl """
    p[0] = nodos.Program(p[1])
    #p2[0] = nodo.

    #print(p[0])

def p_lista_decl(p):
    #Regla 2
    """lista_decl : lista_decl declaracion"""
    if isinstance(p[1], list):
        p[0] = p[1]
        #print(p[0])
    else:
        p[0] = [p[1]]

        #print(p[0])

    if isinstance(p[2], list):
        p[0].extend(p[2])
    else:
        p[0].extend([p[2]])

def p_lista_decl2(p):
   #Regla 2
    """lista_decl : declaracion"""
    p[0] = p[1]

def p_declaracion(p):
    #Regla 3
    """declaracion : declaracion_var"""
    p[0] = p[1]

def p_declaracion2(p):
    #Regla 3
    """declaracion : declaracion_fun"""
    p[0] = p[1]

def p_declaracion_var(p):
    #Regla 4
    """declaracion_var : def_tipo ID SEMICOLON"""
    p[0] = nodos.nodoDeclaracionVar(p[1],p[2])

def p_declaracion_var2(p):
    #Regla 4
    """declaracion_var : def_tipo ID LTCOMMENT NUM RTCOMMENT SEMICOLON"""
    p[0] = nodos.nodoDeclaracionVar(p[1],p[2],thereis_num=True,NUM_t=p[4])

def p_def_tipo(p):
    #Regla 5
    """def_tipo : VACUO"""
    p[0] = p[1]

def p_def_tipo2(p):
    #Regla 5
    """def_tipo : ENT"""
    p[0] = p[1]

def p_declaracion_fun(p):
    #Regla 6
    """declaracion_fun : def_tipo ID LBRACKET parametros RBRACKET sentencia_comp"""
    #"""declaracion_fun : def_tipo ID LBRACKET parametros RBRACKET"""
    p[0] = [nodos.nodoDeclaracionFun(p[1],p[2],p[4],p[6])]

def p_parametros(p):
    #Regla 7
    """parametros : lista_parametros"""
    p[0] = p[1]

def p_parametros2(p):
    #Regla 7
    """parametros : VACUO"""
    #p[0] = nodos.nodoParam(p[1])
    p[0] = p[1]


def p_lista_parametros(p):
    #Regla 8
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
    #Regla 8
    """lista_parametros : param"""
    p[0] = p[1]

def p_param(p):
    #Regla 9
    """param : def_tipo ID"""
    p[0] = [nodos.nodoParam(p[1],thereis_ID=True, ID_t= p[2])]
    #if len(p)==3:
     #   p[0] = nodos.nodoParam(p[1],thereis_ID=True, ID_t= p[2])

def p_param2(p):
    #Regla 9
    """param : def_tipo ID LTCOMMENT RTCOMMENT"""
    p[0] = [nodos.nodoParam(p[1], thereis_ID=True, ID_t= p[2],Lt_Rt='< > ')]

def p_sentencia_comp(p):
    #Regla 10
     """sentencia_comp : LPARENT declaraciones_locales lista_sentencias RPARENT"""
     p[0] = nodos.nodoSentenciaComp(p[2],p[3])
     #p[0] = nodos.nodoSentenciaComp(declaraciones_locales_p=p[2], lista_sentencias_p = p[3])

def p_declaraciones_locales(p):
    #Regla 11
     """declaraciones_locales : declaraciones_locales declaracion_var"""
     if isinstance(p[1], list):
        p[0] = p[1]
     else:
        p[0] = [p[1]]
        #p[0] = nodos.nodoVacio(is_vacio=True,vacio_t = p[1])

     if isinstance(p[2], list):
        p[0].extend(p[2])
     else:
        p[0].extend([p[2]])
        #p[0] = nodos.nodoVacio(is_vacio=True,vacio_t=p[2])

def p_declaraciones_locales2(p):
    #Regla 11
    """declaraciones_locales : vacio"""
    p[0] = [p[1]]
    #p[0] = nodos.nodoVacio(is_vacio=True,vacio_t = p[1])


def p_lista_sentencias(p):
    #Regla 12
    """lista_sentencias : lista_sentencias sentencia"""
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]
        #p[0] = nodos.nodoVacio(is_vacio=True, vacio_t=p[1])
    if isinstance(p[2], list):
        p[0].extend(p[2])
    else:
        p[0].extend([p[2]])

def p_lista_sentencias2(p):
    #Regla 12
    """lista_sentencias : vacio"""
    p[0] = [p[1]]
    #p[0] = nodos.nodoVacio(is_vacio=True,vacio_t=p[1])


def p_sentencia(p):
    #Regla 13
    """sentencia : sentencia_expr"""
    p[0] = p[1]

def p_sentencia2(p):
    #Regla 13
    """sentencia : sentencia_comp"""
    p[0] = p[1]

def p_sentencia3(p):
    #Regla 13
    """sentencia : sentencia_seleccion"""
    p[0] = p[1]

def p_sentencia4(p):
    #Regla 13
    """sentencia : sentencia_iteracion"""
    p[0] = p[1]

def p_sentencia5(p):
    #Regla 13
    """sentencia : sentencia_retorno"""
    p[0] = p[1]

def p_sentencia_expr(p):
    #Regla 14
    """sentencia_expr : expresion SEMICOLON"""
    #p[0] = p[1]

    p[0] = nodos.nodoExpresion(expresion_p=p[1])

def p_sentencia_expr2(p):
    #Regla 14
    """sentencia_expr : SEMICOLON"""
    #p[0] = nodos.nodoExpresion()
    p[0] = nodos.nodoExpresion(semicolon_t=p[1])

def p_sentencia_seleccion(p):
    #Regla 15
    """sentencia_seleccion : SI LBRACKET expresion RBRACKET sentencia"""
    p[0] = nodos.nodoSentenciaSeleccion(p[3],p[5])

def p_sentencia_seleccion2(p):
    #Regla 15
    """sentencia_seleccion : SI LBRACKET expresion RBRACKET sentencia SINO sentencia"""
    p[0] = nodos.nodoSentenciaSeleccion(p[3], p[5],is_else=True,sentencia_p2 = p[7])

def p_sentencia_iteracion(p):
    #Regla 16
    """sentencia_iteracion : MIENTRAS LBRACKET expresion RBRACKET sentencia"""
    p[0] = nodos.nodoSentenciaIteracion(thereis_expresion=True, expresion_p= p[3], thereis_sentencia=True,sentencia_p = p[5])

def p_sentencia_iteracion2(p):
    #Regla 16
    """sentencia_iteracion : REP sentencia_comp"""
    p[0] = nodos.nodoSentenciaIteracion(thereis_sentencia_comp=True , sentencia_comp_p = p[1])

def p_sentencia_retorno(p):
    #Regla 17
    """sentencia_retorno : RET SEMICOLON"""
    p[0] = nodos.nodoSentenciaRetorno()

def p_sentencia_retorno2(p):
    #Regla 17
    """sentencia_retorno : RET expresion SEMICOLON"""
    p[0] = nodos.nodoSentenciaRetorno(thereis_expression=True,expresion_p=p[2])


def p_expresion(p):
    #Regla 18
    """expresion : var ASSIGN expresion"""
    p[0] = nodos.nodoExpresion(var_p=p[1],expresion_p=p[3])

def p_expresion2(p):
    #Regla 18
    """expresion : expresion_negada"""
    p[0] = nodos.nodoExpresion(expresion_negada_p=p[1])

def p_var(p):
    #Regla 19
    """var : ID"""
    p[0] = nodos.nodoVar(ID_t=p[1])

def p_var2(p):
    #Regla 19
    """var : ID LTCOMMENT expresion RTCOMMENT"""
    p[0] = nodos.nodoVar(ID_t=p[1],is_vec_access=True, expresion_p=p[3])

def p_expresion_negada(p):
    #Regla 20
    """expresion_negada : NOT LBRACKET expresion_logica RBRACKET"""
    #p[0] = nodos.nodoExpresionNegada(not_bracket=True,expresion_logica_p=p[3])

    p[0] = nodos.nodoExpresionNegada(expresion_logica_p=p[3])

def p_expresion_negada2(p):
    #Regla 20
    """expresion_negada : expresion_logica"""
    p[0] = nodos.nodoExpresionNegada(expresion_logica_p=p[1])

def p_expresion_logica(p):
    #Regla 21
    """expresion_logica : expresion_logica AND expresion_simple"""
    p[0] = nodos.nodoExpresionLogica(thereis_exp_log=True,expresion_logica_p=p[1],expresion_simple_p=p[3])

def p_expresion_logica2(p):
    #Regla 21
    """expresion_logica : expresion_logica AND NOT LBRACKET expresion_simple RBRACKET"""
    p[0] = nodos.nodoExpresionLogica(thereis_exp_log=True,expresion_logica_p=p[1],expresion_simple_p=p[5])

def p_expresion_logica3(p):
    #Regla 21
    """expresion_logica : expresion_simple"""
    p[0] = nodos.nodoExpresionLogica(expresion_simple_p=p[1])

def p_expresion_logica4(p):
    #Regla 21
    """expresion_logica : NOT LBRACKET expresion_simple RBRACKET"""
    p[0] = nodos.nodoExpresionLogica(expresion_simple_p=p[3])

def p_expresion_simple(p):
    #Regla 22
    """expresion_simple : expresion_simple relop expresion_aditiva"""

    if p[2] == "LT":

        p[0] = nodos.nodoBinarioOP(is_rama=True,ramaIzq_p = p[1],ramaDer_p = p[3],operacion_p=p[2])

    if p[2] == "EQ":

        p[0] = nodos.nodoBinarioOP(is_rama=True,ramaIzq_p = p[1],ramaDer_p = p[3],operacion_p=p[2])

def p_expresion_simple2(p):
    #Regla 22
    """expresion_simple : expresion_aditiva"""
    p[0] = nodos.nodoBinarioOP(ramaDer_p=p[1],nombre2="expresion aditiva")
    #p[0] = p[1]

def p_relop(p):
    #Regla 23
    """relop : LT"""
    p[0] = p[1]

def p_relop2(p):
    #Regla 23
    """relop : EQ"""
    p[0] = p[1]

def p_expresion_aditiva(p):
    #Regla 24
    """expresion_aditiva : expresion_aditiva addop term"""

    if p[2] == "+":

        #p[0] = nodos.nodoBinarioOP(p[1],p[3],"+")
        p[0] = nodos.nodoBinarioOP(is_rama=True, ramaIzq_p=p[1], ramaDer_p=p[3], operacion_p=p[2])

    if p[2] == "-":

        #p[0] = nodos.nodoBinarioOP(p[1],p[3],"-")
        p[0] = nodos.nodoBinarioOP(is_rama=True, ramaIzq_p=p[1], ramaDer_p=p[3], operacion_p=p[2])

def p_expresion_aditiva2(p):
    #Regla 24
    """expresion_aditiva : term"""
    #p[0] = p[1]
    p[0] = nodos.nodoBinarioOP(ramaDer_p= p[1],nombre2="term")

def p_addop(p):
    #Regla 25
    """addop : PLUS"""
    p[0] = p[1]

def p_addop2(p):
    #Regla 25
    """addop : MINUS"""
    p[0] = p[1]

def p_term(p):
    #Regla 26
    """term : term mulop factor"""

    if p[2] == "++":

        #p[0] = nodos.nodoBinarioOP(p[1],p[3],"++")
        p[0] = nodos.nodoBinarioOP(is_rama=True, ramaIzq_p=p[1], ramaDer_p=p[3], operacion_p=p[2])


    if p[2] == "--":

        #p[0] = nodos.nodoBinarioOP(p[1],p[3],"--")
        p[0] = nodos.nodoBinarioOP(is_rama=True, ramaIzq_p=p[1], ramaDer_p=p[3], operacion_p=p[2])

def p_term2(p):
    #Regla 26
    """term : factor"""
    #p[0] = p[1]
    p[0] = nodos.nodoBinarioOP(ramaDer_p=p[1],nombre2="factor")

def p_mulop(p):
    #Regla 27
    """mulop : TIMES"""
    p[0] = p[1]

def p_mulop2(p):
    #Regla 27
    """mulop : DIVIDE"""
    p[0] = p[1]


def p_factor(p):
    #Regla 28
    """factor : LBRACKET expresion RBRACKET"""
    p[0] = nodos.nodoExpresion(expresion_p=p[1])

def p_factor2(p):
    #Regla 28
    """factor : var"""
    p[0] = nodos.nodoVar(p[1])

def p_factor3(p):
    #Regla 28
    """factor : invocacion"""
    p[0] = p[1]

def p_factor4(p):
    #Regla 28
    """factor : NUM"""
    p[0] = nodos.nodoNUM(p[1])

def p_invocacion(p):
    #Regla 29
    """invocacion : ID LBRACKET argumentos RBRACKET """
    p[0] = nodos.nodoInvocacion(p[1],p[3])

def p_argumentos(p):
    #Regla 30
    """argumentos : lista_arg"""
    p[0] = p[1]

def p_argumentos2(p):
    #Regla 30
    """argumentos : vacio"""
    p[0] = [p[1]]
    #p[0] = nodos.nodoVacio(is_vacio= True,vacio_t=p[1])


def p_lista_arg(p):
    #Regla 31
    """lista_arg : lista_arg COMMA expresion"""
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    if isinstance(p[3], list):
        p[0].extend(p[3])
    else:
        p[0].extend([p[3]])

def p_lista_arg2(p):
    #Regla 31
    """lista_arg : expresion"""
    p[0] = [p[1]]




def p_vacio(p):
    'vacio :'
    #p[0] = nodos.nodoVacio()
    p[0] = nodos.nodoVacio()
    pass

# Errores en la sintaxis.
def p_error(p):
    print('Error de sintaxis! ')
    if p is not None:
        print('Error en el ' + str(p.type) + '\n')
    else:
        print('El archivo de entrada esta vacío\n')

def errorSemantico(errores):
    print("Error Semántico",errores)

# Build the parser
#parser = yacc.yacc()
parser = yacc.yacc(debug=True,start="programa")


def listarArchivoPP():

    for carpeta in listdir("."):
        if carpeta.endswith(".pp"):
            print (carpeta)

def ingresarArchivo(nombreArchivo):

    treeFileDot = open('tree.dot', 'w')
    treeFileDot2 = open('tree2.dot', 'w')

    with open(nombreArchivo, 'r') as arch:
        contents = arch.read()
        result = parser.parse(contents)
        if result is not None:
            visitor_tipos = Visitor()
            nodos.Program.accept(result, visitor_tipos)
            treeFileDot.write(visitor_tipos.ast)
            st = symbolTable()
            print(st)
            print("st en parser.py")
            visitor_tipos2 = Visitor2()
            nodos.Program.accept2(result,visitor_tipos2,st)
            treeFileDot2.write(visitor_tipos2.ast)

            #print("aaaaaa")

            #table = getTable()

            #print(table)
            #print("table")

            #print (st.getNodos())
            #print("st.getNodos")

            #t = table.getNodos()

            scope_variables(st)
            scope_function(st)

            es1 = nodos.getesp()
            es.extend(es1)
            for e in es:
                #print("errores semanticos")

                errorSemantico(e)

            es2 = nodos.getess()
            if es2 is not None:
                for e in es2:
                    print(e)
                    #errorSemantico(e)

        else:
            treeFileDot.write('Error al realizar el parse.')

def cerrar(cerrar):

    if cerrar == "CERRAR":

        print("\nBye ! :(")

        c = False

        return c
    else:

        c = True

        return c


def scope_variables(symbolTable):

    cont = 0

    #print(symbolTable)
    #print("scope_variables")

    #if len(symbolTable.getNodos()) != 0:

    if symbolTable:

        #print ("dentro de if symbolTable.getNodos")
        nodes = symbolTable.getNodos()

        #print(nodes)
        #print("symbolTable.")

        for node in nodes:

            #print("dentro node in nodes")

            comparation = 0
            dato = node.identificador
            for nod in nodes:
                if dato == nod.identificador and dato != "if" and dato != "else" and dato != "while":
                    comparation += 1
            if comparation > 1 and node.getsymbolTable() is None:

                es.append("Variable del tipo " + node.tipo + " " + dato + " repetida")

            if node.getsymbolTable() is not None:
                scope_variables(node.getsymbolTable())


def scope_function(symbolTable):
    nodeFunction = []
    nodes = symbolTable.getNodos()
    temp = Nodo(None, None, None)
    position = 0
    comparation = 0
    for node in nodes:
        if node.getsymbolTable() is not None:
            nodeFunction.append(node)

    for i in range(len(nodeFunction)):
        temp = nodeFunction[i]
        position = i
        nodeFunction.pop(i)
        for x in nodeFunction:
            if temp.tipo == x.tipo and temp.identificador == x.identificador:
                comparation += 1
                if comparation == 2:
                    st = temp.getsymbolTable().getParam()
                    st2 = x.getsymbolTable().getParam()
                    comparation = 0
                    cont = 0
                    if len(st) == len(st2):
                        for s in range(len(st)):
                            if st[s].tipo == st2[s].tipo:
                                cont += 1
                        if len(st) == cont:
                            es.append("Funciones declaradas iguales " + temp.identificador)
                            break
        nodeFunction.insert(i, temp)




def main():

    global flag

    flag = True

    while flag != False:

        listarArchivoPP()

        print("\nPara salir Ingresar: CERRAR ")

        archivoNombre = input("\nIngrese el nombre del archivo a leer: ")

        flag = cerrar(archivoNombre)

        if flag == False:

            break

        while os.path.isfile(archivoNombre) == False:

            print("\nArchivo no encontrado :( ")

            # se ingresa nuevamente el nombre del archivo a buscar
            archivoNombre = input("\nIngrese el nombre del archivo a leer: ")

            flag = cerrar(archivoNombre)

            if flag == False:

                break

        if os.path.isfile(archivoNombre) == True:

            print("\nArchivo Encontrado :) \n")

            ingresarArchivo(archivoNombre)

            print("\nArchivo tree.dot Generado :) \n")
            print("Archivo tree2.dot Generado :) \n")


        #flag = cerrar(archivoNombre)


if __name__ == "__main__":

    #flag = True

    main()