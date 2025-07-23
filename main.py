'''сделалили новую ветку и добавили новую функцию'''

def num(a: list):  # Подсказка: a должен быть списком
    return len(a)

# Вызовы функции
print(num([1, 2, 3]))  # OK (тип list)
print(num("abc"))       # Ошибки не будет, но тип не list!

def say():
    print('hi')

say()