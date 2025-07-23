import os, time

source = ['/Users/m1pro/IT/test1', '/Users/m1pro/IT/test2']
target_dir = '/Users/m1pro/IT/rescopy'

today = target_dir + os.sep + time.strftime('%Y-%m-%d')
now = time.strftime('%H%M%S')

__version__ = 3.0