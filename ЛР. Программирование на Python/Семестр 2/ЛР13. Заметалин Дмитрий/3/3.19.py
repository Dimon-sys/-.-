#Вариант10

import os
import shutil

abs_path = os.getcwd()
l = os.listdir(abs_path + "\\3\\")
kirilitsa = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
for file in l:
    if set(file) & set(kirilitsa):
        os.remove(f'{abs_path}\\{file}')