# -*- coding: utf-8 -*-
"""
# Created by Guilhermi M. Crispi at Mon May 17 10:48:47 2021

============================
Titulo: # IMG_resize
Descricao: # https://stackoverflow.com/questions/21517879/python-pil-resize-all-images-in-a-folder
============================

"""
#%% IMPORTAR BIBLIOTECAS

from PIL import Image
import os, sys
import glob

#%% DEFINIR PASTA

path = 'C:/Users/guilh/Desktop/teste/tuta/images'


for filename in glob.iglob(path + '**/*.png', recursive=True):
    print(filename)
    im = Image.open(filename)
    imResize = im.resize((2048, 3840), Image.ANTIALIAS)
    imResize.save(filename , 'png', quality=90)