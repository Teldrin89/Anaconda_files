# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:48:23 2018

@author: 502236423
"""
# import 6 functions from 2 libraries to calculate the sin, pi values,
# to get the linearly spaced values, to create a subplots in
# single plot and show it
from numpy import sin, pi, linspace
from pylab import plot, show, subplot

# definition of "a" and "b" parameters for lissajous curve - the appearance
# of those figures in subplots is highly sensitive to the ratio of "a/b"
# so in this case we have 4 plots with ratios: 1/1, 3/5, 5/7 and 3/4
# to simply figure out what are the "a" and "b" of a given plot you could
# simply count the number of inversions in "x" and "y" axis (for "a" and "b"
# parameters in that order)

# both "a" and "b" have been assigned multiple values - creating a list
a = [1, 3, 5, 3]  # plotting the curves for
b = [1, 5, 7, 4]  # different values of a/b
c = ["green", "red", "blue", "black"]
# Delta value have been specified as pi/2 which for "a/b" ratio = 1 should
# produce a common circle (for delta = 0 would be line and for every other
# value of delta - ellipse)
delta = pi / 2
# since "pi" value is a float - the resulting delta is also a float

# variable "t" has been assigned with list of numbers generated using the
# "linspace" function - it generate evenly distributed numbers from and to
# specified value and given number of values - in this case from "-pi" to
# "pi" - 300 values
t = linspace(-pi, pi, 300)

# for loop will run 4 times (in range from 0  to 4 - but the key part is that
# loops in python are running "up to but no including" specified value)
for i in range(0, 4):
    # the "x" and "y" equations are specific for lissajous curve generation
    # with already described parameters as "a", "b" and "delta"
    # the "t" variable used here specifies how many point will be used in
    # creation of a single curve - the range is a full circle (in rad) and
    # the resulting "x" and "y" variables (similar as in "delta" example)
    # will be lists of the same size, containing the float type values
    x = sin(a[i] * t + delta)
    y = sin(b[i] * t)

    # the subplot function allows to place several plots in one "plot window"
    # the parameters to be defined are the number of plots in a row, then in
    # a column and then the plot index to decide where a given plot should be
    # placed
    subplot(2, 3, i + 1)
    # a simple plot function for "x" and "y" variables calculated before - it
    # will be placed in a subplot defined in previous line
    plot(x, y, color=c[i])
# function to show the resulting "plot window" with all subplots
show()
