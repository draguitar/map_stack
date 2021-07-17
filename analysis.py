# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 10:14:41 2021

@author: dragu
"""
import glob
import numpy as np
import pandas as pd

from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors

def draw(data):
    sns.set(font_scale=0.8)
    fig, ax = plt.subplots(figsize=(10,8))
    # cmap = sns.color_palette("Pastel2", 3) 
    cmap = mcolors.LinearSegmentedColormap.from_list("n",['#f0f8ff','#7cfc00','#ff0000'])
    sns.heatmap(data, 
                robust = True,
                center=0, 
                cmap=cmap,
                annot=True,
                fmt="d",
                linewidths=1, 
                vmax=4, vmin=-1,
                mask= data<0
                )
    ax.set_title('wafer')

ls = glob.glob('mapfile/*.csv') 
  
name = 0  

for i in ls :
    raw_map = pd.read_csv(i, header=None)
    all_map = pd.read_csv('ALL_MAP.csv', header=None)
    for i in range(23):
        for j in range(23):
            if raw_map.iloc[i,j] == 0:
                all_map.iloc[i,j] = -1
            elif raw_map.iloc[i,j] == 1 :
                all_map.iloc[i,j] = 0
    draw(all_map)
    
    plt.savefig(f"output/{name}.png", dpi=120)
    name += 1
    
# %%
           
           