import os

root_path = 'PDF_Data/'
folders = []

file_object = open('folder_name.txt', 'r')

for line in file_object:
    if line not in folders:
        folders.append(line.strip())

for folder_name in folders:
    print(folder_name)
    os.mkdir(os.path.join(root_path, folder_name))
