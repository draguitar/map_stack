

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors
import random

df = pd.read_excel(r"raw_map.xlsx", header=None)



def draw_rawmap(data, folder, imgname):
    sns.set(font_scale=1.5)
    fig, ax = plt.subplots(figsize=(10,10))
    # cmap = sns.color_palette("Pastel2", 3)
    # 淺綠色
    cmap = mcolors.LinearSegmentedColormap.from_list("n",['white', '#98fb98', 'red'])
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
    plt.savefig(f"{folder}/{imgname}.png", dpi=120)


def draw_defect_map(data, filename):
    sns.set(font_scale=1.5)
    fig, ax = plt.subplots(figsize=(10,10))
    # cmap = sns.color_palette("Pastel2", 3)
    cmap = mcolors.ListedColormap(['white', '#7cfc00', 'red', '#4872db', '#6e19c2'])
    sns.heatmap(data,
                center=2,
                cmap=cmap,
                fmt="d",
                linewidths=1,
                vmax=4, vmin=0,
                cbar=False
                )
    ax.set_title('',  fontsize=20)
    plt.savefig(filename, dpi=120)

def get_chance():
    x = random.randint(1,99)
    if x > 97 :
        return 2
    else :
        return 1


if __name__ == "__main__":
    # draw_rawmap(df.values)

    for x in range(1,5):
        ndry = pd.read_excel(r"raw_map.xlsx", header=None).values
        for i in range(27):
            for j in range(31):
                if ndry[i][j] == 1:
                    die = get_chance()
                    ndry[i][j] = die

        df = pd.DataFrame(ndry, columns=None)
        df.to_excel(f"xlsx/map_{x}.xlsx", index= False, header=False)
        draw_rawmap(df, "img",f"map_{x}")



