from Qubit import *


# Create a simple Qubit
q1 = Qubit(1, 0)

# Print the Qubit
print("Print example:\nq1: " + str(q1) + "\n") 

# Copy your Qubit
q2 = q1
print("Copy example:\nq2: " + str(q2) + "\n")

# Use pauliX
q3 = q1.pauliX()
print("PauliX example:\nq3: " + str(q3) + "\n") 

# Use pauliY
q4 = q1.pauliY()
print("PauliY example:\nq4: " + str(q4) + "\n")

# Use pauliZ
q5 = q1.pauliZ()
print("PauliZ example:\nq5: " + str(q5) + "\n")

# Use hadamard
q6 = q1.hadamard()
print("Hadamard example:\nq6: " + str(q6) + "\n")

# Use sqrtNot
q7 = q1.sqrtNot()
print("SqrtNot example:\nq7: " + str(q7) + "\n")

# Use rphi
q8 = q1.rphi()
print("Rphi example:\nq8: " + str(q8) + "\n")

# After reading
val = q7.read()
print("after reading q7 gave:\n" + str(val) + "\n")

# After reading you cant do calculations again
q8 = q7.hadamard()
print("q8: " + str(q8) + " is hetzelfde als q7: " + str(q7))


