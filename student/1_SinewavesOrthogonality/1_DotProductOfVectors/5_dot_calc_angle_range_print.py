import numpy as np
from lib import rotate_vector

vector = [0,1]

for i in range (0,361,10):
    rot_vector = rotate_vector(vector,i)
    
    print(f'{i:03d}: {(np.dot(vector,rot_vector)):+0.3f}')
