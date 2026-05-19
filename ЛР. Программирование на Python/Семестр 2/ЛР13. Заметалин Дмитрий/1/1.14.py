#Вариант10

import os

abs_path = os.getcwd()
os.makedirs(abs_path + '\\1\\school\\subjects')
os.mkdir(abs_path + '\\1\\school\\subjects\\math\\')
os.mkdir(abs_path + '\\1\\school\\subjects\\physics\\')
os.makedirs(abs_path + '\\1\\school\\notes')
print(abs_path)