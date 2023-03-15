import matplotlib.pyplot as plt
import numpy as np
import os
from skimage.io import imread

def HeatMapplotter(filename_read, folder_save='Colormaps', suffix_save='new', colormap=plt.cm.plasma, save=True, format='pdf', dpi=300):
    """  
    Plots a single image as heatmap and saves it if save is True.

    @args:
    filename_read: (String) path to image.
    folder_save: (String) name of folder where new heatmap should be saved.
    suffix_save: (String) suffix of created file to be saved.
    colormap: (plt.cm) plt colormap scheme for heatmap.
    save: (Boolean) True or False.
    dpi: (int) defines resolution of saved heatmap as pdf. 
    """
    #Load image data.
    img =  np.array(imread(filename_read))
    #Create folder to save created heatmap if it does not already exist!
    create_folder = f"{folder_save}"
    if save:
        if not os.path.exists(create_folder):
            os.makedirs(create_folder)

    #Define new filename with suffix.
    filename = filename_read.split("/")[-1]
    new_name = filename.split(".")[0] + f'_{suffix_save}.{format}'

    fig, ax = plt.subplots()
    cs = ax.matshow(img,cmap=colormap)
    plt.axis('off') 
    plt.savefig(f"{create_folder}/{new_name}", bbox_inches='tight', dpi=dpi) if save else None
    plt.show()
    plt.close()



def plotArts(dirname, folder_save='Colormaps_selection', suffix_save='viridis', colormap=plt.cm.plasma, save=True, format='pdf', dpi=300):
    """ 
    Plots all bmp files contained in dirname with method HeatMapplotter().
    Heatmaps are saved, if save=True, with the given suffix in the folder 'folder_save'. 
    """
    #Create a List with paths to all files contained in dirname.
    oslist=os.listdir(dirname)

    for name in oslist:
        filename= os.path.join(dirname, name)
        #Process only bmp files.
        if filename[-3:]=='bmp':
        
            HeatMapplotter(filename, folder_save=folder_save, suffix_save=suffix_save, colormap=colormap, save=save, format=format, dpi=dpi)
        
