# import a number of modules and sub-modules for image handling
import matplotlib.pyplot as plt
import skimage.exposure as exp
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
    # display the image - 2 of them for single "fig"  - ax1 (the
    # image) and ax2 (histogram plot)
    # (represented by 2 axes) as subplots of single plot window
    # with set size
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,3))
    # ax1 as image from input variable, grey cmap and no axis
    ax1.imshow(img, cmap=plt.cm.gray)
    ax1.set_axis_off()

    # prepare the histogram
    ax2.hist(img.ravel(), lw=0, bins=256)
    ax2.set_xlim(0, img.max())
    ax2.set_yticks([])
    # display plot
    plt.show()


# run the function for selected image
show_img(img1)
# a way to dim the image
# show_img(exp.rescale_intensity(img1,
# in_range=(0.4, .95), out_range=(0, 1)))
# a method to increase contrast and balance of the picture
show_img(exp.equalize_adapthist(img1))
