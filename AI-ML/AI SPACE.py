# HTB AI SPACE YS4B

import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import MDS

# Load the distance matrix
file_name = "distance_matrix.npy"
data = np.load(file_name)

# Perform MDS
mds = MDS(n_components=2, dissimilarity="precomputed", random_state=42)
pos = mds.fit_transform(data)

# Plot the results
plt.scatter(pos[:, 0], pos[:, 1], color='blue')
for i, txt in enumerate(range(len(pos))):
    plt.annotate(txt, (pos[i, 0], pos[i, 1]))
plt.grid()
plt.show() #HTB{D0_1t_Your$3lf:)}
