import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from uuid import uuid1
from scipy.optimize import minimize
import petname
import json

N = 50
bw = np.linspace(0, 3, N)

def perceptify_colormap(base):
	cmap_before = LinearSegmentedColormap.from_list(uuid1(), base)

	def f(x):
		if np.any(x < 0) or np.any(x > 1):
			return 1e5
		mag = x[:N] + x[N:(2*N)] + x[(2*N):]
		return np.sum((mag - bw)**2)

	base = base[:,:3]
	base = np.hstack((base[:,0], base[:,1], base[:,2]))

	res = minimize(f, base)
	out = res.x
	out = np.vstack((out[:N], out[N:(2*N)], out[(2*N):])).T

	return out, res.fun


def create_colormap(cols, name=uuid1()):
	cols = map(np.array, cols)
	cols = sorted(cols, key=lambda x: np.sum(x))

	base = LinearSegmentedColormap.from_list(uuid1(), cols)
	base = np.array([base(i) for i in np.linspace(0,1.0,N)])
	
	cols, val = perceptify_colormap(base)
	return cols, val

def create_nice_colormap(n_cols=2, iter=100):
	best_val = float('infinity')
	for i in range(iter):
		cols = [np.random.random(3) for j in range(n_cols)]
		cols, val = create_colormap(cols)
		if val < best_val:
			best_val = val
			best_cols = cols
	return best_cols

if __name__ == '__main__':
	try:
		import os
		os.mkdir('maps')
	except:
		pass

	s = np.linspace(-2,2,100)
	x, y = np.meshgrid(s, s)
	a = np.sin(x)*np.cos(y)
	b = np.random.random((25,25))

	plt.figure(figsize=(12,5))

	s = 'from matplotlib.colors import LinearSegmentedColormap\n\n'
	for n_cols in [3,4]:
		for _ in range(100):
			cols = create_nice_colormap(n_cols=n_cols, iter=20)
			name = petname.Generate(3)
			name = name.replace('-', '_')
			cmap = LinearSegmentedColormap.from_list(name, cols)

			s += 'cols = %s'%json.dumps(map(list, list(cols)))
			s += '\n%s = LinearSegmentedColormap.from_list("%s", cols)\n\n'%(name, name)

			plt.clf()
			plt.subplot(1,2,1)
			plt.title(name)
			plt.imshow(a, cmap=cmap, interpolation='none')
			plt.subplot(1,2,2)
			plt.imshow(b, cmap=cmap, interpolation='none', 
					vmin=0, vmax=1)
			plt.title(name)
			plt.colorbar()
			plt.savefig('maps/%s.png'%name)

			print name

			with open('petcolormaps.py', 'w') as f:
				f.write(s)
