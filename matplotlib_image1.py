# import a number of modules and sub-modules for image handling
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# inside of the project directory for this script there is a .png
# image of a bug for the image handling exercise with matplotlib
img = mpimg.imread('C:/Users/Luki/Documents/Python Scripts/Anaconda_files/stinkbug.png')
print(img)
