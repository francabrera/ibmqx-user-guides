Multiple Qubits
===============

Until this point, we have only considered a single qubit; let's now
consider more than one qubit in a system. The complex vector space of
an :math:`n` qubit system has a dimension equal to :math:`2^n`, which we
denote :math:`\mathbb{C}^{2^{n}}`. The standard basis is the set of all
binary strings for :math:`k\in \{0, 2^n-1\}`. For example, the basis
for two qubits is

.. math:: 
  ~~~~~~~~\{|00\rangle, |01\rangle,  |10\rangle,  |11\rangle\};

for three qubits,

:math:`\{|000\rangle, |001\rangle,  |010\rangle,  |011\rangle, 
  |100\rangle,  |101\rangle,  |110\rangle,  |111\rangle \}`;

and for four qubits,

:math:`\{|0000\rangle, |0001\rangle,  |0010\rangle,  |0011\rangle, 
|0100\rangle,  |0101\rangle,  |0110\rangle,  |0111\rangle,
|1000\rangle, |1001\rangle,`  :math:`|1010\rangle,  |1011\rangle, 
|1100\rangle,  |1101\rangle,  |1110\rangle,  |1111\rangle 
\}`.

You may notice the number of terms is increasing exponentially. Try
writing out all 32 terms for five qubits, then try writing them all out
for 64 qubits! (This is like the famous `wheat and chessboard
problem <https://en.wikipedia.org/wiki/Wheat_and_chessboard_problem>`__.)
This exponential increase is one of the reasons why a large quantum
system becomes impossible to simulate on a conventional computer. 

Note, however, that the complexity is subtler than just the absolute
number of terms growing exponentially. A classical computer that has
:math:`n`-bits also has :math:`2^n` possible configurations; at any one point in
time, the computer state is in one and only one of these configurations.
For example, a classical computer takes an :math:`n` bit number, say
:math:`00000`, and performs bit-wise operations on it, mapping the input
though an :math:`n`-bit intermediate state such as :math:`00001`, which is then
output as another :math:`n`-bit number :math:`10101`. Interestingly, a quantum
computer also takes in an :math:`n`-bit number and outputs an :math:`n`-bit
number; but because of the superposition principle and the possibility
of entanglement, the intermediate state is very different. To describe
it requires :math:`2^n` complex numbers, giving a lot more room for
maneuvering. 

| |image0|

| 

| As an example, try running the "Random Classical Circuit" provided
  below. It takes the initial state :math:`|0\rangle^{\otimes n}` and
  should produce the output :math:`|10101\rangle`. By using :math:`X`
  operations (NOTs) you can take the :math:`|0\rangle^{\otimes n}` to any
  classical state.

To do interesting things that make use of those many configurations in
the quantum world, we need gates that perform conditional logic between
qubits. The conditional gate we have provided is the Controlled-NOT, or
CNOT.  It is represented by the element  

|                         |image1|

The CNOT gate's action on classical basis states is to flip (apply a NOT
or :math:`X` gate to) the target qubit if the control qubit is
:math:`|1\rangle`; otherwise it does nothing. The CNOT plays the role of
the classical XOR gate, but unlike the XOR, it is a two-output gate in
order to be
`reversible <https://en.wikipedia.org/wiki/Reversible_computing>`__\ (as
all quantum gates must be).  It is represented by the matrix

|                           |image2|

| Try the "CNOT Circuits" example below with different input states.
  Note that the :math:`X` gates have prepared the qubits in a different
  configuration for each example. Here you can see the results we got
  when we ran these experiments on the processor:

|                            |image3|

Finally, many `quantum
algorithms <https://en.wikipedia.org/wiki/Quantum_algorithm>`__ start
out by applying a Hadamard gate, because it maps *:math:`n`* qubits prepared
in state :math:`|0\rangle^{\otimes n}` to a superposition of all :math:`2^n`
orthogonal states with equal weight. Try out the five-qubit version. You
should see that it has made a quantum sphere that points in all
directions with a small weight :math:`1/(2^5)`. Try adding the CNOT gate to
make your own complex quantum states. In the next sections we will show
you how quantum computers take advantage of a certain peculiarity known
as *entangled* states.

.. raw:: html

  OpenQasm Input

.. literalinclude:: ../../../qiskit/openqasm/classical_state.qasm
  :language: c++
  :linenos:

.. raw:: html

  OpenQasm Input

.. literalinclude:: ../../../qiskit/openqasm/h5.qasm
  :language: c++
  :linenos:

.. raw:: html

  OpenQasm Input

.. literalinclude:: ../../../qiskit/openqasm/cnot_00.qasm
  :language: c++
  :linenos:

.. raw:: html

  OpenQasm Input

.. literalinclude:: ../../../qiskit/openqasm/cnot_01.qasm
  :language: c++
  :linenos:

.. raw:: html

  OpenQasm Input

.. literalinclude:: ../../../qiskit/openqasm/cnot_10.qasm
  :language: c++
  :linenos:

.. raw:: html

  OpenQasm Input

.. literalinclude:: ../../../qiskit/openqasm/cnot_11.qasm
  :language: c++
  :linenos:


.. |image0| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/exponential-2nyf69faj94rkke29.png
.. |image1| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-01%20at%2011.19.55%20AMsvbpgjmu97iizfr.png
.. |image2| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-01%20at%2011.21.09%20AM77nnrwadzwa5rk9.png
.. |image3| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-03%20at%2010.04.10%20PMkoyeh28bqm4y4x6r.png

