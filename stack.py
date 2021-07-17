# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 12:34:15 2021

@author: dragu
"""

import glob
import numpy as np
import pandas as pd

from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors
# %%
def draw(data):
    """Draw HeatMap"""
    sns.set(font_scale=0.8)
    fig, ax = plt.subplots(figsize=(10,8))

    # cmap = mcolors.LinearSegmentedColormap.from_list("n",['#f0f8ff','#008080','#0000ff','#ffff00','#ff0000','#000000'])
    cmap= mcolors.ListedColormap(['gray', 'pink','green' ,'blue', 'yellow','orange','red'])
    sns.heatmap(data,
                cmap = cmap,
                annot=True,
                fmt="d",
                linewidths=1,
                vmax=7, vmin=2,
                mask= data<1
                )
    ax.set_title('wafer')

# %%
ls = glob.glob(r'D:\map_stack\chamber\*.csv')
# %%
Data = np.zeros((23,23))

for i in ls :
    Data += pd.read_csv(i, header=None).values

Data = Data.astype(int)

# %%
one = pd.read_csv(r'D:\map_stack\original_map.csv',header=None).values

Data2 = Data - (25*one)

print(Data2)
# %%

df = pd.DataFrame(Data2)
df.to_csv(r"D:\map_stack\ALL_MAP.csv", index = False, header=False)
# %%
draw(df)
plt.savefig(rf"D:\map_stack\stack_map.png", dpi=120)
# %%
plt.show()
# %%
