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
import matplotlib.colors as  mcolors

NUM_min = 5
NUM_max = 20

class Die:
    def __init__(self, rulename, coordinate, content, amount):
        self.rulename = rulename
        self.coordinate = coordinate
        self.content = content
        self.amount = amount




def gen_chambermap():
    """Genetate chambermap"""
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


    ls = glob.glob(r'D:\map_stack\chamber\*.csv')

    Data = np.zeros((23,23))

    for i in ls :
        Data += pd.read_csv(i, header=None).values

    Data = Data.astype(int)


    one = pd.read_csv(r'D:\map_stack\original_map.csv',header=None).values

    Data2 = Data - (25*one)

    df = pd.DataFrame(Data2)
    df.to_csv(r"D:\map_stack\chamber_MAP.csv", index = False, header=False)

    draw(df)
    plt.savefig(rf"D:\map_stack\chamber_MAP.png", dpi=120)

    plt.show()

def check():
    data = pd.read_csv('chamber_MAP.csv',header=None).values
    rows, cols = np.where((data > NUM_min) & (data < NUM_max))
    pos = list(zip(rows, cols))
    return pos

def count(idx):
    chamber_amount = 0
    for x in range(0,len(idx)-1):
        if idx[x+1] == idx[x] and idx[x] == 2:
            chamber_amount += 1
    return chamber_amount+1

def rule_odd(pos):
    """奇數"""
    idx = []
    for i in range(1,26,2):
        df = pd.read_csv(f'chamber/{i}.csv',header=None)
        idx.append(df.iloc[pos])
    return idx

def rule_even(pos):
    """偶數"""
    idx = []
    for i in range(2,26,2):
        df = pd.read_csv(f'chamber/{i}.csv',header=None)
        idx.append(df.iloc[pos])
    return idx


if __name__ == '__main__':
    # gen_chambermap()
    pos = check()
    chamber_info = []

    for p in pos:
        content = rule_odd(p)
        c = count(content)
        die = Die('--Rule 1--', p, content, c)
        chamber_info.append(die)

    for x in chamber_info:
        # rulename, coordinate, content, amount
        if x.amount > 4:
            print(x.rulename)
            print(x.coordinate)
            print(x.content)
            print('---------Rule1 Break：---------')
            print([2*i+1 for i, e in enumerate(x.content) if e == 2])
            print(x.amount)
            print()

    for p in pos:
        content = rule_even(p)
        c = count(content)
        die = Die('--Rule 2--', p, content, c)
        chamber_info.append(die)

    for x in chamber_info:
        # rulename, coordinate, content, amount
        if x.amount > 4:
            print(x.rulename)
            print(x.coordinate)
            print(x.content)
            print('---------Rule2 Break：---------')
            print([2*i+2 for i, e in enumerate(x.content) if e == 2])
            print(x.amount)
            print()



