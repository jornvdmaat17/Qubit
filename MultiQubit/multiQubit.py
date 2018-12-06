import sys
sys.path.append('../')
from Qubit import *
from QuantumConstants import *

class multiQubit:

    def __init__(self, qubits):
        self.__qubits = qubits

    def pauliX(self, index):
        if isinstance(index, list):
            for i in index:
                if i < len(self.__qubits):
                    self.__qubits[i].pauliX()
        else:
            self.__qubits[index].pauliX()

    def pauliY(self, index):
        if isinstance(index, list):
            for i in index:
                if i < len(self.__qubits):
                    self.__qubits[i].pauliY()
        else:
            self.__qubits[index].pauliY()

    def pauliZ(self, index):
        if isinstance(index, list):
            for i in index:
                if i < len(self.__qubits):
                    self.__qubits[i].pauliZ()
        else:
            self.__qubits[index].pauliZ()

    def hadamard(self, index):
        if isinstance(index, list):
            for i in index:
                if i < len(self.__qubits):
                    self.__qubits[i].hadamard()
        else:
            self.__qubits[index].hadamard()

    def sqrtNot(self, index):
        if isinstance(index, list):
            for i in index:
                if i < len(self.__qubits):
                    self.__qubits[i].sqrtNot()
        else:
            self.__qubits[index].sqrtNot()

    def rphi(self, index, phi):
        if isinstance(index, list):
            for i in index:
                if i < len(self.__qubits):
                    self.__qubits[i].rphi(phi)
        else:
            self.__qubits[index].rphi(phi)

    def read(self):
        val =""
        for q in self.__qubits:
            val += str(q.read())
        return val

    def __str__(self):
        ret = "["
        for q in self.__qubits:
            ret += "\n" + str(q)
        ret += "\n]" 
        return ret

