# quantum_phase_u1.py
import numpy as np
import matplotlib.pyplot as plt
import seaborn

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.wrapper import execute, available_backends, register

import Qconfig
register(Qconfig.APItoken, Qconfig.config['url'])

# Define the Quantum and Classical Registers
q = QuantumRegister(1)
c = ClassicalRegister(1)

# Build the circuit
pre = QuantumCircuit(q, c)
pre.x(q)
pre.barrier()
middle = QuantumCircuit(q, c)
meas = QuantumCircuit(q, c)
meas.measure(q, c)
circuits = []
exp_vector = range(1,51)
for exp_index in exp_vector:
    for i in range(50):
        middle.iden(q)
    circuits.append(pre + middle + meas)


# Execute the circuit
shots = 1024
compile_config = {
    'shots': shots,
    'max_credits': 10
}
result = execute(circuits, 'ibmqx4', compile_config, wait=5, timeout=1800)
print(result)
# Get result
exp_data = []
exp_error = []
for exp_index in exp_vector:
    data = result.get_counts(circuits[exp_index-1])
    try:
        p0 = data['00000']/shots
    except KeyError:
        p0 = 0
    exp_data.append(p0)
    exp_error.append(np.sqrt(p0*(1-p0)/shots))

plt.errorbar(exp_vector, exp_data, exp_error)
plt.xlabel('time [50*gate time]')
plt.ylabel('Pr(0)')
plt.grid(True)
plt.show()