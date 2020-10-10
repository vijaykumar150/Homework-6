import os
import sys

file= sys.argv[1]
print('File Path: ' + os.path.abspath(file))
for root, subdirs, files in os.walk(file):
    list_file_path = os.path.join(root, 'file.txt')
    with open(list_file_path, 'w') as list_file:
        for j in subdirs:
            print('\t- subdirectory ',j)
        for i in files:
            file_path = os.path.join(root, i)
            with open(file_path, 'r') as fp:
                f_content = fp.read()
                list_file.write(('The file %s contains:\n' %i).encode('utf-8'))
                list_file.write(f_content)
                list_file.write(b'\n')