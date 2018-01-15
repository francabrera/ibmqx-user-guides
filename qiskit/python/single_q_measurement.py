# use QISKit.org
from qiskit import QuantumProgram

# Define the QProgram and the Quantum and Classical Registers
qp = QuantumProgram()
q = qp.create_quantum_register('q', 1)
c = qp.create_classical_register('c', 1)

# Build the circuit
single_q_measurement = qp.create_circuit('single_q_measurement', [q], [c])
single_q_measurement.measure(q, c)
 
# Execute the circuit, to run on the real device change 
# backend = 'local_qasm_simulator' to backend = 'ibmqx...' and set the API.
# Also to explore the quantum randomness remove seed = 1
result = qp.execute(['single_q_measurement'], backend = 'local_qasm_simulator',seed=1)

# Print result
print(result.get_counts('single_q_measurement'))