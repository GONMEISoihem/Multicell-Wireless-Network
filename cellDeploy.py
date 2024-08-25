import numpy as np
from envParameters import EnvPar
from numCell import NumCell
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d


class CellDeployment:
    def __init__(self, num_cell, env):
        self.num_cell = num_cell
        self.env = env

    def cell_deploy(self, i_sim):
        NtWk = {}

        # BS Generation
        NtWk['posR'] = np.zeros((self.num_cell.nBS[0], 1))

        # Main BS positions
        NtWk['posR'][0:self.num_cell.mainBS[0]] = (
                self.num_cell.measureRadius * np.sqrt(np.random.rand(self.num_cell.mainBS[0], 1))
        )

        # Dummy BS positions
        NtWk['posR'][self.num_cell.mainBS[0]:self.num_cell.nBS[0]] = (
            np.sqrt(
                self.num_cell.measureRadius ** 2 +
                np.random.rand(self.num_cell.dummyBS[0], 1) *
                (self.num_cell.dummyRadius ** 2 - self.num_cell.measureRadius ** 2)
            )
        )

        NtWk['posTh'] = 2 * np.pi * np.random.rand(self.num_cell.nBS[0], 1)

        # Convert polar coordinates to Cartesian
        NtWk['posX'] = NtWk['posR'] * np.cos(NtWk['posTh'])
        NtWk['posY'] = NtWk['posR'] * np.sin(NtWk['posTh'])
        NtWk['posBS'] = NtWk['posX'] + NtWk['posY'] * 1j

        # UE Generation
        R = self.num_cell.dummyRadius * np.sqrt(np.random.rand(self.num_cell.nUE[0], 1))
        Th = 2 * np.pi * np.random.rand(self.num_cell.nUE[0], 1)

        X = R * np.cos(Th)
        Y = R * np.sin(Th)
        NtWk['posUE'] = X + 1j * Y

        return NtWk

    def plot(self, NtWk):
        # Extract BS and UE positions
        posX = np.real(NtWk['posBS'])
        posY = np.imag(NtWk['posBS'])
        posUE_X = np.real(NtWk['posUE'])
        posUE_Y = np.imag(NtWk['posUE'])

        plt.figure()

        # Plot BS positions with scatter plot
        plt.scatter(posX, posY, marker='^', color='red', label='Base Stations')

        # Plot UE positions with scatter plot
        plt.scatter(posUE_X, posUE_Y, color='k', marker='.', label='User Equipment')

        # Add labels and title
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.title('BS and UE Positions with Voronoi Tessellation')

        # Display legend
        plt.legend()

        # Show plot
        plt.show()
