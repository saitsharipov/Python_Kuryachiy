"""

Тестировщик
Написать класс Tester, при создании экземпляра которого ему передаётся единственный параметр
— некоторая функция fun. Сам экземпляр должен быть callable, и принимать два параметра —
последовательность кортежей suite и последовательность исключений allowed.
При вызове должна осуществляться проверка, можно ли функции fun() передавать каждый элемент
suite в качестве позиционных параметров. Если исключений не возникло, результат работы — 0,
если исключения попадали под классификацию одного из allowed, результат — -1, если же были исключения не из allowed — 1.

Примеры
Входные данные
T = Tester(int)
print(T([(12,), ("12", 16)], [ValueError, IndexError]))
print(T([(12,), ("12", 16), ("89", 8)], [ValueError, IndexError]))
print(T([(12,), ("12", 16), ("89", 8), (1, 1, 1)], [ValueError, IndexError]))

Результат работы
0
-1
1

"""



class Tester:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, suite, allowed=[]):
        """
        При вызове должна осуществляться проверка, можно ли функции fun() передавать каждый элемент suite
        в качестве позиционных параметров. Если исключений не возникло, результат работы — 0, если исключения
        попадали под классификацию одного из allowed, результат — -1, если же были исключения не из allowed — 1.
        """
        ans = 0
        for el in suite:
            try:
                self.fun(*el)
            except Exception as e:
                flag = False
                for a in allowed:
                    if isinstance(e, a):
                        flag = True
                if flag:
                    ans = -1
                else:
                    ans = 1
        return ans


# T = Tester(int)
# print(T([(12,), ("12", 16)], [ValueError, IndexError]))
# print(T([(12,), ("12", 16), ("89", 8)], [ValueError, IndexError]))
# print(T([(12,), ("12", 16), ("89", 8), (1, 1, 1)], [ValueError, IndexError]))