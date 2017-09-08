import matplotlib.pyplot as plt
import numpy as np
import petcolormaps

cmap_names = ['deadly_moral_corgi', 'deeply_deep_ape', 'firmly_ideal_crow', 'fully_giving_magpie', 'fully_star_boa', 'humbly_rapid_ray', 'jolly_rested_alpaca', 'lovely_divine_duck', 'neatly_picked_sawfly', 'rarely_pumped_molly', 'really_eager_jackal', 'safely_mature_ewe', 'simply_first_roughy', 'wholly_vast_cow']

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))
def plot_color_gradients(cmap_list, nrows):
    fig, axes = plt.subplots(nrows=nrows, figsize=(8,1.0*nrows))
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
plt.savefig('some_colormaps.png')

plt.close()

a = np.random.random((25, 25))
def plot_color_random(cmap_list, nrows):
    fig, axes = plt.subplots(nrows=nrows, figsize=(8,7.0*nrows))
    fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)

    for ax, name in zip(axes, cmap_list):
        ax.imshow(a, aspect='auto', cmap=
            eval('petcolormaps.%s'%name), interpolation='none')
        pos = list(ax.get_position().bounds)
        x_text = pos[0] + 0.6
        y_text = pos[1] + pos[3] + 0.002
        fig.text(x_text, y_text, name, va='center', ha='right', fontsize=25)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()

plot_color_random(cmap_names, len(cmap_names))
plt.savefig('some_colormaps_random.png')