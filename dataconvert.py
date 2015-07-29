import numpy as np
import re

file_y = np.load("ota33a/pgtabley.npz")
pgtabley=file_y['data']

np.savetxt("pgtabley.txt",pgtabley,delimiter=',')

file_z = np.load("ota33a/pgtablez.npz")
pgtablez=file_z['data']
np.savetxt("pgtablez.txt",pgtablez,delimiter=',')

file_data = np.load("exampleData.npz")
for key, value in file_data.items():
    if np.shape(np.atleast_1d(value)) != (1,):
        np.savetxt("exampleData_"+key+".txt",value,fmt="%s")
    else:
        with open("exampleData_"+key+".txt", 'w') as file_:
            file_.write(str(value))