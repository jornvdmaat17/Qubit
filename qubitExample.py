
'''
This file contains a example of all the calculation you can apply to a Qubit.
Also some basic examples are included for instance how to instansiate a Qubit and assign a Alpha and Beta to this Qubit.
You can print the output of these calculations to the console using the command: "python qubitExample.py".
The examples listed in this file are:

- Creating a Qubit
- Printing a Qubit
- Copying a Qubit
- Using pauliX
- Using pauliY
- Using pauliZ
- Using hadamard
- Using sqrtNot
- Using rphi
- Reading the Qubit
- After reading


The class Qubit and its functions can be found in Qubit.py.
Inside the file QuantumConstants you can find certain the matrices and some math constants which you will also be able to use.
'''

from Qubit import *
from QuantumConstants import HS2
from math import pi


# Create a simple Qubit
q0 = Qubit(1, 0)


# Print the Qubit
print("Print example:\nq0: " + str(q0) + "\n\n") 


# Copy your Qubit
q1 = q0
print("Copy example:\nq1: " + str(q1) + "\n\n")


# Use pauliX
q2 = Qubit(1,0)
q2.pauliX()
print("Pauli-X example:\nq2: " + str(q2) + "\n\n")


# Use pauliY
q3 = Qubit(1,0)
q3.pauliY()
print("Pauli-Y example:\nq3: " + str(q3) + "\n\n")


# Use pauliZ
q4 = Qubit(0, 1)
q4.pauliZ()
print("Pauli-Z example:\nq4: " + str(q4) + "\n\n")


# Use hadamard
q5 = Qubit(1,0)
q5.hadamard()
print("Hadamard example:\nq5: " + str(q5) + "\n\n")


# Use sqrtNot
q6 = Qubit(1,0)
q6.sqrtNot()
print("SqrtNot example:\nq6: " + str(q6) + "\n\n")


# Use rphi
q7 = Qubit(1,0)
q7.rphi(pi/8)
print("Rphi example:\nq7: " + str(q7) + "\n\n")


# After reading
q8 = Qubit(HS2, HS2)
val = q8.read()
print("After reading q8 gave:\nBitvalue:" + str(val) + "\n\n")


# q8 is either 1 or 0 after reading and won't go back to its qubit state
print("q8 now behaves as a normal bit:\nq8:" + str(q8) + "\n\n")


# After reading you won't be able to apply the gates to the qubit again
q8.pauliY()
print("Applied pauliY on q8 again but nothing changed:\n" + str(q8) + "\n\n")
