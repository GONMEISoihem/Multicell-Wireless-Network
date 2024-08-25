import numpy as np
from envParameters import EnvPar

ev = EnvPar()


class NumCell:
    def __init__(self):
        self.initialize_parameters()
        self.calculate_base_stations()
        self.calculate_users()

    def initialize_parameters(self):
        self.measureRadius = 447.2136
        self.dummyRadius = 2 * self.measureRadius
        self.average_mainBS = ev.densityBS * np.pi * self.measureRadius**2
        self.average_dummyBS = (ev.densityBS * np.pi *
                                (self.dummyRadius - self.measureRadius)**2)
        self.average_UE = ev.densityUE * np.pi * self.measureRadius**2

    def calculate_base_stations(self):
        self.mainBS = np.random.poisson(self.average_mainBS, 1)
        self.dummyBS = np.random.poisson(self.average_dummyBS, 1)
        self.nBS = self.mainBS + self.dummyBS

    def calculate_users(self):
        self.nUE = np.random.poisson(self.average_UE, 1)





