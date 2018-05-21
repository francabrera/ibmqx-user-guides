Multi-Qubit Gates
=================

.. toctree::
   :maxdepth: 1
   :glob:
   :hidden:

..
   *

The notation for the state of a machine with multiple qubits is similar
to what we have been using, but now there are multiple numbers inside
the :math:`|\rangle` ‘ket’. For a two-qubit processor, the qubits can be
in four possible states:
:math:`|00\rangle`, :math:`|01\rangle`, :math:`|10\rangle`,
and :math:`|11\rangle`. Reading from left to right, the first number
represents the state of the second qubit and the second number
represents the state of the first qubit. That is to say: \ **the first
qubit (q0) is always listed at the far right**\ . We chose this notation
to be consistent with the classical binary representation of numbers.
Just like the single qubit, there can also be superpositions of these
states like::math:`\frac{1}{\sqrt{2}}(|00\rangle-|11\rangle)`. When
this state is measured, \ **both**\  qubits will have the same value,
but 50% of the time \ **both**\  will be 0 and 50% of the time both will
be 1. 

To do interesting things and make use of those many configurations in
the quantum world, we need gates that perform *conditional* logic
between qubits, meaning the state of one qubit depends on the state of
another. 

| The conditional gate we will use is the Controlled-NOT, or CNOT.  It
  is represented by the element:  

| |image0|

The CNOT gate's action on classical basis states is to flip (apply a NOT
or X gate to) the target qubit \ *only*\ if the control qubit
is :math:`|1\rangle`; otherwise it does nothing. 

Below is how the CNOT gate transforms a set of 2 qubits (where **the
first qubit – the one on the right – is the control**):

|image1|

Try the "CNOT Circuits" example below with different input states. Drag
the CNOT gate to the target qubit and then click on the control qubit to
add the link between them. \ **Note that the X gates have prepared the
qubits in a different configuration for each example.**\

|
| **CNOT (input 00)**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=1ae7fa71f3ad1e6f8fbe269fafcc7ca9&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-0ef8d525ddb9f739bb8fb4cb4c7aa53c.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=1ae7fa71f3ad1e6f8fbe269fafcc7ca9&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **CNOT (input 01)**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=1ae7fa71f3ad1e6f8fbe269fafd9abf4&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-ba6021130f09ec06b6a5646bdcf780f4.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=1ae7fa71f3ad1e6f8fbe269fafd9abf4&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **CNOT (input 10)**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=15d54765a0eeedcf83c173d5a6b80166&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-7bf1fe8b112a27f1defdd1797e4a3a95.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=15d54765a0eeedcf83c173d5a6b80166&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **CNOT (input 11)**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=7177ed173b5d2e3124c405339b9b6f15&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-c1908bfce53e5d26b810465dbb68ef3e.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=7177ed173b5d2e3124c405339b9b6f15&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>



.. |image0| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/cnotpiv8xpd3ep2jra4i.png
.. |image1| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/screen-shot-2017-03-04-at-5.10.14-pmb3gj6v8t7d9m5cdi.png

