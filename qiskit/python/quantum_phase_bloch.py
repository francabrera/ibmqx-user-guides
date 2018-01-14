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

meas_y = qp.create_circuit('meas_y', [q], [c])
meas_y.barrier()
meas_y.s(q).inverse()
meas_y.h(q)
meas_y.measure(q, c)

meas_z = qp.create_circuit('meas_z', [q], [c])
meas_z.barrier()
meas_z.measure(q, c)

bloch_vector = ['x', 'y', 'z']
exp_vector = range(0, 20)
for exp_index in exp_vector:
    phase = 2*np.pi*exp_index/len(exp_vector)
    middle.u1(phase, q)

    circuit_name = "quantum_phase_%d"%exp_index + bloch_vector[0]
    qp.add_circuit(circuit_name, pre + middle + meas_x)
    circuits.append(circuit_name)

    circuit_name = "quantum_phase_%d"%exp_index + bloch_vector[1]
    qp.add_circuit(circuit_name, pre + middle + meas_y)
    circuits.append(circuit_name)

    circuit_name = "quantum_phase_%d"%exp_index + bloch_vector[2]
    qp.add_circuit(circuit_name, pre + middle + meas_z)
    circuits.append(circuit_name)
    
# Execute the circuit
result = qp.execute(circuits, backend = 'local_qasm_simulator')

# Print result
for exp_index in exp_vector:
    bloch = [0, 0, 0]
    for bloch_index in range(len(bloch_vector)):
        data = result.get_counts(circuits[3*exp_index+bloch_index])
        try:
            p0 = data['0']/1024.0
        except KeyError:
            p0 = 0
        try:
            p1 = data['1']/1024.0
        except KeyError:
            p1 = 0
        bloch[bloch_index] = p0-p1
    print('[{}, {}, {}]'.format(bloch[0], bloch[1], bloch[2]))