# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 17:44:00 2024

@author: sonus
"""

from qiskit import *
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector

n = input("Enter the Binary Digits More than 1 bit : ") 
n1 = len(n)

qc = QuantumCircuit(n1)

for i in range(n1):
    if n[i] == '1':
        qc.x(i)
qc.draw(output='mpl')

n2 = n1 - 1
i = 1
for i in range(n1-1):
    qc.cx(n2 -i -1, n2)
    
qc.draw(output='mpl')

#Running Simulation
qc.save_statevector()
sim = Aer.get_backend('aer_simulator')
res = sim.run(qc, shots = 2024).result()

#final state vectors
final_state = res.get_statevector(qc)
print("final state vector : ",final_state)

#plot the probability
ans1 = res.get_counts()
plot_histogram(ans1)