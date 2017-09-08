# petcolormaps
200 colormaps for python matplotlib and generator for more.

```python
import petcolornames as pcn
a = np.random.random((25,25))
plt.imshow(a, cmap = pcn.firmly_ideal_crow)
plt.show()
```

All colormaps are increasing in brightness -- although code should be easy to change for diverging colormaps.


![Example colormaps](https://raw.githubusercontent.com/juliusbierk/petcolormaps/master/some_colormaps_random.png)


![All colormaps](https://raw.githubusercontent.com/juliusbierk/petcolormaps/master/all_colormaps.png)
