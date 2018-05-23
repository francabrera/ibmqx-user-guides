//Quantum Phase exp 1
OPENQASM 2.0;
include "qelib1.inc";

// Register declarations
qreg q[1];
creg c[1];

// Quantum Circuit
h q;
barrier q;
t q;
barrier q;
h q;
sdg q;
measure q -> c;