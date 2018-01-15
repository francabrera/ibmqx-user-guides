# use QISKit.org
from qiskit import QuantumProgram
import numpy as np

# Define the QProgram and the Quantum and Classical Registers
qp = QuantumProgram()
q = qp.create_quantum_register('q', 1)
c = qp.create_classical_register('c', 1)

# Build the circuit
circuits = []
pre = qp.create_circuit('pre', [q], [c])
pre.h(q)
pre.barrier()
middle = qp.create_circuit('middle', [q], [c])
meas_y = qp.create_circuit('meas_y', [q], [c])
meas_y.barrier()
meas_y.s(q).inverse()
meas_y.h(q)
meas_y.measure(q, c)
exp_vector = range(0,8)
for exp_index in exp_vector:
    circuit_name = "quantum_phase_%d"%exp_index
    qp.add_circuit(circuit_name, pre + middle + meas_y)
    middle.t(q)
    circuits.append(circuit_name)

# Execute the circuit, to run on the real device change 
# backend = 'local_qasm_simulator' to backend = 'ibmqx...' and set the API.
# Also to explore the quantum randomness remove seed = 1
result = qp.execute(circuits, backend = 'local_qasm_simulator',seed=1)

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
    print('exp {}: [{}, {}] X lenght = {}'.format(exp_index, p0, p1, p0-p1))