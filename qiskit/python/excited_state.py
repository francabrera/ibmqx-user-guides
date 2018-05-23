# excited_state.py
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute

# Define the Quantum and Classical Registers
q = QuantumRegister(1)
c = ClassicalRegister(1)

# Build the circuit
excited_state = QuantumCircuit(q, c)
excited_state.x(q)
excited_state.measure(q, c)

# Execute the circuit
job = execute(excited_state, backend = 'local_qasm_simulator', shots=1024)
result = job.result()

# Print the result
print(result.get_counts(excited_state))