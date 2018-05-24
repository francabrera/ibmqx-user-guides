Decoherence
===========

Real quantum computers must deal with `decoherence <https://en.wikipedia.org/wiki/Quantum_decoherence>`_,
or the loss of information due to environmental disturbances (noise). The Bloch vector formalism we 
introduced in the previous section is sufficient to describe the state of the system under decoherence
processes. The `pure states <https://en.wikipedia.org/wiki/Quantum_state#Pure_states>`_ we have studied 
so far have a Bloch vector of length 1, touching the surface of the Bloch sphere, 
and can be represented in density matrix form as :math:`\rho=| \psi\rangle \langle \psi |`.
Decoherence causes a change in our quantum states from pure to 
`mixed states <https://en.wikipedia.org/wiki/Quantum_state#Mixed_states>`__,
which have a `density matrix <https://en.wikipedia.org/wiki/Density_matrix>`__ :math:`\rho`
that can be written as a sum over pure states

:math:`\rho = \sum_k p_k | \psi_k\rangle \langle \psi_k |`

and a Bloch vector that sits inside the Bloch sphere

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

Below is a QISKit script for measuring :math:`T_1`.

.. raw:: html

  <a href="https://qiskit.org"  target="_blank">QISKit</a> example

.. literalinclude:: ../../../qiskit/python/t1.py
  :language: python
  :linenos:

Dephasing and :math:`T_2`
^^^^^^^^^^^^^^^^^^^^^^^^^

Dephasing is another decoherence process, and unlike energy
relaxation, it affects only superposition states. It can be understood
solely in a quantum setting as it has no classical analog. The time
constant :math:`T_2` includes the effect of dephasing as well as energy
relaxation, and is another crucial figure-of-merit. Again, IBM has
some of the world's best qubits by this metric. Practice with the
scripts below to investigate the Ramsey and echo experiments. A Ramsey experiment measures
:math:`T_2^*`, which can be affected by slow noise, and the echo experiment removes some of this noise. 

Below is a QISKit script for measuring :math:`T_2^*` (Ramsey) and :math:`T_2` (echo).

.. raw:: html

  <a href="https://qiskit.org"  target="_blank">QISKit</a> example

.. literalinclude:: ../../../qiskit/python/t2_ramsey.py
  :language: python
  :linenos:

.. raw:: html

  <a href="https://qiskit.org"  target="_blank">QISKit</a> example

.. literalinclude:: ../../../qiskit/python/t2_echo.py
  :language: python
  :linenos:

Progress in decoherence with superconducting qubits
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Because :math:`T_2` is such an important quantity, it is interesting to
chart how far the community of superconducting qubits has come over
the years. Here is a graph depicting :math:`T_2` versus time. 

|image0|

.. |image0| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/T2h1lc19xmqrdlsor.png
