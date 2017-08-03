Stabilizer Measurements
=======================

`Stabilizer codes <http://arxiv.org/abs/quant-ph/9705052>`__ are a large
and important family of quantum error-correcting codes. These codes are
defined as joint eigenspaces of a collection of operators known as
*stabilizers*. The eigenvalues of the stabilizers are used to detect and
diagnose errors. Therefore, many quantum error-correction protocols make
*stabilizer measurements* to obtain these eigenvalues. One way to
implement a stabilizer measurement is to use extra qubits, known as
*syndrome qubits*, to detect errors on *data qubits* that are part of
your computation. Stabilizer measurements can identify a collective
property of a set of data qubits; one such property is the
qubits' \ *parity*.

| Consider the quantum bit-flip code again. The bit-flip code is a
  stabilizer code, and one choice for its stabilizers is :math:`Z\otimes
  Z\otimes I` and :math:`I\otimes Z\otimes Z`. A valid codeword is a :math:`+1`
  eigenstate of these stabilizer operators. For :math:`Z`-type operators such
  as these, the stabilizer enforces that the parity of the first two
  qubits is even, and the parity of the second two qubits is even. The
  stabilizer measurement tells us whether the parity has changed, which
  we can use to diagnose the error.

In quantum codes such as the `surface
code <https://en.wikipedia.org/wiki/Toric_code>`__, there are :math:`Z`-type
and :math:`X`-type stabilizers to measure. The :math:`X`-type stabilizers simply
enforce a parity constraint in the :math:`\{|+\rangle,|-\rangle\}`
basis. For example, the states :math:`|++\rangle` and :math:`|--\rangle` are
:math:`+1` eigenstates of :math:`X\otimes X`. The :math:`Z`-type stabilizers in the bulk
of the surface code have the form :math:`Z\otimes Z\otimes Z\otimes Z` and
detect bit-flip errors on the four data qubits that are involved. The
:math:`X`-type stabilizers in the bulk have the form :math:`X\otimes X\otimes
X\otimes X` and detect phase-flip errors. These stabilizer measurements
are implemented by computing the associated bit-flip or phase-flip
parities into a syndrome qubit.

| In the Composer, we can test such stabilizer measurements using
  :math:`Q_2` as a syndrome qubit, and :math:`Q_0`, :math:`Q_1`, :math:`Q_3`, and
  :math:`Q_4` as data qubits. The :math:`Z`-type parity check is performed using
  a CNOT gate from each data qubit to the syndrome qubit. The :math:`X`-type
  parity check is simply the conjugate of the :math:`Z`-type check, obtained
  by applying Hadamard gates to the input and output data qubits. In a
  fault-tolerant implementation of the circuits, the order of gates is
  important to limit the spread of errors.

The scores below prepare different states of input parity. See if the
processor returns the proper parity measurements.

When we ran these experiments we got 

|                                                                  
    |image0|

| 

.. |image0| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/PlaquetteWebExp18626ul21g1ra4i.png

