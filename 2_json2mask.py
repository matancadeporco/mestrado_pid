# -*- coding: utf-8 -*-
"""
# Created by Guilhermi M. Crispi at Mon May 24 10:48:44 2021

============================
Titulo: #Entre com o título do projeto aqui
Descricao: #Entre com a descrição aqui
============================

"""

#%%

import os
#%%

path = 'D:/BD_resized_n_annotated/tuta/new'
json_file = os.listdir(path)
os.system("activate labelme")
for file in json_file: 
    os.system("labelme_json_to_dataset.exe %s"%(path + '/' + file))