# import a number of modules and sub-modules for image handling
import matplotlib.pyplot as plt
import urllib3
import matplotlib.image as mpimg
from skimage import io
from urllib.request import urlopen


# the .png has been uploaded to github folder with address inside
# the code = image of a bug for the image handling exercise with
# matplotlib

# for opening of the image use urlopen from urllib module
f = urlopen("https://github.com/Teldrin89/Anaconda_files/blob/master/stinkbug.png?raw=true")

# different method url image loading
# img3 = io.imread("https://github.com/Teldrin89/Anaconda_files/blob/master/stinkbug.png?raw=true")

# use matplotlib pyplot method for reading of the image (assigned
# to "f" variable from url
img1 = plt.imread(f)


# function for showing image and histogram of said image
def show_img(img):
    # display the image
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,3))

    ax1.imshow(img, cmap=plt.cm.gray)
    ax1.set_axis_off()

    # display the histogram
    ax2.hist(img.ravel(), lw=0, bins=256)
    ax2.set_xlim(0, img.max())
    ax2.set_yticks([])
    
    plt.show()


# run the function for selected image
show_img(img1)
