# quantum_phase_u1.py
import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.wrapper import execute, register

import Qconfig
register(Qconfig.APItoken, Qconfig.config['url'])

# Define the Quantum and Classical Registers
q = QuantumRegister(1)
c = ClassicalRegister(1)

# Build the circuit
circuits = []
pre = QuantumCircuit(q, c)
pre.h(q)
pre.barrier()
middle = QuantumCircuit(q, c)
meas_x = QuantumCircuit(q, c)
meas_x.barrier()
meas_x.h(q)
meas_x.measure(q, c)
exp_vector = range(1,51)
phase = 0.0
for exp_index in exp_vector:
    delta_phase = 6*np.pi/len(exp_vector)
    phase = phase + delta_phase
    middle.u1(delta_phase,q)
    middle.iden(q)
    circuits.append(pre + middle + meas_x)


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
plt.xlabel('time [gate time]')
plt.ylabel('Pr(+)')
plt.grid(True)
plt.show()