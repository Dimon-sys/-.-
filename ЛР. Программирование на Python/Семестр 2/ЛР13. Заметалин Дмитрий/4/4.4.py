#Вариант10

import os
import shutil

abs_path = os.getcwd()
l = os.listdir(abs_path + "\\4\\logs\\")
l.sort(key=os.path.getmtime, reverse=True)
print(l)