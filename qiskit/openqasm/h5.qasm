//H^5
OPENQASM 2.0;
include "qelib1.inc";

// Register declarations
qreg q[5];
creg c[5];

// Quantum Circuit
h q;
measure q -> c;