# quantum_phase_u1.py
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.wrapper import execute

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
exp_vector = range(0,50)
exp_phase = []
phase = 0.0
for exp_index in exp_vector:
    phase = phase + 2*np.pi/len(exp_vector)
    exp_phase.append(phase)
    middle.u1(phase,q)
    circuits.append(pre + middle + meas_x)

# Execute the circuit
shots = 1024
compile_config = {
    'shots': shots,
    'seed': 8
}
result = execute(circuits, backend_name = 'local_qasm_simulator', compile_config=compile_config)

# Print result
exp_data = []
for exp_index in exp_vector:
    data = result.get_counts(circuits[exp_index])
    try:
        p0 = data['0']/shots
    except KeyError:
        p0 = 0
    try:
        p1 = data['1']/shots
    except KeyError:
        p1 = 0
    exp_data.append(p0-p1)

import matplotlib.pyplot as plt

plt.plot(exp_phase, exp_data)
plt.show()