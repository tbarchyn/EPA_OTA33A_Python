import numpy as np

file_y = np.load("pgtabley.npz")
pgtabley=file_y['data']

np.savetxt("pgtabley.txt",pgtabley,delimiter=',')

file_z = np.load("pgtablez.npz")
pgtablez=file_z['data']
np.savetxt("pgtablez.txt",pgtablez,delimiter=',')