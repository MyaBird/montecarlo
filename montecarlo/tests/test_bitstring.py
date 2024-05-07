"""
Unit and regression test for the bitstring module.
"""
import montecarlo
import numpy as np
import pytest

def test_bitstring():
    my_bs = montecarlo.BitString(20)
    my_bs.set_int_config(3221)
    tmp = np.array([0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,1])

    assert((my_bs.config == tmp).all())

    for i in range(1000):
        my_bs.set_int_config(i) # Converts from integer to binary
        assert(my_bs.int() == i) # Converts back from binary to integer and tests