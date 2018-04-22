# quantum_phase_meas_y.py
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
meas_y = QuantumCircuit(q, c)
meas_y.barrier()
meas_y.s(q).inverse()
meas_y.h(q)
meas_y.measure(q, c)
exp_vector = range(0,8)
for exp_index in exp_vector:
    circuits.append(pre + middle + meas_y)
    middle.t(q)
    
# Execute the circuits
shots = 1024
compile_config = {
    'shots': shots,
    'seed': 8
}
result = execute(circuits, backend_name = 'local_qasm_simulator', compile_config=compile_config)

# Print the result
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
    print('exp {}: [{}, {}] Y lenght = {}'.format(exp_index, p0, p1, p0-p1))