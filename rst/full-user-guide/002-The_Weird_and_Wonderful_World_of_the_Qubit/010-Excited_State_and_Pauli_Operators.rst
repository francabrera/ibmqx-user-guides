Excited State and Pauli Operators
=================================

| As you may have guessed, a qubit does more than just sit around in the
  :math:`|0\rangle` ground state. To put it into the :math:`|1\rangle`
  *excited* state, we need a *quantum gate*. In this section we will
  introduce gates, and how to use them in the Composer.

| Quantum gates, or operations, are typically represented as matrices. A
  gate that acts on one qubit is represented by a :math:`2 \times 2`
  `unitary matrix <https://en.wikipedia.org/wiki/Unitary_matrix>`__.
  Since quantum operations must be reversible and preserve probability
  amplitudes, the matrices must be unitary. The result of the quantum
  gate is found by multiplying the matrix representing the gate with the
  vector representing the quantum state.

      :math:`|\psi'\rangle=U|\psi\rangle`  where :math:`U^\dagger U = 1` 
(:math:`A^\dagger` represents the complex conjugation and transpose of any
matrix :math:`A`).

| A common group of gates, known as the `Pauli
  Operators <https://en.wikipedia.org/wiki/Pauli_matrices>`__, are
  represented by the matrices

|                          |image0|

| The Pauli :math:`X` gate is known as an :math:`X_{\pi}`-rotation. It takes
  :math:`|0\rangle\rightarrow X|0\rangle=|1\rangle`; in other words,
  it flips the zero to a one, or vice versa (this is why it is also
  commonly referred to as a bit-flip). Try the Pauli :math:`X` gate in the
  Composer, using the score file below. Did you find that, unlike in the
  example on the previous page, the qubit ended up in the excited
  state :math:`|1\rangle` with high probability? Like before, any
  deviation from the excited state is likely due to decoherence and
  imperfect measurements.

|image1|

| In the other examples below, explore what the Pauli Operators do. What
  do you get when you try a :math:`Y` or :math:`Z` gate? Did you find that :math:`Y`
  gave you an excited state and :math:`Z` did not do anything?

|
| **1Q Pauli X**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=d45a9317f90b97fddfda9f15f31eb14f&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-d45a9317f90b97fddfda9f15f31eb14f.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=d45a9317f90b97fddfda9f15f31eb14f&sharedCode=true" target="_parent" style="text-align: right; display: block;">Open in composer</a>

|
| **1Q Pauli Y**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=d45a9317f90b97fddfda9f15f33478de&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-d45a9317f90b97fddfda9f15f33478de.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=d45a9317f90b97fddfda9f15f33478de&sharedCode=true" target="_parent" style="text-align: right; display: block;">Open in composer</a>

|
| **1Q Pauli Z**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=8afcf3a276348f6c37ee3246a5e3c561&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-8afcf3a276348f6c37ee3246a5e3c561.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=8afcf3a276348f6c37ee3246a5e3c561&sharedCode=true" target="_parent" style="text-align: right; display: block;">Open in composer</a>




.. |image0| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-01%20at%209.59.59%20AMg9al3vn7mf1xajor.png
.. |image1| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/excitededl80civwo8ncdi.png

