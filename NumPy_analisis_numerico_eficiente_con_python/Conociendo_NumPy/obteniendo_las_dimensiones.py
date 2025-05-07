url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/bytebank.csv'
import numpy as np
dato = np.loadtxt(url, delimiter=',', skiprows=1, dtype=float)
np.shape(dato)
print(np.shape(dato))

url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/bytebank.csv'
import numpy as np
dato = np.loadtxt(url, delimiter=',', skiprows=1, dtype=float)
dato.shape
print(dato.shape)

