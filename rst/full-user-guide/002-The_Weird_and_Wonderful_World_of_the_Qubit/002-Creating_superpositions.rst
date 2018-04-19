Creating superpositions
=======================

Up to this point, nothing is different from a classical bit. 
To go beyond classical bits we must explore what it means to make a superposition. 
The operation for generating a superposition 
is the Hadamard gate, :math:`H`. In the Composer, this is the
blue gate labeled :math:`H`.

The simple score to make a superposition is given below. It starts with placing 
the :math:`H` gate on one of the qubits (which starts in the :math:`|0\rangle` state) 
and a standard measurement. Go run it. 

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

Did you find that the results give half the time a 0 and half the time a 1? 
Indeed, much like flipping a fair coin, the results are close to 50/50 
with the non-ideality due to shot noise and errors (if you ran it on 
a real experiment). 
You would not be alone thinking the :math:`H` gate is is like flipping a 
fair coin (it is the randomness that we all experience).

However, quantum randomness is much different. Lets see how.  Let's 
run the experiment again, but this time with two :math:`H` gates in succession. 
If we consider the :math:`H` gate to be analog to a coin flip, here we would be 
flipping it twice. Flipping a coin twice you would still expect a 50/50 
distribution. Below is a quantum score for this experiment, go run it 
and see what you get. 

**Superposition state X basis**

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
computational basis to a new basis (which we will call the superposition basis 
or x-basis) and the 
experiment confirms by giving result 0 that the system is in the :math:`|+\rangle` 
superposition state.  

Before we give the math to understand this lets consider two more experiments. 
The first puts the qubit first in the excited state and then applies 
the :math:`H` gate. The score for this is below and running it on the
experiment we find that we get the same 50/50 statistics as the first experiment.  

**Negative Superposition state**

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

The final experiment consists of first preparing the qubit in the excited state 
and then applying the 
:math:`H` gate (putting it in a superposition) and then measuring in the 
x-basis (another :math:`H` gate followed by a measurement). Here we find 
with high probability that the system gives outcome 1. This tells us that 
the state just before the x-basis measurement was a superposition that 
was orthogonal to the :math:`|+\rangle` state. By definition this state has to be 
:math:`|-\rangle=(|0\rangle-|1\rangle)/\sqrt{2}`. 
That is the :math:`H` gate transforms the computational basis into a new basis, 
the superposition basis, defined by the set :math:`\{|+\rangle, |-\rangle\}`.

**Negative Superposition state X basis**

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
  ~~~~~~~~H|0\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}=|+\rangle

and applying it to the :math:`|1\rangle` gives 

.. math:: 
  ~~~~~~~~H|1\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} 0 \\ 1 \end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}=|-\rangle
  
From these it is simple to understand the above four experiments and you have 
now learnt about quantum randomness. You have also learnt about quantum superpositons 
and that these superpositions can have a sign. The main message we would like you to 
take away from this this chapter is:

- a physical system in a perfectly definite state can still behave randomly. 

This is the first of the two principles from \ 
`the Quantum World <../001-The_IBM_Qu_Experience/002-The_Quantum_World.html>`__ \ 
section that we believe needs to become your new intuition and 
what makes quantum systems different to classical systems.