import encodermap as em

# generating data:
high_d_data, ids = em.misc.random_on_cube_edges(10000, sigma=0.05)

# setting parameters:
parameters = em.Parameters()
parameters.main_path = em.misc.run_path("/home/tobias/Desktop/test_cuboid")
parameters.n_steps = 10000
parameters.dist_sig_parameters = (0.2, 3, 6, 1, 2, 6)
parameters.periodicity = float("inf")

# training:
autoencoder = em.Autoencoder(parameters, high_d_data)
autoencoder.train()

# projecting:
low_d_projection = autoencoder.encode(high_d_data)
generated = autoencoder.generate(low_d_projection)


#########################################################################
# Plotting:

from mpl_toolkits.mplot3d import Axes3D  # somehow this conflicts with tensorflow if imported earlier
import matplotlib.pyplot as plt

fig = plt.figure()
axe = fig.add_subplot(111, projection='3d')
axe.scatter(high_d_data[:, 0], high_d_data[:, 1], high_d_data[:, 2], c=ids, marker="o", linewidths=0, cmap="tab10")

fig, axe = plt.subplots()
axe.scatter(low_d_projection[:, 0], low_d_projection[:, 1], c=ids, s=5, marker="o", linewidths=0, cmap="tab10")

fig = plt.figure()
axe = fig.add_subplot(111, projection='3d')
axe.scatter(generated[:, 0], generated[:, 1], generated[:, 2], c=ids, marker="o", linewidths=0, cmap="tab10")

plt.show()
