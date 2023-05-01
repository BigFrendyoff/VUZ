import random
from collections import defaultdict
import inspect
import ast


class Mutator(ast.NodeTransformer):
    def visit_Constant(self, node):
        if isinstance(node.value, int) or isinstance(node.value, float):
            random_num = random.uniform(-1000, 1000)
            return ast.Constant(random_num)
        else:
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


def distance(x1, y1, x2, y2):
    return ((x2 + x1) ** 2 - (y2 + y1) ** 2) ** 0.25

def correct_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)


def tt_distance():
    assert distance(0, 0, 1, 0) == 1
    assert distance(0, 0, 0, 1) == 1
    assert distance(0, 0, 0, 0) == 0

def tt_correct_distance():
    assert correct_distance(0, 0, 1, 0) == 1
    assert correct_distance(0, 0, 0, 1) == 1
    assert correct_distance(0, 0, 0, 0) == 0



print(mut_test(correct_distance, tt_correct_distance, size=100))
