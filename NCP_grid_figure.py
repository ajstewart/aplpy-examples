#!/usr/bin/env python

# This script gives an example of how to create a grid of figures.
# Also shows how to create the inset lines used in my paper.

import aplpy
import matplotlib
import matplotlib.pyplot as plt

def standard_options(fplot):
    #Standard settings in a function.
    fplot.recenter(15., 90., 8.)
    fplot.set_theme('publication')
    fplot.add_beam()
    fplot.beam.set_frame(True)
    fplot.beam.set_facecolor('black')
    fplot.add_grid()
    fplot.grid.set_color('black')
    fplot.grid.set_alpha(0.1)
    fplot.add_colorbar()
    fplot.axis_labels.set_xtext('Right Ascension (J2000)')
    fplot.axis_labels.set_ytext('Declination (J2000)')
    fplot.axis_labels.set_font(size='large')
    fplot.tick_labels.set_yformat('dd')
    fplot.tick_labels.set_xformat('hh')
    fplot.tick_labels.set_font(size='medium')
    fplot.ticks.set_xspacing(15)
    fplot.ticks.set_yspacing(1)
    
def plotinitial(figure, images, ranges):
    #This function just loops through the figure creating the subplots and loading the images.
    panels={}
    for n in range(0, len(images)):
        key=n+1
        panels[key]=aplpy.FITSFigure(images[n], figure=fig, subplot=(2,2,n+1))
        panels[key].show_grayscale(vmin=ranges[n][0], vmax=ranges[n][1])
    return panels
    
#define list of images
images=['L42243_30secs.fits', 'L40979_SAP003_SB240_uv.MS.NEW_Feb13_1CHNL.dppp.dppp.prepeel.2500clip.img.fits', 'NCP_BLOCK0059_297Mins.fits', 'NCP_BLOCK0059_297Mins.fits']
#List of vmin and vmax values to use for each image
ranges=[[2.0,20.], [0.5,4.], [0.05,1.875], [0.05,1.875]]

fig = plt.figure(figsize=(15.5, 12))

#Load fits files into subplots and perform standard options
plots=plotinitial(fig, images, ranges)
for p in plots:
    standard_options(plots[p])

#Seperate recenter for the 4th plot
plots[4].recenter(15., 90., 4.)
#Create a circle of radius 7.5 deg on plots 1-3
plots[1].show_circles([15.,], [90.,], radius=7.5, layer='trap-circle-f1')
plots[2].show_circles([15.,], [90.,], radius=7.5, layer='trap-circle-f1')
plots[3].show_circles([15.,], [90.,], radius=7.5, layer='trap-circle-f1')
#Create rectangle on plot 3 for zoom in effect.
plots[3].show_rectangles([15.,], [90.,], width=8., height=8., layer='rectangle-test', alpha=0.5)

#Here I convert the pixel values of 3C 61.1 to world coordinates so I can easily place a box around it with the next line (+text)
pos_x, pos_y=plots[1].pixel2world(891,670)
plots[1].show_rectangles([pos_x,], [pos_y,], width=1.0, height=1.0, layer='3C61-box', alpha=0.8)
plots[1].add_label(pos_x-5., pos_y-1.2, "3C 61.1", layer='3C61-label', alpha=0.8)

#These lines create the dashed lines to show a zoom in effect.
#Little tricky as the coordinates are in figure coordinates i.e. (0,0) is the bottom left hand cornder of the figure and (1,1) is the top right.
#Look up the matplotlib Line2D for more information
line = matplotlib.lines.Line2D((0.223,0.574),(0.375,0.465),
                               transform=fig.transFigure, color='k', alpha=0.8, ls="--")
line2 = matplotlib.lines.Line2D((0.223,0.574),(0.19,0.1),
                               transform=fig.transFigure, color='k', alpha=0.8, ls="--")

#Add the above defined lines to the figure
fig.lines.append(line)
fig.lines.append(line2)

# plt.show()
plt.savefig('NCP-grid-new.pdf', bbox_inches='tight')