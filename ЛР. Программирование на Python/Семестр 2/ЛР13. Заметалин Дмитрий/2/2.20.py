#Вариант10

import os
import shutil

abs_path = os.getcwd()
l = os.listdir(abs_path + "\\2\\")
for file in l:
    if file == '2.20.py':
        continue
    if not(os.path.isdir(abs_path + "\\2\\" + file[0])):
        os.mkdir(f'{abs_path}\\2\\{file[0]}')
    shutil.move(f'{abs_path}\\2\\{file}', f'{abs_path}\\2\\{file[0]}')