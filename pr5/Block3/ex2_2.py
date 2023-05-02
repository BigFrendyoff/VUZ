import random
from collections import defaultdict
import inspect
import ast
import string

#Функция сортировки
def bucketsort(arr, k):
    if len(arr) == 0:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    bucket_size = (max_val - min_val) / k + 1
    buckets = [[] for _ in range(k)]

    for x in arr:
        i = int((x - min_val) / bucket_size)
        buckets[i].append(x)

    sorted_arr = []
    for i in range(k):
        sorted_arr.extend(sorted(buckets[i]))

    return sorted_arr


class Mutator(ast.NodeTransformer):
    # def visit_Constant(self, node):
    #     if isinstance(node.value, (int, float)):
    #         # заменяем числовые константы на случайные значения
    #         return ast.Constant(value=random.choice([0.5, 2.0]))
    #     elif isinstance(node.value, str):
    #         # заменяем строковые константы на случайные строки
    #         return ast.Constant(value=''.join(random.choice(string.ascii_letters) for _ in range(10)))
    #     else:
    #         # оставляем остальные константы без изменений
    #         return node

    def visit_BinOp(self, node):
        # заменяем бинарные операции на случайные операции
        left = self.visit(node.left)
        right = self.visit(node.right)
        op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.Div()])
        return ast.BinOp(left=left, right=right, op=op)


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

def my_test_bucketsort():
    assert bucketsort([3, 1, 4, 2], 4) == [1, 2, 3, 4]
    assert bucketsort([5, 2, 9, 3, 6], 3) == [2, 3, 5, 6, 9]
    assert bucketsort([], 5) == []

survived = mut_test(bucketsort, my_test_bucketsort, size=100)
print("Survived mutants:", len(survived))