#!/usr/bin/env python3
#Author: lnotspotl https://github.com/lnotspotl/a1_sim_py
#Modified by: Lyle

import numpy as np
from math import sin, cos

def rot_x(alpha):
    """
    Creates a 3x3 rotation matrix around the x axis

    Parameters
    ----------
    alpha : double
        The rotation angle around the x axis in radians

    returns
    -------
    rx : numpy array, double
        A 3x3 matrix 
    """
    rx = np.array([[1, 0,          0,         ],
                   [0, cos(alpha), -sin(alpha)],
                   [0, sin(alpha), cos(alpha) ]])

    return rx    