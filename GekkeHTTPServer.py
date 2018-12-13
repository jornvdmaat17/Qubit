from flask import Flask,request
from math import sqrt,e
import numpy as np

# Math constants
GOLDEN = (1 + 5 ** 0.5) / 2 #This value is about: 1.618033988749895
HS2 = 1 / sqrt(2)   #This value is about: 0.7071067811865475

# Matrices to be used with quantum calculations
IDENTITY = np.matrix([[1, 0],[0,1]])
PAULIX = np.matrix([[0,1],[1,0]])
PAULIY = np.matrix([[0,1j],[1j,0]])
PAULIZ = np.matrix([[1,0],[0,-1]])
HADAMARD = HS2 * np.matrix([[1, 1], [1, -1]])
SQRTNOT = (1/2) * np.matrix([[1+1j, 1 - 1j], [1 - 1j, 1+1j]])
# RPHI = np.matrix([[1,0],[0,e ** (1j * GOLDEN)]])
OFFSET = 0.000001

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to my Flask page!"

@app.route("/get/pauliX/<Alpha>:<Beta>", methods=['GET'])
def get_pauliX(Alpha,Beta):
    if 1 - OFFSET < abs(Alpha * Alpha) + abs(Beta * Beta) < 1 + OFFSET:
        tmp = PAULIX * np.matrix([[complex(Alpha)],[complex(Beta)]])
        a = tmp.item(0)
        b = tmp.item(1)

        return str(a) + ":" + str(b)
    else: return "impossibleQubitException: Expected A^2 + B^2 = 1, but was " + str(abs(a * a) + abs(b * b))

@app.route("/get/pauliY/<Alpha>:<Beta>", methods=['GET'])
def get_pauliY(Alpha,Beta):
    if 1 - OFFSET < abs(Alpha * Alpha) + abs(Beta * Beta) < 1 + OFFSET:
        tmp = PAULIY * np.matrix([[complex(Alpha)],[complex(Beta)]])
        a = tmp.item(0)
        b = tmp.item(1)

        return str(a) + ":" + str(b)
    else: return "impossibleQubitException: Expected A^2 + B^2 = 1, but was " + str(abs(a * a) + abs(b * b))

@app.route("/get/pauliZ/<Alpha>:<Beta>", methods=['GET'])
def get_pauliZ(Alpha,Beta):
    if 1 - OFFSET < abs(Alpha * Alpha) + abs(Beta * Beta) < 1 + OFFSET:
        tmp = PAULIZ * np.matrix([[complex(Alpha)],[complex(Beta)]])
        a = tmp.item(0)
        b = tmp.item(1)

        return str(a) + ":" + str(b)
    else: return "impossibleQubitException: Expected A^2 + B^2 = 1, but was " + str(abs(a * a) + abs(b * b))

@app.route("/get/hadamard/<Alpha>:<Beta>", methods=['GET'])
def get_hadamard(Alpha,Beta):
    if 1 - OFFSET < abs(Alpha * Alpha) + abs(Beta * Beta) < 1 + OFFSET:
        tmp = HADAMARD * np.matrix([[complex(Alpha)],[complex(Beta)]])
        a = tmp.item(0)
        b = tmp.item(1)

        return str(a) + ":" + str(b)
    else: return "impossibleQubitException: Expected A^2 + B^2 = 1, but was " + str(abs(a * a) + abs(b * b))

@app.route("/get/sqrtNOT/<Alpha>:<Beta>", methods=['GET'])
def get_sqrtNOT(Alpha,Beta):
    if 1 - OFFSET < abs(Alpha * Alpha) + abs(Beta * Beta) < 1 + OFFSET:
        tmp = SQRTNOT * np.matrix([[complex(Alpha)],[complex(Beta)]])
        a = tmp.item(0)
        b = tmp.item(1)

        return str(a) + ":" + str(b)
    else: return "impossibleQubitException: Expected A^2 + B^2 = 1, but was " + str(abs(a * a) + abs(b * b))

@app.route("/get/rphi/<Alpha>:<Beta>:<phi>", methods=['GET'])
def get_rphi(Alpha,Beta,phi):
    if 1 - OFFSET < abs(Alpha * Alpha) + abs(Beta * Beta) < 1 + OFFSET:
        tmp = np.matrix([[1,0],[0,e ** (1j * phi)]]) * np.matrix([[complex(Alpha)],[complex(Beta)]])
        a = tmp.item(0)
        b = tmp.item(1)

        return str(a) + ":" + str(b)
    else: return "impossibleQubitException: Expected A^2 + B^2 = 1, but was " + str(abs(a * a) + abs(b * b))

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=7234)


