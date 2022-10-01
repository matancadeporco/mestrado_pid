# -*- coding: utf-8 -*-
"""
# Created by Guilhermi M. Crispi at Tue Apr 27 13:18:54 2021

============================
Titulo: #Divide_images_to_patches
Descricao: #
============================

"""

#%%
import numpy as np
from patchify import patchify, unpatchify
import cv2
import os
from PIL import Image
import matplotlib.pyplot as plt


#%%

patch_size = 256
step = 256

image_path = "C:/Users/guilh/Desktop/h_masks/images/"
image_dataset = []
for img in os.listdir(image_path)
    #print(img)
    #Needs 8 bit, not float. ???
    image = cv2.imread(image_path+img, 1) # 0 corta cinza, como cortar RGB? 1 da erro em image_patches 
    banda1 = image[:,:,0]
    plt.imshow(banda1)
    #image = Image.fromarray(image)
    #image_dataset.append(np.array(image))
    
    image_patches = patchify((image), (patch_size, patch_size), step=step) ##coloco np.array erro muda de TypeError: `arr_in` must be a numpy ndarray para ,ValueError: `window_shape` is incompatible with `arr_in.shape`

    m, n = image_patches.shape[0], image_patches.shape[1]

    for i in range(m):
        for j in range(n):
            print(i,j)
            patch = image_patches[i,j]
            cv2.imwrite("C:/Users/guilh/Desktop/h_masks/256_patches_images/"
                        +img+str(i)+"_"+str(j)+".png", patch)
            

mask_path = "C:/Users/guilh/Desktop/h_masks/masks/"
mask_dataset = []
for msk in os.listdir(mask_path):
    #print(img)
    #Needs 8 bit, not float.???
    mask = cv2.imread(mask_path+msk, 0)
    mask = Image.fromarray(mask)
    mask_dataset.append(np.array(mask))
    
    mask_patches = patchify(mask, (patch_size, patch_size), step=step)

    x, y = mask_patches.shape[0], mask_patches.shape[1]

    for i in range(x):
        for j in range(y):
            print(i,j)
            patch = mask_patches[i,j]
            cv2.imwrite("C:/Users/guilh/Desktop/h_masks/256_patches_masks/"
                        +"_"+msk+str(i)+"_"+str(j)+".png", patch)
            

#%%
reconstructed_image = unpatchify(patches, image.shape)