from math import sqrt,e
import numpy as np

# Math constants
GOLDEN = (1 + 5 ** 0.5) / 2
HS2 = 1 / sqrt(2)

# Matrices to be used with quantum calculations
IDENTITY = np.matrix([[1, 0],[0,1]])
PAULIX = np.matrix([[0,1],[1,0]])
PAULIY = np.matrix([[0,1j],[1j,0]])
PAULIZ = np.matrix([[1,0],[0,-1]])
HADAMARD = HS2 * np.matrix([[1, 1], [1, -1]])
SQRTNOT = (1/2) * np.matrix([[1+1j, 1 - 1j], [1 - 1j, 1+1j]])
RPHI = np.matrix([[1,0],[0,e ** (1j * GOLDEN)]])