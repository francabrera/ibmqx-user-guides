Decoherence
===========

| Real quantum computers must deal with
  `decoherence <https://en.wikipedia.org/wiki/Quantum_decoherence>`_,
  or the loss of information due to environmental disturbances (noise).
  The Bloch vector formalism we introduced in the previous section is
  sufficient to describe the state of the system under decoherence
  processes. The `pure states <https://en.wikipedia.org/wiki/Quantum_state#Pure_states>`_ we
  have studied so far have a Bloch vector of length 1, touching the
  surface of the Bloch sphere, and can be represented in density matrix
  form as :math:`\rho=| \psi\rangle \langle \psi |`. Decoherence causes
  a change in our quantum states from pure to `mixed states <https://en.wikipedia.org/wiki/Quantum_state#Mixed_states>`__,
  which have a `density matrix <https://en.wikipedia.org/wiki/Density_matrix>`__ :math:`\rho`
  that can be written as a sum over pure states

:math:`\rho = \sum_k p_k | \psi_k\rangle \langle \psi_k |`

| and a Bloch vector that sits inside the Bloch sphere

:math:`|\langle X\rangle|^2 +  |\langle Y\rangle|^2 + | \langle Z\rangle|^2 < 1`.

Energy relaxation and :math:`T_1`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One important decoherence process is called *energy relaxation*, where
the excited :math:`|1\rangle` state decays toward the ground state
:math:`|0\rangle`. The time constant of this process, :math:`T_1`, is an
extremely important figure-of-merit for any implementation of quantum
computing, and one in which IBM has made great progress in recent years,
ultimately leading to the prototype quantum computer you are now using.
Experiment with the circuits below to see how adding many repetitions of
additional do-nothing Idle :math:`Id` gates (or Identity gates; these are
gates that do nothing but wait) before measurement causes the state to
gradually decay towards :math:`|0\rangle`.

Dephasing and :math:`T_2`
^^^^^^^^^^^^^^^^^^^^^^^^^

| Dephasing is another decoherence process, and unlike energy
  relaxation, it affects only superposition states. It can be understood
  solely in a quantum setting as it has no classical analog. The time
  constant :math:`T_2` includes the effect of dephasing as well as energy
  relaxation, and is another crucial figure-of-merit. Again, IBM has
  some of the world's best qubits by this metric. Experiment with the
  circuits below to see that with a Ramsey experiment, essentially
  separating two :math:`\pi`/2 rotations with an Idle, there is a decay in
  the final expected excited state signal. When pointing along the
  equator, the qubit is subjected to more decay channels than when it
  starts in the computational state :math:`| 1 \rangle`.

Progress in decoherence with superconducting qubits
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Because :math:`T_2` is such an important quantity, it is interesting to
  chart how far the community of superconducting qubits has come over
  the years. Here is a graph depicting :math:`T_2` versus time. 

| |image0|


|
| **Excited state (No idle)**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=f0c8e1f96638ef39ca67a6378231d4a4&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-b9096192e0ccec3ff6ac2156b7ce0b79.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=f0c8e1f96638ef39ca67a6378231d4a4&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Excited state (4 idle)**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=f0c8e1f96638ef39ca67a63782490887&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-95469a8631bfe86cdf55b0a254de46e3.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=f0c8e1f96638ef39ca67a63782490887&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Excited state (16 idle)**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=8d36692e07e55a8ef2688a910e62a9b4&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-0ef8d525ddb9f739bb8fb4cb4c826c0c.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=8d36692e07e55a8ef2688a910e62a9b4&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Ramsey (no idle)**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=117bf13ae0d48351f58fca70f11206d6&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-95469a8631bfe86cdf55b0a254de5399.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=117bf13ae0d48351f58fca70f11206d6&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Ramsey (4 idle)**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=8d36692e07e55a8ef2688a910e938fe2&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-6d67a99a2c4c052189cdc29046579b42.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=8d36692e07e55a8ef2688a910e938fe2&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Ramsey (16 idle)**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=b44dce9f84c53d75c991e794006a83f2&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-10910faa24c7d6aacafbfe41a9f9f67d.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=b44dce9f84c53d75c991e794006a83f2&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>


.. |image0| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/images-classroom/T2h1lc19xmqrdlsor.png

