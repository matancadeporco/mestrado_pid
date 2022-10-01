# -*- coding: utf-8 -*-
"""
# Created by Guilhermi M. Crispi at Wed Aug 25 09:47:00 2021

============================
Titulo: # Filtrar imagens com >95% de fundo e excluí-las
Descricao: # Restando apenas imagens/patches com informação das 3 classes
============================

"""

#%%
import os
import cv2
import numpy as np
import random
from matplotlib import pyplot as plt

#%% Checkpoint - plotar imagem e máscara treinamento 

#train_img_dir = "D:/DB_tuta_separated_PS/train/256_images/"
#train_mask_dir = "D:/DB_tuta_separated_PS/train/256_masks/"

train_img_dir = "D:/DB_tuta_separated_PS/train_2/256_images/"
train_mask_dir = "D:/DB_tuta_separated_PS/train_2/256_masks/"

img_list = os.listdir(train_img_dir)
msk_list = os.listdir(train_mask_dir)

num_images = len(os.listdir(train_img_dir))


img_num = random.randint(0, num_images-1)

img_for_plot = cv2.imread(train_img_dir+img_list[img_num], 1)
img_for_plot = cv2.cvtColor(img_for_plot, cv2.COLOR_BGR2RGB)

mask_for_plot =cv2.imread(train_mask_dir+msk_list[img_num], 0)

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(img_for_plot)
plt.title('Image')
plt.subplot(122)
plt.imshow(mask_for_plot, cmap='gray')
plt.title('Mask')
plt.show()


#%% Varrer as máscaras e copiar apenas as com informações relevantes
# ignorar as mascaras que tiverem apenas fundo (pixel 0) 95% de fundo

useless=0  #Useless image counter
for img in range(len(img_list)):   #Using t1_list as all lists are of same size
    img_name=img_list[img]
    mask_name = msk_list[img]
    print("Now preparing image and masks number: ", img)
      
    temp_image=cv2.imread(train_img_dir+img_list[img], 1)
   
    temp_mask=cv2.imread(train_mask_dir+msk_list[img], 0)
    #temp_mask=temp_mask.astype(np.int64) #uint8 # estva comentando esta linha
    
    val, counts = np.unique(temp_mask, return_counts=True)
    
    if (1 - (counts[0]/counts.sum())) > 0.05:  #At least 5% useful area with labels that are not 0
        print("Save Me")
        cv2.imwrite('D:/DB_tuta_separated_PS/train_2/images/'+img_name, temp_image)
        cv2.imwrite('D:/DB_tuta_separated_PS/train_2/masks/'+mask_name, temp_mask)
        
    else:
        print("I am useless")   
        useless +=1

print("Total useful images are: ", len(img_list)-useless)  #12810
print("Total useless images are: ", useless)  #35670
