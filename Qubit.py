import numpy as np
import cmath
from math import sqrt,e
from random import randint

golden = (1 + 5 ** 0.5) / 2
hs2 = 1 / sqrt(2)
offset = 0.000001

identity = np.matrix([[1, 0],[0,1]])
pauliX = np.matrix([[0,1],[1,0]])
pauliY = np.matrix([[0,1j],[1j,0]])
pauliZ = np.matrix([[1,0],[0,-1]])
hadamard = hs2 * np.matrix([[1, 1], [1, -1]])
sqrtNot = (1/2) * np.matrix([[1+1j, 1 - 1j], [1 - 1j, 1+1j]])
rphi = np.matrix([[1,0],[0,e ** (1j *golden)]])

class Qubit:
    def __init__(self, a, b):
        if 1 - offset < abs(a * a) + abs(b * b) < 1 + offset:
            self.__a = a
            self.__b = b
            self.__matrix = np.matrix([[self.__a],[self.__b]])
        else:
           raise impossibleQubitException("Expected A^2 + B^2 = 1, but was " + str(abs(a * a) + abs(b * b)), None) 

    def read(self):
        val = randint(0,100) / 100.0
        if val < abs(self.__a)**2:
            self.__a = 1
            self.__b = 0
            return 0
        else:
            self.__a = 0
            self.__b = 1
            return 1            

    def pauliX(self):
        tmp = pauliX * self.__matrix
        return Qubit(tmp.item(0), tmp.item(1))

    def pauliY(self):
        tmp = pauliY * self.__matrix
        return Qubit(tmp.item(0), tmp.item(1))

    def pauliZ(self):
        tmp = pauliZ * self.__matrix
        return Qubit(tmp.item(0), tmp.item(1))

    def hadamard(self):
        tmp = hadamard * self.__matrix
        return Qubit(tmp.item(0), tmp.item(1))

    def sqrtNot(self):
        tmp = sqrtNot * self.__matrix
        return Qubit(tmp.item(0), tmp.item(1))

    def rphi(self):
        tmp = rphi * self.__matrix
        return Qubit(tmp.item(0), tmp.item(1))

    def __str__(self):
        return str(self.__a) + "|0> + " + str(self.__b) + "|1>"

class impossibleQubitException(Exception):
    def __init__(self, message, errors):
        
        super().__init__(message)
        self.__errors = errors
