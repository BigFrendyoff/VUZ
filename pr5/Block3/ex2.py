import random
from collections import defaultdict
import inspect
import ast


class Mutator(ast.NodeTransformer):
    def visit_BinOp(self, node):
        operators = [ast.Add(), ast.Sub(), ast.Mult(), ast.Div()]  # список возможных операций
        op = random.choice(operators)  # выбор случайной операции
        return ast.BinOp(left=node.left, right=node.right, op=op)

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


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def mut_test_binary_ops(func, data, n_mutants, threshold=0.8):
    n_passed = round(len(data) * threshold)  # количество тестов, которые должен пройти мутант
    survived = []
    original_source = inspect.getsource(func)
    for mutant_source in make_mutants(original_source, n_mutants):
        try:
            exec(mutant_source)
            passed = []
            for i, d in enumerate(data):
                # проверяем, что мутант проходит тест на i-ом элементе из data
                assert func(d) == sorted(d)
                passed.append(i)
                if len(passed) >= n_passed:
                    # если мутант прошел достаточное количество тестов, добавляем его к списку выживших
                    survived.append(mutant_source)
                    break
        except:
            pass
    return survived


data = []
for i in range(10):
    arr = [random.randint(-100, 100) for _ in range(random.randint(1, 10))]
    data.append(arr)

survived_mutants = mut_test_binary_ops(quick_sort, data, 50)

print(f'{len(survived_mutants)} out of 50 mutants survived testing')

for mutant_source in survived_mutants:
    print(mutant_source)

