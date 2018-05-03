Single-Qubit Gates
==================

.. toctree::
   :maxdepth: 1
   :glob:
   :hidden:

   *

| **Just as classical computers perform calculations by manipulating
  bits between the 0 and 1 states, we manipulate qubits to perform
  calculations on a quantum computer. In this section, we’ll show you
  how to use some important single-qubit gates.**

| To understand what these do mathematically, go ahead and check out the
  full User Guide.

.. cssclass:: h2

X gate


| Let’s start with the \ *X* gate, which is known as a “bit-flip”, since
  it flips the 0 to 1 and vice versa. This is similar to a classical NOT
  gate.

| |image0|

| It is also known as an X-rotation, since it rotates the state by
  :math:`\pi` radians around the X-axis. If you start in the
  :math:`|0\rangle` state at the top of the Bloch sphere, the X gate
  rotates you to the bottom of the Bloch sphere (:math:`|1\rangle`). See
  the below schematic and also try the X gate in the Composer, using the
  score below.

|

| |image1|

|

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=1a35de9b1f3b236cf98fc3e0960da72e&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-075df8e2dacac4fa2f76486ecc824a52.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=1a35de9b1f3b236cf98fc3e0960da72e&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>


|

| |image3|


.. |image0| image:: data:image/png;base64,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
.. |image1| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/x-gatefacd0ok4wd7eewmi.png
.. |image2| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/1q-xgate1dgbxpvuvbm1v2t9.png
.. |image3| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/403gzthc7pi8ft4vx6r.png

