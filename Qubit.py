import numpy as np
import cmath
from math import sqrt,e
from random import randint
import QuantumConstants

offset = 0.000001

class Qubit:
    def __init__(self, a, b):
        self.__read = False
        if 1 - offset < abs(a * a) + abs(b * b) < 1 + offset:
            self.__a = a
            self.__b = b
            self.__matrix = np.matrix([[self.__a],[self.__b]])
        else:
            print(a)
            raise impossibleQubitException("Expected A^2 + B^2 = 1, but was " + str(abs(a * a) + abs(b * b)), None)

    def read(self):
        self.__read = True
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
        if not self.__read:
            tmp = QuantumConstants.PAULIX * self.__matrix
            return Qubit(tmp.item(0), tmp.item(1))
        else:
            return self

    def pauliY(self):
        if not self.__read:
            tmp = QuantumConstants.PAULIY * self.__matrix
            return Qubit(tmp.item(0), tmp.item(1))
        else:
            return self

    def pauliZ(self):
        if not self.__read:
            tmp = QuantumConstants.PAULIZ * self.__matrix
            return Qubit(tmp.item(0), tmp.item(1))
        else:
            return self

    def hadamard(self):
        if not self.__read:
            tmp = QuantumConstants.HADAMARD * self.__matrix
            return Qubit(tmp.item(0), tmp.item(1))
        else:
            return self

    def sqrtNot(self):
        if not self.__read:
            tmp = QuantumConstants.SQRTNOT * self.__matrix
            return Qubit(tmp.item(0), tmp.item(1))
        else:
            return self

    def rphi(self):
        if not self.__read:
            tmp = QuantumConstants.RPHI * self.__matrix
            return Qubit(tmp.item(0), tmp.item(1))
        else:
            return self

    def __str__(self):
        return str(self.__a) + "|0> + " + str(self.__b) + "|1>"

class impossibleQubitException(Exception):
    def __init__(self, message, errors):
        
        super().__init__(message)
        self.__errors = errors
