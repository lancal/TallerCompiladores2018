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
        self.id_id = 0

    def visit_program(self, program):
        self.id_program += 1
        id_program = self.id_program
        if program.statement_list is not None:
            for stmt in program.statement_list:
                if stmt is not None:
                    self.ast += '\t"Lista ' + str(id_program) + '" '
                    stmt.accept(self)
        self.ast = 'digraph G {\n' + self.ast + '}'

    def visit_expression(self, expression):
        self.id_expression += 1
        id_expression = self.id_expression
        self.ast += '-> "' + 'Asignacion ' + str(id_expression) + '"' + '\n'
        self.ast += '\t"' + 'Asignacion ' + str(id_expression) + '" '
        expression.var_p.accept(self)
        self.ast += '\t"' + 'Asignacion ' + str(id_expression) + '" '
        expression.expression_p.accept(self)

    def visit_simple_expression(self, simple_expresion):
        self.id_simple_expression += 1
        id_simple_expression = self.id_simple_expression
        self.ast += '-> "Comparador ' + str(id_simple_expression) + ': ' + simple_expresion.relop_t + '"' + '\n'
        self.ast += '\t"Comparador ' + str(id_simple_expression) + ': ' + simple_expresion.relop_t + '" '
        simple_expresion.additive_expression1_p.accept(self)
        self.ast += '\t"Comparador ' + str(id_simple_expression) + ': ' + simple_expresion.relop_t + '" '
        simple_expresion.additive_expression2_p.accept(self)

    def visit_additive_expression(self, additive_expresion):
        self.id_additive_expression += 1
        id_additive_expression = self.id_additive_expression
        self.ast += '-> "Signo ' + str(id_additive_expression) + ': ' + additive_expresion.addop_t + '"' + '\n'
        self.ast += '\t"Signo ' + str(id_additive_expression) + ': ' + additive_expresion.addop_t + '" '
        additive_expresion.additive_expression_p.accept(self)
        self.ast += '\t"Signo ' + str(id_additive_expression) + ': ' + additive_expresion.addop_t + '" '
        additive_expresion.term_p.accept(self)

    def visit_term(self, term):
        self.id_term += 1
        id_term = self.id_term
        self.ast += '-> "Signo ' + str(id_term) + ': ' + term.mulop_t + '"' + '\n'
        self.ast += '\t"Signo ' + str(id_term) + ': ' + term.mulop_t + '" '
        term.term_p.accept(self)
        if term.factor_p is not None:
            self.ast += '\t"Signo ' + str(id_term) + ': ' + term.mulop_t + '" '
            term.factor_p.accept(self)

    def visit_num(self, num):
        self.id_num += 1
        id_num = self.id_num
        self.ast += '-> "NUM' + str(id_num) + ': ' + num.num_t + '"' + '\n'

    def visit_type_esp_id_num(self,declaracion_var_p):

        #completar
        print(declaracion_var_p)