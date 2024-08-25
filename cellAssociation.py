import numpy as np
from numCell import NumCell
from cellDeploy import CellDeployment


class CellAssociation:
    def __init__(self, num_cell):
        self.num_cell = num_cell

    def calculate_distances(self, NtWk):
        # Calculate the distance between each UE and every BS
        posUE = NtWk['posUE']
        posBS = NtWk['posBS']

        # Replicate posUE for each BS (using np.kron)
        ue_repeated = np.kron(posUE, np.ones((1, self.num_cell.nBS[0])))

        # Replicate posBS for each UE (using np.kron)
        bs_repeated = np.kron(posBS.T, np.ones((self.num_cell.nUE[0], 1)))

        # Calculate the distances
        NtWk['distance'] = np.abs(ue_repeated - bs_repeated)

        return NtWk
