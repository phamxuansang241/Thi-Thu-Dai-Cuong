import pandas as pd
import urllib.request
import math


opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)


def url_to_jpg(i, _url, file_path):
    filename = 'image-{}.jpg'.format(i)
    full_path = '{}{}'.format(file_path, filename)

    urllib.request.urlretrieve(_url, full_path)
    print('{} saved.'.format(filename))

    return None


# Set Constants
File_Name = 'list.csv'
File_Path = 'Data/'

urls = pd.read_csv('list.csv')
df = urls

df.fillna(str(0), inplace=True)
for index, row in df.iterrows():
    path_mssv = File_Path + str(row[0]) + '/'
    print(path_mssv)
    for i in range(1, 10):
        #         print(row[i])
        if(row[i] != '0'):
            #             url_to_jpg(i, row[i], path_mssv)
            print(row[i])
    print()

url_to_jpg(3, 'https://husteduvn-my.sharepoint.com/personal/duy_bk195864_sis_hust_edu_vn/Documents/Apps/Microsoft%20Forms/GT1/C%C3%A2u%20h%E1%BB%8Fi%206/4_Hieu.CD202376@sis.hu.jpg', File_Path)
