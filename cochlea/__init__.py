from __future__ import division, print_function, absolute_import

__author__ = "Marek Rudnicki"


import warnings
import numpy as np

from cochlea.zilany2009 import run_zilany2009
from cochlea.holmberg2007 import run_holmberg2007
from cochlea.zilany2014 import run_zilany2014
from cochlea.zilany2014 import run_zilany2014_rate


from cochlea.holmberg2007 import real_freq_map as freq_map_holmberg2007
from cochlea.holmberg2007 import get_nearest_cf as get_nearest_cf_holmberg2007


__version__ = "0.10"


def set_dbspl(signal, dbspl):
    """Rescale the signal to a new level in dB SPL.

    Parameters
    ----------
    signal : array_like
        Signal for scaling.
    dbspl : float
        Desired level of the output signal in dB SPL.

    Returns
    -------
    array_like
        Scaled version of the original signal.

    """
    p0 = 20e-6
    rms = np.sqrt( np.sum(signal**2) / signal.size )

    scalled = signal * 10**(dbspl/20) * p0 / rms

    return scalled


def set_dba_isolet(signal, dba):
    p0 = 20e-6
    rms_dba = 0.02972401089     # value from miclib (precalculated for
                                # all ISOLET files)

    scaled = signal * 10**(dba/20) * p0 / rms_dba

    return scaled
