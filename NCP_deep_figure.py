#!/usr/bin/env python

# a simple script to display a single fits image

import matplotlib.pyplot as plt
import aplpy

#Define the figure
fig = plt.figure(figsize=(12, 12))
#Load the fits file
f1 = aplpy.FITSFigure('NCP_JUNE_DEEP_FINAL.fits', figure=fig)
#In this case the figure is displayed in grayscale, with min and max values (these will be calculated automatically if not specified.)
f1.show_grayscale(vmin=0.005, vmax=6.032e-01)
#Can then recenter the image
f1.recenter(15., 90., 10.)
#Set theme
f1.set_theme('publication')
#Below various different parameters are set such as showing the beam, grid and colorbar
f1.add_beam()
f1.beam.set_frame(True)
f1.beam.set_facecolor('black')
f1.add_grid()
f1.grid.set_color('black')
f1.grid.set_alpha(0.1)
f1.add_colorbar()
#Edit axis and tick points.
f1.axis_labels.set_xtext('Right Ascension (J2000)')
f1.axis_labels.set_ytext('Declination (J2000)')
f1.axis_labels.set_font(size='x-large')
f1.tick_labels.set_yformat('dd')
f1.tick_labels.set_xformat('hh')
f1.tick_labels.set_font(size='large')
f1.ticks.set_xspacing(15)
f1.ticks.set_yspacing(1)
#Finally save
f1.save('new-deep-july2015_2.pdf')