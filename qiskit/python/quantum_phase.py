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
meas_x = qp.create_circuit('meas_x', [q], [c])
meas_x.barrier()
meas_x.h(q)
meas_x.measure(q, c)
exp_vector = range(0,8)
for exp_index in exp_vector:
    circuit_name = "quantum_phase_%d"%exp_index
    qp.add_circuit(circuit_name, pre + middle + meas_x)
    middle.t(q)
    circuits.append(circuit_name)

# Execute the circuit
result = qp.execute(circuits, backend = 'local_qasm_simulator')

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