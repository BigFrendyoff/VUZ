def bucketsort(arr, k):
    """
    Сортирует массив arr с помощью алгоритма Bucket Sort.

    Аргументы:
    arr (list): список элементов для сортировки
    k (int): количество корзин

    Возвращает:
    list: отсортированный список элементов

    Примеры:
    >>> bucketsort([3, 1, 4, 2], 4)
    [1, 2, 3, 4]
    >>> bucketsort([5, 2, 9, 3, 6], 3)
    [2, 3, 5, 6, 9]
    >>> bucketsort([], 5)
    []
    """
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

# Тестирование на случайных данных
import random
for i in range(10):
    arr = [random.randint(0, 100) for _ in range(20)]
    k = random.randint(2, 10)
    expected = sorted(arr)
    assert bucketsort(arr, k) == expected

# Функция-спецификация
def test_bucketsort():
    # Сортировка пустого массива
    assert bucketsort([], 5) == []

    # Сортировка массива из одного элемента
    assert bucketsort([1], 5) == [1]

    # Сортировка массива из нескольких элементов
    assert bucketsort([3, 1, 4, 2], 4) == [1, 2, 3, 4]
    assert bucketsort([5, 2, 9, 3, 6], 3) == [2, 3, 5, 6, 9]

    # Сортировка массива с повторяющимися элементами
    assert bucketsort([3, 1, 4, 2, 1, 4], 4) == [1, 1, 2, 3, 4, 4]

    # Сортировка отсортированного массива
    assert bucketsort([1, 2, 3, 4], 4) == [1, 2, 3, 4]

    # Сортировка в обратном порядке отсортированного массива
    assert bucketsort([4, 3, 2, 1], 4) == [1, 2, 3, 4]

    # Сортировка массива с отрицательными элементами
    assert bucketsort([-3, -1, -4, -2], 4) == [-4, -3, -2, -1]