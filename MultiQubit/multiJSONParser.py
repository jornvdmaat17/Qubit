import json
from pprint import pprint
from multiQubit import *
from math import pi

with open('multi.json') as f:
    multi = json.load(f)

i = 0
MQ = None

if "qubits"  in multi["multi"][i]:
    multiQ = []
    for index, q in enumerate(multi["multi"][i]["qubits"]):
        if isinstance(multi["multi"][i]["qubits"][index][0], str):
            alphaC = complex(multi["multi"][i]["qubits"][index][0])
        else:
            alphaC = multi["multi"][i]["qubits"][index][0]

        if isinstance(multi["multi"][i]["qubits"][index][1], str):
            betaC = complex(multi["multi"][i]["qubits"][index][1])
        else:
            betaC = multi["multi"][i]["qubits"][index][1]

        multiQ.append(Qubit(alphaC, betaC))
    MQ = multiQubit(multiQ)
    

    if "paulix" in multi["multi"][i]:   
        MQ.pauliX(multi["multi"][i]["paulix"]) 

    if "pauliy" in multi["multi"][i]:   
        MQ.pauliY(multi["multi"][i]["pauliy"]) 

    if "pauliz" in multi["multi"][i]:   
        MQ.pauliZ(multi["multi"][i]["pauliz"]) 

    if "hadamard" in multi["multi"][i]:   
        MQ.hadamard(multi["multi"][i]["hadamard"]) 

    if "sqrtnot" in multi["multi"][i]:   
        MQ.sqrtNot(multi["multi"][i]["sqrtnot"])
    
    if "rphi" in multi["multi"][i]:    
        phi = 1 
        if "phi" in multi["multi"][i]["rphi"]:
            phi = pi / multi["multi"][i]["rphi"]["phi"]
        MQ.rphi(multi["multi"][i]["rphi"]["index"], phi)

else:
    print("JSON not valid")

print(MQ.read())
