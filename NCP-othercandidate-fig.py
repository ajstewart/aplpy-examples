#!/usr/bin/env python

#An example of creating an inset zoom in effect with aplpy

import aplpy
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def standard_options(fplot):
    #Standard options function to apply to plots like other examples
    fplot.set_theme('publication')
    fplot.add_beam()
    fplot.beam.set_frame(True)
    fplot.beam.set_facecolor('black')
    fplot.add_grid()
    fplot.grid.set_color('black')
    fplot.grid.set_alpha(0.1)
    fplot.axis_labels.set_xtext('Right Ascension (J2000)')
    fplot.axis_labels.set_ytext('Declination (J2000)')
    fplot.axis_labels.set_font(size='x-large')
    fplot.tick_labels.set_yformat('dd')
    fplot.tick_labels.set_xformat('hh')
    fplot.tick_labels.set_font(size='large')
    fplot.ticks.set_xspacing(15)
    fplot.ticks.set_yspacing(1)

def plotinitial(figure, images, ranges):
    #This function basically puts the first image as the main image and the second image as the inset.
    #Returns a dictionary containing the plots
    #Key is n+1 as in matplotlib the first plot is called by '1' not '0'.
    #Can also change colorscale here for the plots.
    panels={}
    for n in range(0, len(images)):
        key=n+1
        if key==2:
            #edit the below subplot value to move subplot around
            panels[key]=aplpy.FITSFigure(images[n], figure=fig, subplot=[0.45,0.18,0.4,0.4])
        else:
            panels[key]=aplpy.FITSFigure(images[n], figure=fig)
        panels[key].show_grayscale(vmin=ranges[n][0], vmax=ranges[n][1])
    return panels
    
def create_marker(x, y, l1, l2, img):
    #This function creates the crosshair.
    #Arguments x, y are the center in pixel values
    #l1 and l2 are the distance from center start of line and distance from center end of line respectively
    lines=[]
    line1=list(img.pixel2world(x+l1, y))+list(img.pixel2world(x+l2, y))
    lines.append(np.array([[line1[0], line1[2]],[line1[1], line1[3]]]))
    line1=list(img.pixel2world(x-l1, y))+list(img.pixel2world(x-l2, y))
    lines.append(np.array([[line1[0], line1[2]],[line1[1], line1[3]]]))
    line1=list(img.pixel2world(x, y+l1))+list(img.pixel2world(x, y+l2))
    lines.append(np.array([[line1[0], line1[2]],[line1[1], line1[3]]]))
    line1=list(img.pixel2world(x, y-l1))+list(img.pixel2world(x, y-l2))
    lines.append(np.array([[line1[0], line1[2]],[line1[1], line1[3]]]))
    return lines
    
#List of images and then list of vmin and vmax values for each image.
images=['L46442_SAP003_SB240_uv.MS.NEW_Feb13_1CHNL.dppp.dppp.prepeel.2500clip.8k.img.fits','L46442_SAP003_SB240_uv.MS.NEW_Feb13_1CHNL.dppp.dppp.prepeel.2500clip.8k.img.fits']
ranges=[[1.0,9.], [1.0,9.]]

#Define figure
fig = plt.figure(figsize=(10, 10))
#create plots
plots=plotinitial(fig, images, ranges)
#Here I get the world coordinates of where I want the zoom in box to be centered, using the pixel values.
pos_x, pos_y=plots[1].pixel2world(1033, 1295)

#run plots through the standard options
for p in plots:
    standard_options(plots[p]) 

#Some individual additions to plots
plots[1].add_colorbar()
plots[1].recenter(19.*15., 88., 6.)
#Here I use the coordinates obtained above to recenter the inset and then create a box on the first plot
plots[2].recenter(pos_x, pos_y, 0.9)
plots[1].show_rectangles([pos_x,], [pos_y,], height=1.8, width=1.8, layer='rectangle', alpha=0.8)
#More specific plot changes
plots[2].axis_labels.hide()
plots[2].tick_labels.set_font(size='medium', weight='bold')
#create the crosshair and add the lines to the inset plot
linestoplot=create_marker(1033, 1295, 10, 20, plots[2])
plots[2].show_lines(linestoplot, layer='lines', color='black', linewidth=3., alpha=0.5)
#if at this point the plot is previewed, you can make note of the pixel coordinates on the first plot to where the zoom in lines have to start and end.
#e.g. in this case the first corner of the inset box was at (951, 1213) and needed to be drawn to (1125, 591) which was the corner of the subplot.
zoomcoords1=plots[1].pixel2world(951,1213)+plots[1].pixel2world(1125, 591)
zoomcoords2=plots[1].pixel2world(1113,1375)+plots[1].pixel2world(1706, 1137)
zoomline1=np.array([[zoomcoords1[0],zoomcoords1[2]], [zoomcoords1[1],zoomcoords1[3]]])
zoomline2=np.array([[zoomcoords2[0],zoomcoords2[2]], [zoomcoords2[1],zoomcoords2[3]]])
#Show the lines and save figure.
plots[1].show_lines([zoomline1, zoomline2], layer='zoomlines', color='black', linestyle='--', alpha=0.8)
plt.savefig('NCP-candidate2-fig.pdf', bbox_inches='tight')