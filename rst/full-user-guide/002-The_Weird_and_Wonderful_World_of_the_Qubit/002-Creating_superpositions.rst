Creating Superpositions
=======================

Up to this point, our system has behaved like a classical bit. 
To go beyond classical behavior, we must explore what it means to make a superposition. 
The operation for generating a superposition 
is the Hadamard gate, :math:`H`. In the Composer, this is the
blue gate labeled :math:`H`.

The simple score to make a superposition is given below. It starts with placing 
the :math:`H` gate on one of the qubits (which starts in the :math:`|0\rangle` state) 
and a standard measurement. Run the example below. 

**Superposition state**

.. raw:: html

  OpenQasm Input

.. literalinclude:: ../../../qiskit/openqasm/superposition_state.qasm
  :language: c++
  :linenos:

.. raw:: html

  <a href="https://qiskit.org"  target="_blank">QISKit</a> example

.. literalinclude:: ../../../qiskit/python/superposition_state.py
  :language: python
  :linenos:

Did you find that the results give a 0 half the time, and a 1 the rest of the time? 
Indeed, much like flipping a fair coin, the results are close to 50/50 
(running on the real device will give less-than-ideal results, due to noise and errors). 

However, quantum randomness is much different. Let's see how.  Run the experiment 
again, but this time with two :math:`H` gates in succession. 
If we consider the :math:`H` gate to be analog to a coin flip, here we would be 
flipping it twice. When you flip a coin twice in a row, you would still expect a 50/50 
distribution. Below is a quantum score for this experiment; run the example.

**Superposition state X-basis**

.. raw:: html

  OpenQasm Input

.. literalinclude:: ../../../qiskit/openqasm/superposition_state_xbasis.qasm
  :language: c++
  :linenos:

.. raw:: html

  <a href="https://qiskit.org"  target="_blank">QISKit</a> example

.. literalinclude:: ../../../qiskit/python/superposition_state_xbasis.py
  :language: python
  :linenos:

This time, the results are surprising. Unlike the classical case, with 
high probability the outcome is not random, but in the :math:`|0\rangle` 
state. Quantum randomness is not simply like a classical random coin flip.
In both of the above experiments, the system (without noise) is in a definite 
state, but only in the first case does it behave randomly. This is because, 
in the first case, via the :math:`H` gate, we make a uniform superposition 
of the ground and excited state, 
:math:`|+\rangle=(|0\rangle+|1\rangle)/\sqrt{2}`, but then follow 
it with a measurement in the computational basis. The act of measurement 
in the computational basis forces the system to be in either the 
:math:`|0\rangle` state or the :math:`|1\rangle` state with an equal 
probability. In the second case, 
we can think of the second :math:`H` gate as being part of the final 
measurement operation; it changes the measurement basis from the 
computational basis to a new basis - which we call the superposition basis, 
or x-basis. The experiment confirms this by giving the result 0, 
showing the system is in the :math:`|+\rangle` superposition state.  

Before we give the math to explain this, let's consider two more experiments. 
The first puts the qubit in the excited state, then applies 
the :math:`H` gate. The score for this is below; run it and you will see
that we get the same 50/50 statistics as the first experiment.  

**Negative superposition state**

.. raw:: html

  OpenQasm Input

.. literalinclude:: ../../../qiskit/openqasm/negative_superposition_state.qasm
  :language: c++
  :linenos:

.. raw:: html

  <a href="https://qiskit.org"  target="_blank">QISKit</a> example

.. literalinclude:: ../../../qiskit/python/negative_superposition_state.py
  :language: python
  :linenos:

The second experiment consists of first preparing the qubit in the excited state,
applying the :math:`H` gate (putting it in a superposition), and then measuring in the 
x-basis (another :math:`H` gate followed by a measurement). Here we find 
with high probability that the system gives outcome 1. This tells us that 
the state just before the x-basis measurement was a superposition that 
was orthogonal to the :math:`|+\rangle` state. By definition, this state has to be 
:math:`|-\rangle=(|0\rangle-|1\rangle)/\sqrt{2}`. 
That is, the :math:`H` gate transforms the computational basis into a new basis, 
the superposition basis, defined by the set :math:`\{|+\rangle, |-\rangle\}`.

**Negative superposition state X-basis**

.. raw:: html

  OpenQasm Input

.. literalinclude:: ../../../qiskit/openqasm/negative_superposition_state_xbasis.qasm
  :language: c++
  :linenos:

.. raw:: html

  <a href="https://qiskit.org"  target="_blank">QISKit</a> example

.. literalinclude:: ../../../qiskit/python/negative_superposition_state_xbasis.py
  :language: python
  :linenos:

The matrix the represents the :math:`H` gate is
 
.. math:: 
  ~~~~~~~~H =\frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}.

Applying this gate to the :math:`|0\rangle` gives 

.. math:: 
  ~~~~~~~~H|0\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}=|+\rangle,

and applying it to the :math:`|1\rangle` gives 

.. math:: 
  ~~~~~~~~H|1\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} 0 \\ 1 \end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}=|-\rangle.
  
These matrices lead directly to the quantum randomness seen above.
You have also learnt about quantum superpositions, and that these superpositions
can have a sign. The main message we would like you to 
take away from this this chapter is:

- a physical system in a definite state can still behave randomly. 

This is the first of the two principles from \ 
`the Quantum World <../001-The_IBM_Qu_Experience/002-The_Quantum_World.html>`__ \ 
section.  This needs to become your new intuition, as it is 
what makes quantum systems different to classical systems.
