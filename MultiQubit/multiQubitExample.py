
from multiQubit import *
import sys
sys.path.append('../')

mq = multiQubit([Qubit(HS2, HS2), Qubit(HS2,HS2), Qubit(HS2, HS2)])
print(mq.read())