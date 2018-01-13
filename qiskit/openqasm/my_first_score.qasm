// My First Score
OPENQASM 2.0;
include "qelib1.inc";

// Register declarations
qreg q[2];
creg c[2];

// Quantum Circuit
// Pauli operations 
x q[0];
y q[1];
z q[0];
barrier q;
// Clifford operations
h q;
s q[0];
sdg q[1];
cx q[0],q[1];
barrier q;
// non-Clifford operations
t q[0];
tdg q[1];
barrier q;
// measurement operations
measure q[0] -> c[0];
measure q[1] -> c[1];