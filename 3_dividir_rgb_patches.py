# -*- coding: utf-8 -*-
"""
# Created by Guilhermi M. Crispi at Fri May 28 11:02:28 2021

============================

Titulo: # dividir imagens RGB em patches
Descricao: # https://stackoverflow.com/questions/5953373/how-to-split-image-into-multiple-pieces-in-python

============================

"""

#%%

import os
import glob
from PIL import Image
Image.MAX_IMAGE_PIXELS = None # to avoid image size warning

#%%

#D:\BD_resized_n_annotated\BD_Masks
imgdir = "D:/BD_resized_n_annotated/BD_Masks/tuta/images/"
filelist = [f for f in glob.glob(imgdir + "**/*.png", recursive=True)]
savedir = "D:/BD_resized_n_annotated/BD_Masks/tuta/256_patches_images_t/"

start_pos = start_x, start_y = (0, 0)
cropped_image_size = w, h = (256,256)

for file in filelist:
    img = Image.open(file)
    width, height = img.size

    frame_num = 1
    for col_i in range(0, width, w):
        for row_i in range(0, height, h):
            crop = img.crop((col_i, row_i, col_i + w, row_i + h))
            name = os.path.basename(file)
            name = os.path.splitext(name)[0]
            save_to= os.path.join(savedir, name+"_{:03}.png")
            crop.save(save_to.format(frame_num))
            frame_num += 1