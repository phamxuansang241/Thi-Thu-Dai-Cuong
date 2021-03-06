import pandas as pd
import urllib.request
import math
import os


def change_name(old_name):
    new_name = ""
    cnt = 0
    for element in range(0, len(old_name)):
        if(old_name[element] == '@'):
            cnt = element

    for element in range(int(cnt) - 6, int(cnt)):
        new_name = new_name + old_name[element]

    return new_name


def checking(old_name, count, add):
    extend = ""
    for element in range(len(old_name) - 3, len(old_name)):
        extend = extend + old_name[element]

    if(extend == "jpg"):
        return str(change_name(old_name) + "_" + add + "_" + count + ".jpg")
    elif(extend == 'png'):
        return str(change_name(old_name) + "_" + add + "_" + count + ".png")
    elif(extend == 'peg'):
        return str(change_name(old_name) + "_" + add + "_" + count + ".jpeg")
    elif(extend == 'JPG'):
        return str(change_name(old_name) + "_" + add + "_" + count + ".JPG")


xyz = "GT1/GT1/"
add = "1a"
for count, filename in enumerate(os.listdir(xyz + add + "/")):
    dst = checking(filename, str(count), add)
    print(dst)
    src = xyz + add + '/' + filename
    des = xyz + add + '/' + str(dst)
    os.rename(src, des)
