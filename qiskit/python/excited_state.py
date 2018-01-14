# use QISKit.org
from qiskit import QuantumProgram

# Define the QProgram and the Quantum and Classical Registers
qp = QuantumProgram()
q = qp.create_quantum_register('q', 1)
c = qp.create_classical_register('c', 1)

# Build the circuit
excited_state = qp.create_circuit('excited_state', [q], [c])
excited_state.x(q)
excited_state.measure(q, c)

# Execute the circuit
result = qp.execute(['excited_state'], backend = 'local_qasm_simulator')

# Print result
print(result.get_counts('excited_state'))