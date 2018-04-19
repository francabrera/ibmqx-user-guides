import numpy as np

# use QISKit.org
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
exp_vector = range(0,8)
for exp_index in exp_vector:
    circuits.append(pre + middle + meas_x)
    middle.t(q)

# Execute the circuit
result = execute(circuits, backend_name = 'local_qasm_simulator')

# Print result
for exp_index in exp_vector:
    data = result.get_counts(circuits[exp_index])
    try:
        p0 = data['0']/1024.0
    except KeyError:
        p0 = 0
    try:
        p1 = data['1']/1024.0
    except KeyError:
        p1 = 0
    print('exp {}: [{}, {}] Y lenght = {}'.format(exp_index, p0, p1, p0-p1))