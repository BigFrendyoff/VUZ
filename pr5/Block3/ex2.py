import random
from collections import defaultdict
import inspect
import ast

def sum_positive_numbers(numbers):
    return sum([x**2 for x in numbers if x > 0])

def mutate_code(src):
    tree = ast.parse(src)
    Mutator().visit(tree)
    return ast.unparse(tree)

class Mutator(ast.NodeTransformer):
    def visit_Constant(self, node):
        if isinstance(node.value, int):
            node.value = random.randint(-100, 100)
        return node


BINARY_OPERATORS = [ast.Add(), ast.Sub(), ast.Mult(), ast.Div()]

class Mutator(ast.NodeTransformer):
    def visit_BinOp(self, node):
        node.left = self.visit(node.left)
        node.right = self.visit(node.right)
        if isinstance(node.op, ast.Add):
            node.op = random.choice(BINARY_OPERATORS)
        return node


def sort_numbers(numbers):
    return sorted(numbers)


import random
from collections import defaultdict
import inspect
import ast

BINARY_OPERATORS = [ast.Add(), ast.Sub(), ast.Mult(), ast.Div()]

class Mutator(ast.NodeTransformer):
    def visit_Constant(self, node):
        if isinstance(node.value, int):
            node.value = random.randint(-100, 100)
        return node

    def visit_BinOp(self, node):
        node.left = self.visit(node.left)
        node.right = self.visit(node.right)
        if isinstance(node.op, ast.Add):
            node.op = random.choice(BINARY_OPERATORS)
        return node

def mutate_code(src):
    tree = ast.parse(src)
    Mutator().visit(tree)
    return ast.unparse(tree)

def make_mutants(func, size):
    mutant = src = ast.unparse(ast.parse(inspect.getsource(func)))
    mutants = [src]
    while len(mutants) < size + 1:
        while mutant in mutants:
            mutant = mutate_code(src)
        mutants.append(mutant)
    return mutants[1:]

def mut_test(func, test, size=20):
    survived, scope = [], {}
    mutants = make_mutants(func, size)
    for mutant in mutants:
        try:
            exec(mutant, scope)
            exec(inspect.getsource(test), scope)
            survived.append(mutant)
        except:
            pass
    return survived

def sum_positive_numbers(numbers):
    return sum([x**2 for x in numbers if x > 0])

def test_sum_positive_numbers():
    assert sum_positive_numbers([1, 2, 3]) == 14
    assert sum_positive_numbers([-1, 2, 3]) == 13
    assert sum_positive_numbers([1, -2, 3]) == 10
    assert sum_positive_numbers([1, 2, -3]) == 5
    assert sum_positive_numbers([-1, -2, -3]) == 0

def sort_numbers(numbers):
    return sorted(numbers)

def test_sort_numbers():
    assert sort_numbers([1, 2, 3]) == [1, 2, 3]
    assert sort_numbers([3, 2, 1]) == [1, 2, 3]
    assert sort_numbers([2, 3, 1]) == [1, 2, 3]
    assert sort_numbers([1]) == [1]
    assert sort_numbers([]) == []


survived = mut_test(sum_positive_numbers, test_sum_positive_numbers)
assert not survived, f"{len(survived)} mutants survived: {survived}"
survived = mut_test(sort_numbers, test_sort_numbers)
assert not survived, f"{len(survived)} mutants survived: {survived}"