//CNOT 00
OPENQASM 2.0;
include "qelib1.inc";

// Register declarations
qreg q[2];
creg c[2];

// Quantum Circuit
cx q[0],q[1]
measure q -> c;