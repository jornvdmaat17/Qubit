# MultiQubit

MultiQubit class to do calculations with logical ports on multiple Qubits, as if they were in a computer.<br>
The functions will do exectly the same to a Qubit as in the Qubit class, but now the function ask for indices on which Qubits you want to apply the gates to.<br>
All the logical ports will take an index parameter, this can either be an array of indices or one single number.<br>
For instance: [1,2], [1], 1 are viable inputs.

### read()
Will read the whole MultiQubit system and returns the outcome of the system

### pauliX(index)
Will multiply the given index or indices with the Pauli-X matrix

### pauliY()
Will multiply the given index or indices with the Pauli-Y matrix

### pauliZ()
Will multiply the given index or indices with the Pauli-Z matrix

### hadamard()
Will multiply the given index or indices with the Hadamard matrix

### sqrtNot()
Will multiply the given index or indices with the square root of the NOT gate, NOT gate being the Pauli-X gate

### rphi()
Will multiply the given index or indices with the Phase Shift gate
  
The last six apply certain gates to the the qubit, these gates can be found [here](https://en.wikipedia.org/wiki/Quantum_logic_gate).
