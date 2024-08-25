import numpy as np


class EnvPar:
    def __init__(self):
        ### Simulation Parameters
        self.nSim = 1

        ### Density Parameters (per square meter)
        self.densityBS = 1e-4  # Base Station density
        self.densityUE = 1e-4  # User Equipment density

        ### Path Loss Parameters
        self.pathlossExp = [2, 4]  # Path loss exponents for different environments
        self.nakagamiFading = [3, 2]  # Nakagami fading parameters

        ### Antenna Parameters (in radians)
        self.beamwidthBS = 10 / 180 * np.pi  # BS beamwidth in radians
        self.beamwidthUE = 360 / 180 * np.pi  # UE beamwidth in radians
        self.maingainBS = 18  # Main lobe gain of BS antenna (dBi)
        self.sidegainBS = -2  # Side lobe gain of BS antenna (dBi)
        self.maingainUE = 0  # Main lobe gain of UE antenna (dBi)
        self.sidegainUE = 0  # Side lobe gain of UE antenna (dBi)

        ### Frequency and Bandwidth
        self.carierFreq = 28e9  # Carrier frequency in Hz
        self.bandwidth = 100e6  # Bandwidth in Hz

        ### Path Loss and Range
        self.rangeLoS = 141.4  # Line-of-Sight range in meters
        self.pathlossIntercept = (3e8 / (4 * np.pi * self.carierFreq)) ** 2  # Path loss intercept

        ### Power and Noise
        self.p = 15  # Transmit power in dBm
        self.thermalNoise_dBm = -174 + 10 * np.log10(self.bandwidth) + 10  # Thermal noise in dBm
        self.thermalNoise = 10 ** (self.thermalNoise_dBm / 10)  # Thermal noise in linear scale

        # Optional: validate the parameters to ensure they are within reasonable ranges
        self._validate_parameters()

    def _validate_parameters(self):
        assert self.densityBS > 0, "Base station density must be positive"
        assert self.densityUE > 0, "User equipment density must be positive"
        assert self.carierFreq > 0, "Carrier frequency must be positive"
        assert self.bandwidth > 0, "Bandwidth must be positive"
        assert self.p > 0, "Transmit power must be positive"
        # Add any other necessary validations

