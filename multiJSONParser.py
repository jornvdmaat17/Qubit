import json
from math import pi

import sys
sys.path.append('lib/')
from multiQubit import *
from QuantumConstants import HS2

with open('multi.json') as f:
    multi = json.load(f)

i = 0
MQ = None
while i < len(multi["multi"]):
    pr = False
    if "qubits" in multi["multi"][i]:
        multiQ = []
        for index, q in enumerate(multi["multi"][i]["qubits"]):
            if len(multi["multi"][i]["qubits"][index]) != 0:
                if isinstance(multi["multi"][i]["qubits"][index][0], str):
                    if multi["multi"][i]["qubits"][index][0] == "HS2":
                        alphaC = HS2
                    else:
                        alphaC = complex(multi["multi"][i]["qubits"][index][0])
                else:
                    alphaC = multi["multi"][i]["qubits"][index][0]

                if isinstance(multi["multi"][i]["qubits"][index][1], str):
                    if multi["multi"][i]["qubits"][index][0] == "HS2":
                        betaC = HS2
                    else:
                        betaC = complex(multi["multi"][i]["qubits"][index][1])
                else:
                    betaC = multi["multi"][i]["qubits"][index][1]   
                multiQ.append(Qubit(alphaC, betaC))
            else:
                multiQ.append(getRandomQubit(True, True))
        MQ = multiQubit(multiQ)
        
        if "print" in multi["multi"][i]:
            if multi["multi"][i]["print"] == "true":
                pr = True

        if pr:
            print("Your start matrix looks like this:\n\n" + str(MQ) + "\n\n")

        if "paulix" in multi["multi"][i]:   
            MQ.pauliX(multi["multi"][i]["paulix"]) 
            if pr:
                print("After pauli-X your matrix looks like this:\n\n" + str(MQ) + "\n\n")

        if "pauliy" in multi["multi"][i]:   
            MQ.pauliY(multi["multi"][i]["pauliy"])
            if pr:
                print("After pauli-Y your matrix looks like this:\n\n" + str(MQ) + "\n\n")

        if "pauliz" in multi["multi"][i]:   
            MQ.pauliZ(multi["multi"][i]["pauliz"]) 
            if pr:
                print("After pauli-Z your matrix looks like this:\n\n" + str(MQ) + "\n\n")

        if "hadamard" in multi["multi"][i]:   
            MQ.hadamard(multi["multi"][i]["hadamard"]) 
            if pr:
                print("After hadamard your matrix looks like this:\n\n" + str(MQ) + "\n\n")

        if "sqrtnot" in multi["multi"][i]:   
            MQ.sqrtNot(multi["multi"][i]["sqrtnot"])
            if pr:
                print("After sqrtNot your matrix looks like this:\n\n" + str(MQ) + "\n\n")
        
        if "rphi" in multi["multi"][i]:    
            phi = 1 
            if "phi" in multi["multi"][i]["rphi"]:
                phi = pi / multi["multi"][i]["rphi"]["phi"]
            MQ.rphi(multi["multi"][i]["rphi"]["index"], phi)
            if pr:
                print("After rphi your matrix looks like this:\n\n" + str(MQ) + "\n\n")

    else:
        print("JSON not valid")

    print("The outcome of multiQubit " + str(i) + " is: " + str(MQ.read()) + "\n\n")
    if pr:
        print("After reading your matrix looks like this:\n\n" + str(MQ) + "\n\n")
    i+=1