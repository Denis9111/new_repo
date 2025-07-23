import os, time

source = ['/Users/m1pro/IT/test1', '/Users/m1pro/IT/test2']
target_dir = '/Users/m1pro/IT/rescopy'
'''сделалили новую ветку и добавили новую функцию'''

today = target_dir + os.sep + time.strftime('%Y-%m-%d')
now = time.strftime('%H%M%S')

# Вызовы функции
print(num([1, 2, 3]))  # OK (тип list)
print(num("abc"))       # Ошибки не будет, но тип не list!