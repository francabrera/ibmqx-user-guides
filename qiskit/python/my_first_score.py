# use QISKit.org
from qiskit import QuantumProgram

# Define the QProgram and the Quantum and Classical Registers
qp = QuantumProgram()
q = qp.create_quantum_register('q', 2)
c = qp.create_classical_register('c', 2)

# Build the circuit
my_first_score = qp.create_circuit('my_first_score', [q], [c])
# Pauli operations 
my_first_score.x(q[0])
my_first_score.y(q[1])
my_first_score.z(q[0])
my_first_score.barrier(q)
# Clifford operations
my_first_score.h(q)
my_first_score.s(q[0])
my_first_score.s(q[1]).inverse()
my_first_score.cx(q[0],q[1])
my_first_score.barrier(q)
# non-Clifford operations
my_first_score.t(q[0])
my_first_score.t(q[1]).inverse()
my_first_score.barrier(q)
# measurement operations
my_first_score.measure(q, c)
 
# Execute the circuit, to run on the real device change 
# backend = 'local_qasm_simulator' to backend = 'ibmqx...' and set the API.
# Also to explore the quantum randomness remove seed = 1
result = qp.execute(['my_first_score'], backend='local_qasm_simulator', seed=1)

# Print result
print(result.get_counts('my_first_score'))