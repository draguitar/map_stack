

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors
import pandas as pd

import random

def draw(data):
    sns.set(font_scale=1.5)
    fig, ax = plt.subplots(figsize=(10,10))
    # cmap = sns.color_palette("Pastel2", 3)
    cmap = mcolors.LinearSegmentedColormap.from_list("n",['#f0f8ff','#7cfc00','#ff0000'])
    sns.heatmap(data,
                center=1,
                # cmap= 'RdBu',
                cmap=cmap,
                # annot=True,
                fmt="d",
                linewidths=1,
                vmax=2, vmin=0,
                mask= data<1,
                cbar=False
                )
    ax.set_title('wafer',  fontsize=20)

# df = pd.read_csv(r"D:\map.csv", header=None)
# draw(df)

def get_card(x):
    sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16]
    c = random.choice(sequence)
    return(c <= x)

# %%
for k in range(25):
    df = pd.read_csv('map.csv',header=None)
    for i in range(23):
       for j in range(23):
           if df.iloc[i,j] == 1 and get_card(0):
               df.iloc[i,j] = 2

    df.to_csv(f'mapfile/map_{k}.csv', index = False, header=False)
    draw(df)
    plt.savefig(f"mapfile/map_{k}.png", dpi=120)
# %%
# import glob
# import os
# ls = glob.glob('chamber/*.csv')

# for l in ls:
#     df = pd.read_csv(l, header=None)
#     filename = os.path.basename(l).split(".")[0]
#     draw(df)
#     plt.savefig(f"demo/{filename}.png", dpi=120)
    
# %%    

for k in range(1,12):
    df = pd.read_csv('33.csv',header=None)
    for i in range(3):
       for j in range(3):
           if df.iloc[i,j] == 1 and get_card(0):
               df.iloc[i,j] = 2

    df.to_csv(f'33demo/map_{k}.csv', index = False, header=False)
    draw(df)
    plt.savefig(f"33demo/map_{k}.png", dpi=120)
    


# %%    
for k in range(1,13):
    df = pd.read_csv(f'33demo/map_{k}.csv',header=None)
    draw(df)
    plt.savefig(f"33demo/map_{k}.png", dpi=100)
    
# %%   
df = pd.read_csv(f'ddd/map.csv',header=None)
draw(df)
plt.savefig(f"ddd/map.png", dpi=100)
# %% 
amount = -1
assert amount > 0 ,'要大於0'

# %%