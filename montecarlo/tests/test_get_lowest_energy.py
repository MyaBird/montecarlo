"""
Unit and regression test for the get_lowest_energy module.
"""

import montecarlo
import numpy as np
import pytest

def test_getlowestenergy():

    def build_1d_Hamiltonian(N, Jval, mu=0.0):
        """
        Build a 1D Hamiltonian with a single J value (Jval)
        """
        mus = [0.0 for i in range(N)]
        J = [[] for i in range(N)]
        for site in range(N-1):
            J[site].append((site+1, Jval))
        return montecarlo.IsingHamiltonian(J,mus)
     
    ham = build_1d_Hamiltonian(N=3, Jval=1)
    # let's add a local mu value to the first spin
    ham.mu[0] = 1.2 

    n_steps = 3
    beta = []
    gamma = []

    for i in range(n_steps+1):
        beta.append(1-i/n_steps)
        gamma.append(i/n_steps)

    emin, cmin = ham.get_lowest_energy_config()

    cmin_list = []
    for i in str(cmin):
        cmin_list.append(i)

    assert pytest.approx(emin) == -3.2
    assert cmin_list == ['[','1',' ','0',' ','1',']']