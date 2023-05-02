import random
from collections import defaultdict
import inspect
import ast
import string


def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5


class Mutator(ast.NodeTransformer):
    def visit_Constant(self, node):
        if isinstance(node.value, (int, float)):
            # заменяем числовые константы на случайные значения
            return ast.Constant(value=random.choice([0.5, 2.0, 2.0]))
        elif isinstance(node.value, str):
            # заменяем строковые константы на случайные строки
            return ast.Constant(value=''.join(random.choice(string.ascii_letters) for _ in range(10)))
        else:
            # оставляем остальные константы без изменений
            return node


def mutate_code(src):
    tree = ast.parse(src)
    Mutator().visit(tree)
    return ast.unparse(tree)


def make_mutants(func, size):
    mutant = src = ast.unparse(ast.parse(inspect.getsource(func)))
    mutants = [src]
    while len(mutants) < size + 1:
        mutant = mutate_code(src)
        mutants.append(mutant)
    return mutants[1:]


def mut_test(func, test, size=20):
    survived = []
    mutants = make_mutants(func, size)
    for mutant in mutants:
        try:
            exec(mutant, globals())
            test()
            survived.append(mutant)
        except:
            pass
    return survived

def my_test_distance():
    assert distance(0, 0, 3, 4) == 5.0
    assert distance(-1, -1, 2, 3) == 5.0

survived = mut_test(distance, my_test_distance, size=100)
print("Survived mutants:", len(survived))