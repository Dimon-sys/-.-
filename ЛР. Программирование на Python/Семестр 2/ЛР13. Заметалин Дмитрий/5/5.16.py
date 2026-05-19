#Вариант10

import os
import zipfile

abs_path = os.getcwd()
l = os.listdir(abs_path + "\\5\\")
print(l)
with zipfile.ZipFile('my.zip', 'w', zipfile.ZIP_DEFLATED) as myzip:
    for file in l:
        file_path = os.path.join(abs_path + '\\5\\', file)
        arcname = os.path.relpath(file_path, start=f'{abs_path}')
        if os.path.getsize(file_path) < 100000000:
            myzip.write(file_path, arcname)