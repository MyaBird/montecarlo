from .bitstring import BitString
from .isinghamiltonian import IsingHamiltonian as ham

def get_lowest_energy_config(self):
        """Class to determine the lowest energy configuration.
        """
        my_bs = BitString(self.N)
        x = [] # Store list of indices
        y = [] # Store list of energies
        xmin = None # configuration of minimum energy configuration
        emin = 0 # minimum of energy
        for i in range(2 ** 10):
            my_bs.set_int_config(i)
            if ham.energy(my_bs, G) < emin:
                emin = ham.energy(my_bs, G)
                xmin = i
            else:
                pass
            x.append(i)
            y.append(ham.energy(my_bs, G))