# single_q_measurement.py
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.wrapper import execute

# Define the Quantum and Classical Registers
q = QuantumRegister(1)
c = ClassicalRegister(1)

# Build the circuit
single_q_measurement = QuantumCircuit(q, c)
single_q_measurement.measure(q, c)
 
# Execute the circuit
result = execute(single_q_measurement, backend_name = 'local_qasm_simulator')

# Print the result
print(result.get_counts(single_q_measurement))