Basic Circuit Identities and Larger Circuits
============================================

| There are several facts about quantum circuits that can be used to
  express more complicated `unitary
  transformations <https://en.wikipedia.org/wiki/Unitary_transformation>`__,
  write circuits more concisely, or adapt circuits to experimental
  constraints.

Changing the direction of a CNOT gate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| In the first example "CNOT (Reverse)," we consider how to implement a
  CNOT gate from control qubit 2 to target qubit 1 (notated
  :math:`CNOT_{21}`) using a CNOT gate that acts in the opposite direction,
  from control qubit 1 to target qubit 2, :math:`CNOT_{12}`. By multiplying
  the matrices for each gate, you can convince yourself that
  :math:`(H\otimes H)CNOT_{12}(H\otimes H)=CNOT_{21}`.

|image0|

| The `Kronecker
  product <https://en.wikipedia.org/wiki/Kronecker_product>`__
  :math:`H\otimes H` in this equation is equal to a four-by-four matrix
  :math:`\frac{1}{\sqrt{2}}\begin{pmatrix} H & H \\ H &
  -H\end{pmatrix}`. If you run the example, you will confirm that this
  combination of Hadamard and CNOT gates implements a CNOT gate in the
  opposite direction. The `Pauli <https://en.wikipedia.org/wiki/Quantum_gate#Pauli-X_gate>`__
  :math:`X` acts
  to invert the control qubit 2, and the result is :math:`|11\rangle` as
  expected for :math:`CNOT_{21}`.

Swapping the states of qubits
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Our second example, "Swap," demonstrates a building block that allows
  you to permute the information stored in a set of qubits. Suppose we
  want to exchange the states of a pair of qubits by implementing a SWAP
  gate on the pair. There is no SWAP gate in our basis, but we can
  construct one from three CNOT gates
  :math:`SWAP_{12}=CNOT_{12}CNOT_{21}CNOT_{12}`.

|image1|

To see that this is true, it is enough to look at what happens to each
classical state :math:`00`, :math:`01`, :math:`10`, and :math:`11`. Let's consider :math:`01`. The
first gate :math:`CNOT_{12}` does nothing since the control is :math:`0`. The
second gate :math:`CNOT_{21}` flips the first qubit, so we have :math:`11`.
Finally, the last :math:`CNOT_{12}` flips the second qubit and we get :math:`10`.
The :math:`1` has moved from the second qubit to the first. The other cases
can be worked out similarly. Now you can see this for yourself by
running the "Swap" example below. Notice that we have used the "CNOT
(Reverse)" identity to change the direction of the :math:`CNOT_{21}` gate,
since this is necessary to run the example on the real device. Try
deleting the Pauli :math:`X` and placing a Pauli :math:`X` on qubit 1 instead.

| In the experimental device, not all qubits are connected to each
  other; therefore, some two-qubit gates cannot be applied directly. In
  the third example, "Swap Q0 with Q1," we show how to swap a pair of
  qubits that are not directly connected to each other but share a
  common neighbor (in this case Q2). The state :math:`|+\rangle`, prepared
  by the first Hadamard gate on :math:`Q_0`, is swapped into :math:`Q_1` by three
  successive SWAP gates.

Adding a control qubit to a gate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some unitary transformations can be constructed exactly using gates in
our basis. One set of transformations we use regularly are
controlled-Pauli operations, where we apply a Pauli gate to a target
qubit if a control qubit is :math:`|1\rangle`. The CNOT gate is a
controlled-:math:`X` gate. Since we know that :math:`HXH=Z` and :math:`SXS^\dagger=Y`,
and furthermore that :math:`HH=I` and :math:`SS^\dagger=I`, it is straightforward
to construct circuits for controlled-:math:`Z` and controlled-:math:`Y`. This is
illustrated in the following figure, where :math:`P` is a Pauli gate :math:`X`, :math:`Y`,
or :math:`Z`, and :math:`C` is a Clifford operation such as :math:`I`, :math:`S`, or :math:`H`.

| |image2|

| For a more involved example, let's add a control qubit to a Hadamard
  gate to implement a controlled-Hadamard operation:

| |image3|

It turns out that we can write down a circuit for a controlled-:math:`V`
operation if we can find three circuits :math:`A`, :math:`B`, and :math:`C` such that
:math:`ABC=I` and :math:`e^{i\alpha}AZBZC=V` [`Barenco et al.,
1995 <http://journals.aps.org/pra/abstract/10.1103/PhysRevA.52.3457?cm_mc_uid=43781767191014577577895&cm_mc_sid_50200000=1460741020>`__].
There is a general recipe for doing this, but we will just write down a
solution for when :math:`V=H` that you can check for yourself:
:math:`A=e^{i3\pi/8}XSHTHS^\dagger`, :math:`B=e^{-i\pi/8}SHT^\dagger
HS^\dagger HSH`, :math:`C=e^{-i\pi/4}HSH`, and :math:`e^{i\alpha}=-i`.
Combining these circuits as shown here 

|image4|

| and making some simplifications, we get the result shown in the fourth
  example, "controlled-Hadamard." This example applies a Hadamard gate
  to the control qubit, :math:`Q_0`, and then applies the controlled-Hadamard
  circuit from :math:`Q_0` to :math:`Q_2`. This creates the output state
  :math:`\frac{1}{\sqrt{2}}\left(|00\rangle+|1+\rangle\right)=\frac{1}{\sqrt{2}}|00\rangle+\frac{1}{2}|10\rangle+\frac{1}{2}|11\rangle`.
  Try deleting the first Hadamard gate on :math:`Q_0` and replacing it with a
  bit-flip (:math:`X`) to see what happens. Can you implement circuits for
  other controlled gates, such as a controlled-S?

Approximating a unitary transformation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Most unitary transformations cannot be written exactly using the gates
  we have in our basis; but because our basis is a discrete universal
  set, it *is* possible to approximate any unitary transformation to any
  accuracy. Let's see an example of this. The :math:`\sqrt{T}` unitary
  transformation cannot be written exactly using our basis. Since
  :math:`\sqrt{T}` is a :math:`Z`-rotation, the identity gate (which does nothing)
  is an approximate :math:`\sqrt{T}` gate, but not a very good one. The fifth
  example "Approximate sqrt(T)" gives a much better approximation using
  :math:`17` Hadamard, S, and T gates. This example first puts the qubit
  :math:`Q_0` on the equator of the Bloch sphere using a Hadamard gate, then
  applies the :math:`17` gate sequence. We use `state
  tomography <https://en.wikipedia.org/wiki/Quantum_tomography>`__ to
  observe the final state on the Bloch sphere. Had we applied an exact
  :math:`\sqrt{T}` gate, the final state would correspond to the point
  :math:`(\frac{\sqrt{2+\sqrt{2}}}{2},\frac{\sqrt{2-\sqrt{2}}}{2},0)\approx
  (0.92388,0.38268,0)` on the Bloch sphere. How good is the :math:`17` gate
  approximation? Arbitrarily good approximations exist, so can you find
  a better one? How might you use these circuits to construct an
  approximate controlled-:math:`T` unitary transformation?

The Toffoli gate
^^^^^^^^^^^^^^^^

Our final examples, "Toffoli with flips" and "Toffoli state" demonstrate
how to implement the reversible circuit equivalent of the (irreversible,
classical) AND gate using gates from our basis. An AND gate has two
inputs and one output, and outputs 1 if and only if both inputs are 1.
One reason the AND gate is important for computation is that it is a
non-linear transformation (a multiplication). Why do we say AND is
irreversible? Notice that all three inputs :math:`00`, :math:`01`, and :math:`10` result
in an output of 0. If you see that the output of the gate is 0, you
can't undo the gate because you don't know which of these three inputs
gave you the result. Since there are three possible answers, even if you
add another output qubit, you won't have enough information to undo the
gate, since you must distinguish 3 cases, and there are only two choices
for the state of the new qubit. However, it is possible to implement AND
reversibly using 3 wires. This reversible AND gate is called the
`Toffoli gate <https://en.wikipedia.org/wiki/Toffoli_gate>`__
:math:`TOF|a,b,c\rangle=|a,b,(a\ \mathrm{AND}\ b)\ \mathrm{XOR}\
c\rangle`.

|image5|

| It is not obvious how to build a Toffoli gate from gates in our basis
  [\ `Barenco et al.,
  1995 <http://journals.aps.org/pra/abstract/10.1103/PhysRevA.52.3457?cm_mc_uid=43781767191014577577895&cm_mc_sid_50200000=1460741020>`__\ ].
  The main idea is illustrated in the following figure

| |image6|

| where :math:`V=\sqrt{U}`. By tracing through each value of the two control
  qubits, you can convince yourself that a :math:`U` gate is applied to the
  target qubit if and only if both controls are :math:`1`. Using ideas we have
  already described, you could now implement each controlled-:math:`V` gate to
  arrive at some circuit for the doubly-controlled-:math:`U` gate. It turns
  out that the minimum number of CNOT gates required to implement the
  Toffoli gate is 6 [`Shende and Markov,
  2009 <http://dl.acm.org/citation.cfm?id=2011799>`__]:

|image7|

| The "Toffoli with flips" example below allows you to choose an input
  state by changing the single-qubit gates at the beginning of the
  circuit. Right now they are set to Pauli :math:`X` on qubits 0 and 1 and
  identity on qubit 2, so the default output is :math:`|111\rangle`. You
  will notice that the example circuit uses 9 CNOT gates instead of the
  optimal number 6. This is because we wrote the circuit so it can run
  on the real device, which requires inserting a SWAP gate on qubits 1
  and 2 near the end of the circuit. Note that we do not undo this swap,
  so if the input qubit labels are :math:`0,1,2`, the output labels are
  actually :math:`0,2,1`. This means, for example, that an input of :math:`010`
  produces output :math:`001` (not :math:`010`). Finally, the "Toffoli state"
  example demonstrates the creation of an interesting 3-qubit entangled
  state
  :math:`SWAP_{1,2}TOF|++0\rangle_{0,1,2}=\frac{1}{2}\left(|000\rangle+|001\rangle+|100\rangle+|111\rangle\right)`
  that encodes the `truth
  table <https://en.wikipedia.org/wiki/Truth_table>`__ of the Toffoli
  gate.

| Using the Toffoli gate, it is possible to construct more complex
  circuits. A single Toffoli gate is sufficient to implement a modulo-4
  addition operation between a pair of 2-bit registers or an
  increment-by-one operation from one 2-bit register to another. Can you
  find circuits for these operations and run them in the Quantum
  Composer?


|
| **Approximate sqrt(T)**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=b5a0e7376ded40cd7dc1022e778fd799&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-b9096192e0ccec3ff6ac2156b7d080ee.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=b5a0e7376ded40cd7dc1022e778fd799&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Toffoli with flips**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=4de5b472cdbc8f33b422ee097e26a3f1&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-6d67a99a2c4c052189cdc290465a8a0f.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=4de5b472cdbc8f33b422ee097e26a3f1&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **CNOT (Reversed)**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=56bfed556c0d64e8b92649d5fb206a21&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-6d67a99a2c4c052189cdc290465a7bda.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=56bfed556c0d64e8b92649d5fb206a21&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **SWAP Gate**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=5537ba08c4b9b9369c47ea0fd67d26ea&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-cab6cbd8d09fa9a72bd276d9c2c1f6db.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=5537ba08c4b9b9369c47ea0fd67d26ea&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Swap q[0] and q[1]**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=5537ba08c4b9b9369c47ea0fd67c616a&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-ac12517d7526a77d19ce104d971a024a.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=5537ba08c4b9b9369c47ea0fd67c616a&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Controlled-Hadamard**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=5537ba08c4b9b9369c47ea0fd6706724&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-4568159e2e0816fb088fec7ee6955bbf.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=5537ba08c4b9b9369c47ea0fd6706724&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **3Q Toffoli state**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=a685beebe7614db5a17b8eddbdcd7e90&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-ba6021130f09ec06b6a5646bdcfeba8b.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=a685beebe7614db5a17b8eddbdcd7e90&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>



.. |image0| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/cnot_reversetvhxy1y40307ldi.png
.. |image1| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/swapedtm8jhiv1ckgldi.png
.. |image2| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/cPauli51b90orbw2zc9pb9.png
.. |image3| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/c-Hcmvfpboi12359udi.png
.. |image4| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/add-controldfjvwzojd8udte29.png
.. |image5| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/toffoli_def7k5imm5yhlivn29.png
.. |image6| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/double-controlled-Uolugr6dbwti0ms4i.png
.. |image7| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/toffoli-6-cnotshgwstno2n3lerk9.png

