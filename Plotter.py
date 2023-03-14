import matplotlib.pyplot as plt
import numpy as np
import os
from skimage.io import imread

def HeatMapplotter(filename_read, folder_save='Colormaps', suffix_save='new', colormap=plt.cm.plasma, save=True, dpi=300):
    """  
    Plots an image as heatmap. 
@filename: path to image
    """

    img =  np.array(imread(filename_read))
    create_folder = f"../{folder_save}"
    if save:
        if not os.path.exists(create_folder):
            os.makedirs(create_folder)

    new_name = filename_read.split("/")[-1] + f'_{suffix_save}.pdf'

    fig, ax = plt.subplots()
    cs = ax.matshow(img,cmap=colormap)
    plt.axis('off') 
    plt.savefig(f"{create_folder}/{new_name}", dpi=dpi) if save else None
    plt.show()
    plt.close()



def plotArts(dirname, folder_save='Colormaps_selection', suffix_save='viridis', colormap=plt.cm.plasma, save=True, dpi=300):
    """ 
    
    """
    os.chdir(dirname)
    oslist=os.listdir()   #Liste mit Pfaden zu Bildern, die neu geplottet werden sollen.

    for name in oslist:
        filename= os.path.join(dirname, name)
        if filename[-3:]=='bmp':
        
            HeatMapplotter(filename, folder_save=folder_save, suffix_save=suffix_save, colormap=colormap, save=save, dpi=dpi)
        