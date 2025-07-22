# ''' прога копирования файлов '''
#
# import os, time
#
# source = ['/Users/m1pro/IT/test1', '/Users/m1pro/IT/test2']
# target_dir = '/Users/m1pro/IT/rescopy'
#
# target = target_dir + os.sep + time.strftime('%Y-%m-%d_%H-%M-%S') + '.zip'
# print(target)
#
# zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
# print(zip_command)
#
# if os.system(zip_command) == 0:
#     print('Резервная копия успешно создана в', target)
#     print(target)
# else:
#     print('Создание резервной копии НЕ УДАЛОСЬ')
#
# __version__ = '1.0'
#
# print(__doc__)

# import os, time
#
# source = ['/Users/m1pro/IT/test1', '/Users/m1pro/IT/test2']
# target_dir = '/Users/m1pro/IT/rescopy'
#
# today = target_dir + os.sep + time.strftime('%Y-%m-%d')
# now = time.strftime('%H%M%S')
#
# if not os.path.exists(today):
#     os.mkdir(today)
#     print('каталог успешно создан:', today)
#
# target = today + os.sep + now + '.zip'
#
# zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
#
# if os.system(zip_command) == 0:
#     print('Резервная копия успешно создана в', target)
#     print(target)
# else:
#     print('Создание резервной копии НЕ УДАЛОСЬ')
#
# __version__ = '2.0'


import os, time

source = ['/Users/m1pro/IT/test1', '/Users/m1pro/IT/test2']
target_dir = '/Users/m1pro/IT/rescopy'

today = target_dir + os.sep + time.strftime('%Y-%m-%d')
now = time.strftime('%H%M%S')

comment = input('Введи небольшой коммент к файлу, он будет использован в названии...')
if len(comment) == 0:
    print('Не захотел оставлять коммент ? ну потом сам будешь искать что и где ...')
    target = today + os.sep + now + '.zip'
else:
    target = (today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip')

if not os.path.exists(today):
    os.mkdir(today)
    print('каталог успешно создан:', today)


zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
    print(target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')

__version__ = '3.0'















