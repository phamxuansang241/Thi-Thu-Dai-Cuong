import shutil
import os

target_dir = 'Data/'
add = '../'
source_dir = str('GT1/GT1/' + add)
file_names = os.listdir(source_dir)


for file_name in file_names:
    extend_of_target = ""
    for ite in range(0, 6):
        extend_of_target = extend_of_target + file_name[ite]
    extend_of_target = "20" + extend_of_target

    print(extend_of_target)
    print(source_dir + file_name)
    print(target_dir + extend_of_target)
    shutil.move(source_dir + file_name, target_dir + extend_of_target)
