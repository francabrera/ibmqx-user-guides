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

|
| **Plaquette Z 0000**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=618bfcf17927bad8e5a5f8d37568772d&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-0ef8d525ddb9f739bb8fb4cb4c9d0b81.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=618bfcf17927bad8e5a5f8d37568772d&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 0001**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=5cba20db95acffdf97bf95af4f253de8&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-7bf1fe8b112a27f1defdd1797e531f4e.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=5cba20db95acffdf97bf95af4f253de8&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 0010**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=e356856b01d8bc9f8db0d3edced40ec1&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-ac12517d7526a77d19ce104d971ed710.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=e356856b01d8bc9f8db0d3edced40ec1&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 0011**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=35cfa432f306d500aa85941a932318bf&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-86e01da97076b98d2319178fd250c14b.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=35cfa432f306d500aa85941a932318bf&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 0100**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=35cfa432f306d500aa85941a93421b6f&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-4568159e2e0816fb088fec7ee697a61d.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=35cfa432f306d500aa85941a93421b6f&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 0101**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=9d8a5f01839f380c33855ba11714ad18&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-0ef8d525ddb9f739bb8fb4cb4c9f395e.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=9d8a5f01839f380c33855ba11714ad18&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 0110**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=618bfcf17927bad8e5a5f8d375b37f29&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-c1908bfce53e5d26b810465dbb768bbb.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=618bfcf17927bad8e5a5f8d375b37f29&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 0111**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=c7177d58a05920ca438c872f1ce253b7&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-7cf716ef5c56be1df8419ec1f2051ebe.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=c7177d58a05920ca438c872f1ce253b7&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 1000**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=deb1f2aa1f7c5718bfdb4029eb67c200&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-9d173b5b4a53131382b97843d2fda623.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=deb1f2aa1f7c5718bfdb4029eb67c200&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 1001**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=618bfcf17927bad8e5a5f8d375c82131&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-570b68405ba63ca75c724d3f40ab48c2.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=618bfcf17927bad8e5a5f8d375c82131&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 1010**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=c495ddc03a0d87c9c4c3a9b31a145813&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-0eb40f5d1eed7b2d8fd23c2c8774d0b0.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=c495ddc03a0d87c9c4c3a9b31a145813&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 1011**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=7ce6f28163171c882dc7228f080ca3a1&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-6769d2329c7fb8be2514f419db59240f.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=7ce6f28163171c882dc7228f080ca3a1&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 1100**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=9d8a5f01839f380c33855ba11789cc51&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-9d173b5b4a53131382b97843d2fc0d75.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=9d8a5f01839f380c33855ba11789cc51&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 1101**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=5cba20db95acffdf97bf95af4fc5c23c&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-c1908bfce53e5d26b810465dbb758199.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=5cba20db95acffdf97bf95af4fc5c23c&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 1110**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=b2d815e741f0b820bd5b93a583b3bf93&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-7bf1fe8b112a27f1defdd1797e5335e7.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=b2d815e741f0b820bd5b93a583b3bf93&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 1111**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=84becc47be891676e7ddc04e8760069c&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-4568159e2e0816fb088fec7ee697b2b1.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=84becc47be891676e7ddc04e8760069c&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette X +-+-**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=b5a0e7376ded40cd7dc1022e777c3e7a&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-ac12517d7526a77d19ce104d971e4e4c.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=b5a0e7376ded40cd7dc1022e777c3e7a&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>


.. |image0| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/PlaquetteWebExp18626ul21g1ra4i.png

