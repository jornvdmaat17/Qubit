import numpy as np
import cmath
from math import sqrt,e
from random import randint
import QuantumConstants

OFFSET = 0.000001

class Qubit:

    def __init__(self, a, b):
        self.__read = False
        if 1 - OFFSET < abs(a * a) + abs(b * b) < 1 + OFFSET:
            self.__a = a
            self.__b = b
            self.__matrix = np.matrix([[self.__a],[self.__b]])
        else:
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
            self.__a = tmp.item(0)
            self.__b = tmp.item(1)

    def pauliY(self):
        if not self.__read:
            tmp = QuantumConstants.PAULIY * self.__matrix
            self.__a = tmp.item(0)
            self.__b = tmp.item(1)

    def pauliZ(self):
        if not self.__read:
            tmp = QuantumConstants.PAULIZ * self.__matrix
            self.__a = tmp.item(0)
            self.__b = tmp.item(1)

    def hadamard(self):
        if not self.__read:
            tmp = QuantumConstants.HADAMARD * self.__matrix
            self.__a = tmp.item(0)
            self.__b = tmp.item(1)

    def sqrtNot(self):
        if not self.__read:
            tmp = QuantumConstants.SQRTNOT * self.__matrix
            self.__a = tmp.item(0)
            self.__b = tmp.item(1)

    def rphi(self, phi):
        if not self.__read:
            tmp =  np.matrix([[1,0],[0,e ** (1j * phi)]]) * self.__matrix
            self.__a = tmp.item(0)
            self.__b = tmp.item(1)

    def __str__(self):
        return str(self.__a) + "|0> + " + str(self.__b) + "|1>"


class impossibleQubitException(Exception):
    def __init__(self, message, errors):
        
        super().__init__(message)
        self.__errors = errors


def getRandomQubit(negPossible, irPossinble):
    randAlpha = randint(0, 100) / 100
    randBeta = 1.0 - randAlpha
    randAlpha = sqrt(randAlpha)
    randBeta = sqrt(randBeta)
    if randint(0,1) == 1 and negPossible:
        randAlpha *= -1
    if randint(0,1) == 1 and negPossible:
        randBeta *= -1
    if randint(0,1) == 1 and irPossinble:
        randAlpha *= 1j
    if randint(0,1) and irPossinble:
        randBeta *= 1j    
    return Qubit(randAlpha, randBeta)