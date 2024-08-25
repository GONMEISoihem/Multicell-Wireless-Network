import numpy as np
from envParameters import EnvPar
from numCell import NumCell
from cellDeploy import CellDeployment
from cellAssociation import CellAssociation

total_sinr = []

Ev = EnvPar()
# positionBS = CellDeployment(number_cell)
# # Deploy cells for simulation index 0
# positionBS.cell_deploy(0)

for i in range(Ev.nSim):
    print(f"Running {i + 1}th simulation")
    number_cell = NumCell()
    deployment = CellDeployment(number_cell, Ev)  # Create the deployment object
    NtWk = deployment.cell_deploy(i)  # Deploy cells for simulation index i
    deployment.plot(NtWk)  # plotting the positions
    association = CellAssociation(number_cell)  # Create the association object
    # Calculate distances between each UE and every BS
    NtWk = association.calculate_distances(NtWk)

    print(f"Number of Main BSs is: {number_cell.mainBS}")
    print(f"Number of dummy BSs is: {number_cell.dummyBS}")
    print(f"Number of BSs is: {number_cell.nBS}")
    print(f"Number of UEs is: {number_cell.nUE}")
    print(f"Base Station positions (Cartesian): {NtWk['posBS']}")
    print(f"User Equipment positions (Cartesian): {NtWk['posUE']}")
    print(f"Distances between UEs and BSs: {NtWk['distance']}")
    # print(positionBS.NtWk['posBS'])

# average_mainBS = Ev.densityBS*np.pi*447.2136**2
# mainBS = np.random.poisson(average_mainBS, 1)
# print(mainBS)
# if __name__ == "__main__":
#     main()

