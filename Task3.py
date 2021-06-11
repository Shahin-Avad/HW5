"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
Задача:
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.
Не забудьте, что сравнивать, например, можно операцию appendleft дека и insert списка и т.д.
"""
from collections import deque
from timeit import timeit

a = [i + 6 for i in range(10)]
b = deque()

for j in range(10):
    b.append(j + 6)

print(f"{a}, Выполнено за {timeit(number=1000000):.10f}")
print(f"{b}, Выполнено за {timeit(number=1000000):.10f}")
"""Операции добавления элементов по времени не сильно отличаются"""


a.reverse()
b.reverse()

print(f"{a}, Выполнено за {timeit(number=1000000):.10f}")
print(f"{b}, Выполнено за {timeit(number=1000000):.10f}")

"""Операция разворота элементов так же по времени не отличаются"""

print(f"{len(a)}, Выполнено за {timeit(number=1000000):.10f}")
print(f"{len(b)}, Выполнено за {timeit(number=1000000):.10f}")

"""Операция количества элементов: обращение к дек выполняется быстрее"""

print(f"{a[5]}, Выполнено за {timeit(number=1000000):.10f}")
print(f"{b[5]}, Выполнено за {timeit(number=1000000):.10f}")

"""Операция доступа к элементу по индексу: дек отрабатывает чуть быстрее"""


print(f"{a.pop()}, Выполнено за {timeit(number=1000000):.10f}")
print(f"{b.pop()}, Выполнено за {timeit(number=1000000):.10f}")

"""Операция удаления элемента с конца: дек отрабатывает чуть быстрее"""

"""[6, 7, 8, 9, 10, 11, 12, 13, 14, 15], Выполнено за 0.0129982000
deque([6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Выполнено за 0.0120258000
[15, 14, 13, 12, 11, 10, 9, 8, 7, 6], Выполнено за 0.0118481000
deque([15, 14, 13, 12, 11, 10, 9, 8, 7, 6]), Выполнено за 0.0110480000
10, Выполнено за 0.0125765000
10, Выполнено за 0.0115993000
10, Выполнено за 0.0120250000
10, Выполнено за 0.0113411000
6, Выполнено за 0.0127118000
6, Выполнено за 0.0113324000"""

"""deque хороша, когда частый доступ осуществляется только к концам коллекции.  
А если нужен доступ к элементам по индексу – лучше брать list"""
