//Negative Superposition State
OPENQASM 2.0;
include "qelib1.inc";

// Register declarations
qreg q[1];
creg c[1];

// Quantum Circuit
x q;
h q;
measure q -> c;