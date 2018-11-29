class Nodo():
    pass

class Program(Nodo):
    def __init__(self, statement_list_p):
        self.statement_list = statement_list_p

    def accept(self, visitor):
        visitor.visit_program(self)

class Expression(Nodo):
    def __init__(self, var_p, expression_p):
        self.var_p = var_p
        self.expression_p = expression_p

    def accept(self, visitor):
        visitor.visit_expression(self)


class SimpleExpression(Nodo):
    def __init__(self, additive_expression1_p, relop_t, additive_expression2_p):
        self.additive_expression1_p = additive_expression1_p
        self.relop_t = relop_t
        self.additive_expression2_p = additive_expression2_p

    def accept(self, visitor):
        visitor.visit_simple_expression(self)


class AdditiveExpression(Nodo):
    def __init__(self, additive_expression_p, addop_t, term_p):
        self.additive_expression_p = additive_expression_p
        self.addop_t = addop_t
        self.term_p = term_p

    def accept(self, visitor):
        visitor.visit_additive_expression(self)


class Term(Nodo):
    def __init__(self, term_p, mulop_t, factor_p):
        self.term_p = term_p
        self.mulop_t = mulop_t
        self.factor_p = factor_p

    def accept(self, visitor):
        visitor.visit_term(self)


class Num(Nodo):
    def __init__(self, num_t):
        self.num_t = num_t

    def accept(self, visitor):
        visitor.visit_num(self)


class type_esp_id_num(Nodo):

    def __init__(self,def_tipo_p,ID_p,NUM_p=None):

        self.def_tipo_p = def_tipo_p
        self.ID_p = ID_p
        self.NUM_p = NUM_p

    def accept(self,visitor):
        visitor.visit_type_esp_id_num(self)