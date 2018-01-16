#!/bin/bash

# you would need to comment the next line in case you already have the remote in your local
git remote add -f -t master --no-tags qiskit https://github.com/QISKit/qiskit-sdk-py.git
# you would need to comment the next line in case you already have the remote in your local
git remote add -f -t master --no-tags openqasm https://github.com/QISKit/openqasm.git

# qiskit examples
git rm -rf examples/qiskit
git read-tree --prefix=examples/qiskit/ -u qiskit/master:examples
git commit -m "Updating qiskit examples"

# openqasm examples
git rm -rf examples/openqasm
git read-tree --prefix=examples/openqasm/ -u openqasm/master:examples
git commit -m "Updating openqasm examples"
