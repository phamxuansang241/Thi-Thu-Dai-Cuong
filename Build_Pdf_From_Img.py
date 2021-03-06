import os
from PIL import Image, ImageOps

root = "Data/"
list_branch = []
file_object = open('folder_mssv.txt', 'r')


def img_2_pdf(branch):
    source_dir = root + branch + '/'
    img_list_name = os.listdir(source_dir)
    out_pdf_name = "PDF_Data/" + branch + '/' + branch + '.pdf'

    images = []
    if(len(img_list_name) == 0):
        return

    for img in img_list_name:
        if(img == 'desktop.ini'):
            continue
        print(img)
        cur_img = Image.open(source_dir + img)
        print(cur_img)
        cur_img = ImageOps.exif_transpose(cur_img)

        if(cur_img.mode == 'RGBA'):
            cur_img = cur_img.convert("RGB")

        images.append(cur_img)

    images[0].save(out_pdf_name, save_all=True, quality=100, append_images=images[1:])


for line in file_object:
    if line not in list_branch:
        list_branch.append(line.strip())

for cur_branch in list_branch:
    img_2_pdf(cur_branch)
