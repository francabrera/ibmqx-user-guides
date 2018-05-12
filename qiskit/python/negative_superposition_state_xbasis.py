# negative_superposition_state_xbasis.py
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute

# Define the Quantum and Classical Registers
q = QuantumRegister(1)
c = ClassicalRegister(1)

# Build the circuit
negative_superposition_state_xbasis = QuantumCircuit(q, c)
negative_superposition_state_xbasis.x(q)
negative_superposition_state_xbasis.h(q)
negative_superposition_state_xbasis.barrier()
negative_superposition_state_xbasis.h(q)
negative_superposition_state_xbasis.measure(q, c)

# Execute the circuit
job = execute(negative_superposition_state_xbasis, backend = 'local_qasm_simulator', shots=1024)
result = job.result()

# Print the result
print(result.get_counts(negative_superposition_state_xbasis))