//classical state
OPENQASM 2.0;
include "qelib1.inc";

// Register declarations
qreg q[5];
creg c[5];

// Quantum Circuit
x q[0];
x q[2];
measure q -> c;