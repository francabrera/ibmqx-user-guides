//CNOT 01
OPENQASM 2.0;
include "qelib1.inc";

// Register declarations
qreg q[2];
creg c[2];

// Quantum Circuit
x q[0];
cx q[0],q[1]l
measure q -> c;