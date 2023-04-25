import hypothesis.strategies as st
from hypothesis import given

class Num:
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value

    def compile(self):
        return f"push {self.value}\n"

    def __str__(self):
        return str(self.value)

    def accept(self, visitor):
        return visitor.visit_Num(self)


class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()

    def compile(self):
        return self.left.compile() + self.right.compile() + "add\n"

    def __str__(self):
        return f"({self.left} + {self.right})"

    def accept(self, visitor):
        return visitor.visit_Add(self)


class Mul:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()

    def compile(self):
        return self.left.compile() * self.right.compile() + "mul\n"

    def __str__(self):
        return f"({self.left} * {self.right})"

    def accept(self, visitor):
        return visitor.visit_Mul(self)


class PrintVisitor:
    def visit(self, node):
        return node.accept(self)

    def visit_Num(self, node):
        return str(node.value)

    def visit_Add(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return f"({left} + {right})"

    def visit_Mul(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return f"({left} * {right})"




# ast = Add(Num(7), Mul(Num(3), Num(2)))
#
# pv = PrintVisitor()
# print(pv.visit(ast))

@given(st.integers(), st.integers(), st.integers())
def test_visitor(a, b, c):
    obj = Add(Num(a), Mul(Num(b), Num(c)))
    pv = PrintVisitor()
    assert pv.visit(obj) == f'({a} + ({b} * {c}))'

test_visitor()