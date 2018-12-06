
from multiQubit import *
import sys
sys.path.append('../')

# sys.path.append('../QuantumConstants.py')

mq = multiQubit([Qubit(HS2, HS2), Qubit(HS2,HS2), Qubit(HS2, HS2)])
print(mq.read())
print(mq.read())