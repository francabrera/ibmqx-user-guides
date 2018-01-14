# use QISKit.org
from qiskit import QuantumProgram

# useful additional packages
from qiskit.tools.visualization import plot_histogram

# Define the QProgram and the Quantum and Classical Registers
qp = QuantumProgram()
q = qp.create_quantum_register('q', 1)
c = qp.create_classical_register('c', 1)

# Build the circuit
superposition_state_xbasis = qp.create_circuit('superposition_state_xbasis', [q], [c])
superposition_state_xbasis.h(q)
superposition_state_xbasis.barrier()
superposition_state_xbasis.h(q)
superposition_state_xbasis.measure(q, c)

# Execute the circuit
result = qp.execute(['superposition_state_xbasis'], backend = 'local_qasm_simulator')

# Plot result
plot_histogram(result.get_counts('superposition_state_xbasis'))