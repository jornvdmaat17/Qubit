import json
from pprint import pprint
from multiQubit import *

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
        for index, val in enumerate(multi["multi"][i]["paulix"]):
            MQ.pauliX(val) 

    if "pauliy" in multi["multi"][i]:   
        for index, val in enumerate(multi["multi"][i]["pauliy"]):
            MQ.pauliY(val) 

    if "pauliz" in multi["multi"][i]:   
        for index, val in enumerate(multi["multi"][i]["pauliz"]):
            MQ.pauliZ(val) 

    if "hadamard" in multi["multi"][i]:   
        for index, val in enumerate(multi["multi"][i]["hadamard"]):
            MQ.hadamard(val) 

    if "sqrtnot" in multi["multi"][i]:   
        for index, val in enumerate(multi["multi"][i]["sqrtnot"]):
            MQ.sqrtNot(val) 
    
    # if "rphi" in multi["multi"][i]:       

else:
    print("JSON not valid")

print(MQ.read())
