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

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=88f85da989468e48a7b86fbd7342aacd&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-618bfcf17927bad8e5a5f8d37568772d.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=88f85da989468e48a7b86fbd7342aacd&sharedCode=true" target="_parent" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 0001**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=73c0b4cc547a3746ec13d741f790503c&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-5cba20db95acffdf97bf95af4f253de8.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=73c0b4cc547a3746ec13d741f790503c&sharedCode=true" target="_parent" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 0010**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=5c637ce6ad9e6925fc97ff8f6d637cf8&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-e356856b01d8bc9f8db0d3edced40ec1.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=5c637ce6ad9e6925fc97ff8f6d637cf8&sharedCode=true" target="_parent" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 0011**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=73042096a8123f444deea8dc0776168f&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-35cfa432f306d500aa85941a932318bf.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=73042096a8123f444deea8dc0776168f&sharedCode=true" target="_parent" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 0100**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=fd2bacdbe83dcd7e799d543626040679&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-35cfa432f306d500aa85941a93421b6f.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=fd2bacdbe83dcd7e799d543626040679&sharedCode=true" target="_parent" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 0101**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=ddde23cda9868f8e77b19c514100c20a&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-9d8a5f01839f380c33855ba11714ad18.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=ddde23cda9868f8e77b19c514100c20a&sharedCode=true" target="_parent" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 0110**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=d85f163168bc0b87f31993da447b0664&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-618bfcf17927bad8e5a5f8d375b37f29.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=d85f163168bc0b87f31993da447b0664&sharedCode=true" target="_parent" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 0111**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=b1e1dcdea6ac3e194e2e995e5605186f&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-c7177d58a05920ca438c872f1ce253b7.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=b1e1dcdea6ac3e194e2e995e5605186f&sharedCode=true" target="_parent" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 1000**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=49902d904b5e190f7769d85e14bc6cbd&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-deb1f2aa1f7c5718bfdb4029eb67c200.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=49902d904b5e190f7769d85e14bc6cbd&sharedCode=true" target="_parent" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 1001**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=cd6085bcd2792801568b6527a7c86410&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-618bfcf17927bad8e5a5f8d375c82131.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=cd6085bcd2792801568b6527a7c86410&sharedCode=true" target="_parent" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 1010**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=80b47c8aacaba8c894adad2082fdda7c&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-c495ddc03a0d87c9c4c3a9b31a145813.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=80b47c8aacaba8c894adad2082fdda7c&sharedCode=true" target="_parent" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 1011**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=6a6bc5d143b797a6a0b350b0e886147a&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-7ce6f28163171c882dc7228f080ca3a1.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=6a6bc5d143b797a6a0b350b0e886147a&sharedCode=true" target="_parent" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 1100**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=b7ae4ac250c374982fad0b77e2c3f913&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-9d8a5f01839f380c33855ba11789cc51.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=b7ae4ac250c374982fad0b77e2c3f913&sharedCode=true" target="_parent" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 1101**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=5551ebf5b17fe88f045a7f89f0adb517&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-5cba20db95acffdf97bf95af4fc5c23c.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=5551ebf5b17fe88f045a7f89f0adb517&sharedCode=true" target="_parent" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 1110**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=790a8f6a616af449d3dddbda9cb8a008&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-b2d815e741f0b820bd5b93a583b3bf93.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=790a8f6a616af449d3dddbda9cb8a008&sharedCode=true" target="_parent" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette Z 1111**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=9cc5f1846285c8a84a95680d755cb0e8&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-84becc47be891676e7ddc04e8760069c.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=9cc5f1846285c8a84a95680d755cb0e8&sharedCode=true" target="_parent" style="text-align: right; display: block;">Open in composer</a>

|
| **Plaquette X +-+-**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=30a411ad2c8222e10635b8a6bc830a8e&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-b5a0e7376ded40cd7dc1022e777c3e7a.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=30a411ad2c8222e10635b8a6bc830a8e&sharedCode=true" target="_parent" style="text-align: right; display: block;">Open in composer</a>

.. |image0| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/PlaquetteWebExp18626ul21g1ra4i.png

