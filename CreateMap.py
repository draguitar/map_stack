

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors
import pandas as pd

import random

df = pd.read_csv(r"Openshort\1.csv", header=None)
df2 = pd.read_csv(r"Openshort\多類型.csv", header=None)



def draw_oneclass(data):
    sns.set(font_scale=1.5)
    fig, ax = plt.subplots(figsize=(10,10))
    # cmap = sns.color_palette("Pastel2", 3)
    cmap = mcolors.LinearSegmentedColormap.from_list("n",['white', '#e3e3e3', 'red'])
    sns.heatmap(data,
                center=1,
                cmap=cmap,
                # annot=True,
                fmt="d",
                linewidths=1,
                vmax=2, vmin=0,
                # mask=data<1,
                cbar=False
                )
    ax.set_title('',  fontsize=20)
    plt.savefig(f"ddd.png", dpi=120)


def draw_mutipleclasses(data, filename):
    sns.set(font_scale=1.5)
    fig, ax = plt.subplots(figsize=(10,10))
    # cmap = sns.color_palette("Pastel2", 3)
    cmap = mcolors.ListedColormap(['white', '#e3e3e3', 'red', '#4872db', '#6e19c2'])
    sns.heatmap(data,
                center=2,
                # cmap= 'RdBu',
                cmap=cmap,
                # annot=True,
                fmt="d",
                linewidths=1,
                vmax=4, vmin=0,
                cbar=False
                )
    ax.set_title('',  fontsize=20)
    plt.savefig(f"{filename}.png", dpi=120)

def replace_data(data, src, dist):
    data[data == src] = dist
    return data


if __name__ == "__main__":
    draw_oneclass(df.values)
    draw_mutipleclasses(df2.values, 'eee')
    # 保留2，其餘轉為1
    # f = replace_data(df2.values, 3, 1)
    # f = replace_data(f, 4, 1)
    # draw_mutipleclasses(f, 'fff')
    # 保留3，其餘轉為1
    # g = replace_data(df2.values, 2, 1)
    # g = replace_data(g, 4, 1)
    # draw_mutipleclasses(g, 'ggg')
    # 保留4，其餘轉為1
    h = replace_data(df2.values, 2, 1)
    h = replace_data(h, 3, 1)
    draw_mutipleclasses(h, 'hhh')