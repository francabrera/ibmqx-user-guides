# use QISKit.org
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.wrapper import execute


# Define the Quantum and Classical Registers
q = QuantumRegister(1)
c = ClassicalRegister(1)

# Build the circuit
excited_state = QuantumCircuit(q, c)
excited_state.x(q)
excited_state.measure(q, c)

# Execute the circuit
result = execute(excited_state, backend_name = 'local_qasm_simulator')

# Print result
print(result.get_counts(excited_state))