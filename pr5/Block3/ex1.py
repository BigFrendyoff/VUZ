import random
from collections import defaultdict
import inspect
import ast


class Mutator(ast.NodeTransformer):
    def visit_Constant(self, node):
        if isinstance(node.value, int) or isinstance(node.value, float):
            random_num = random.uniform(-1000, 1000)  # генерация случайного числа
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


#создадим функцию, которая будет принимать на вход функцию Python и количество мутантов, которые мы хотим сгенерировать.
def mut_test_random_constants(func, n_mutants):
    survived, scope = [], {}
    mutants = make_mutants(func, n_mutants)
    for mutant in mutants:
        try:
            exec(mutant, scope)
            assert func(scope['data']) == scope['expected']
            survived.append(mutant)
        except AssertionError as e:
            print(f'Mutant failed: {mutant}, {e}')
    return survived


def mutate_me(data):
    # Данная функция должна суммировать все положительные числа в списке data,
    # но она содержит ошибку, которую мы попробуем найти с помощью мутационного тестирования

    sum = 0
    for num in data:
        if num > 0:
            sum += num ** 2  # ОШИБКА: нужно суммировать num, а не num ** 2
    return sum


def test_mutate_me():
    # Тесты для функции mutate_me()
    assert mutate_me([1, 2, 3]) == 14
    assert mutate_me([-1, 2, -3]) == 4
    assert mutate_me([0, 0]) == 0


data = [0, 2, 4, -1, 6, 7, -3, 5]
expected = 2 ** 2 + 4 ** 2 + 6 ** 2 + 7 ** 2 + 5 ** 2

# Протестируем функцию mutate_me() с помощью мутационного тестирования
survived_mutants = mut_test_random_constants(mutate_me, 50)

# Проверим, что все мутанты провалили тесты
assert len(survived_mutants) == 0