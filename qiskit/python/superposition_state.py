# superposition_state.py
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute

# Define the Quantum and Classical Registers
q = QuantumRegister(1)
c = ClassicalRegister(1)

# Build the circuit
superposition_state = QuantumCircuit(q, c)
superposition_state.h(q)
superposition_state.measure(q, c)

# Execute the circuit
job = execute(superposition_state, backend = 'local_qasm_simulator', shots=1024)
result = job.result()

# Print the result
print(result.get_counts(superposition_state))