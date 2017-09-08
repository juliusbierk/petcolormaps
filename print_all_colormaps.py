import matplotlib.pyplot as plt
import numpy as np
import petcolormaps

cmap_names = [x for x in dir(petcolormaps) if x.count('_')==2]


gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))
def plot_color_gradients(cmap_list, nrows):
    fig, axes = plt.subplots(nrows=nrows, figsize=(8,0.3*nrows))
    fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)

    for ax, name in zip(axes, cmap_list):
        ax.imshow(gradient, aspect='auto', cmap=
        	eval('petcolormaps.%s'%name))
        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.01
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, name, va='center', ha='right', fontsize=10)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()

plot_color_gradients(cmap_names, len(cmap_names))
plt.savefig('all_colormaps.png')
