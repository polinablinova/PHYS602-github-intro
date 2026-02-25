import numpy as np

# this will create an array of 2*10^8 bytes, too large for github
data = np.random.normal(size=(5000,5000)).astype(np.float64)
data[3000:3100] += 5

np.save('data.npy', data)