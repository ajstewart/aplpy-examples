APLpy examples
============

The scripts in this repository show various examples of using the python module aplpy to produce the type of figures I used in my NCP transient paper.

The APLpy website (https://aplpy.github.io) has great documentation to help with various commands.

Below describes what type of figure each script produces:

* **NCP_deep_figure.py** - An example of a standard, single fits image figure at a publication quality level.
* **NCP_PB_figure.py** - Like above but this time a primary beam image.
* **NCP-othercandidate-fig.py** - Shows an example of producing a figure with a zoom-in inset.
* **NCP_grid_figure.py** - An example of a figure with multiple subplots (in this case 4).

Python packages used: numpy, scipy, matplotlib, astropy, aplpy. Recommend using virtualev.

**Remember** for MNRAS, Type 3 fonts are not allowed in PDF figures. Follow the advice given here: http://phyletica.org/matplotlib-fonts/ to avoid any PDF issues when submitting.