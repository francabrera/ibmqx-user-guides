The Quantum Bit (Qubit)
=======================

In this section you will meet the qubit. You will also see a bit of
mathematical notation, including some concepts from linear algebra.
A qubit is a quantum system consisting of two levels, labeled
:math:`|0\rangle` and :math:`|1\rangle` (here we are using Dirac's bra-ket
notation). It is represented by a two-dimensional vector space over
the complex numbers :math:`\mathbb{C}^2`. This means that a qubit takes
two complex numbers to fully describe it. The computational (or
standard) basis corresponds to the two levels :math:`|0\rangle` and
:math:`|1\rangle`, which correspond to the following vectors:

.. math:: 
  ~~~~~~~~|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix} ~~~~ |1\rangle =\begin{pmatrix} 0 \\ 1 \end{pmatrix}

The qubit does not always have to be in either :math:`|0\rangle` or
:math:`|1\rangle`; it can be in an arbitrary quantum state, denoted
:math:`|\psi\rangle`, which can be any *superposition*
:math:`|\psi\rangle=\alpha |0\rangle + \beta |1\rangle` of the
basis vectors. The superposition quantities :math:`\alpha` and :math:`\beta`
are complex numbers; together they obey
:math:`|\alpha|^2+|\beta|^2=1`.

Interesting things happen when quantum systems are measured, or
observed. Quantum measurement is described by the `Born
rule <https://en.wikipedia.org/wiki/Born_rule>`__. In particular, if a
qubit in some state :math:`|\psi\rangle` is measured in the standard
basis, the result **0** is obtained with probability
:math:`|\alpha|^2`, and the result **1** is obtained with the
complementary probability :math:`|\beta|^2`. Interestingly, a quantum
measurement takes any superposition state of the qubit, and projects
it to either the state :math:`|0\rangle` or the state :math:`|1\rangle`,
with a probability determined from the parameters of the
superposition.

What we have described here is the abstract notion of a qubit. The
prototype quantum computer you interact with in the IBM Q
Experience uses a physical type of qubit called a *superconducting
transmon qubit*, which is made from superconducting materials such as
niobium and aluminum, patterned on a silicon substrate. Physically, for this 
superconducting qubit to behave as the abstract
notion of the qubit, the device must be at drastically low
temperatures. In the IBM Quantum Lab, we keep the temperature so cold
(15 milliKelvin in a dilution refrigerator) that there is no ambient
noise or heat to excite the superconducting qubit. Once our system has
gotten cold enough, which takes several days, the superconducting
qubit reaches equilibrium at the ground state :math:`|0\rangle`. 

To get a sense for what "ground state" means, try running the first
score file below in simulation mode (or look at some cached runs on the
real device). Here, the qubit is initially prepared in the ground state
:math:`|0\rangle`, then is followed by the standard measurement. From your
execution results, you should find in the simulation mode (and with very high
probability for runs using the real device) that the qubit is still in the ground
state. Any errors in the real device are due to imperfect measurements and/or residual heating of the qubit. 

**Single-Qubit Measurement**

.. raw:: html

  OpenQasm Input

.. literalinclude:: ../../../qiskit/openqasm/single_q_measurement.qasm
  :language: c++
  :linenos:

.. raw:: html

  <a href="https://qiskit.org"  target="_blank">QISKit</a> example

.. literalinclude:: ../../../qiskit/python/single_q_measurement.py
  :language: python
  :linenos:

As you may have guessed, we need to be able to put the qubit in other states. 
To do this, we require the concept of a *quantum gate*.  A single-qubit quantum gate 
is a :math:`2 \times 2` `unitary matrix <https://en.wikipedia.org/wiki/Unitary_matrix>`__
(since quantum gates must be reversible and preserve probability
amplitudes, the matrices must be unitary). The quantum state :math:`|\psi'\rangle`
after the action of the gate is found by multiplying the 
original quantum state by the gate :math:`|\psi'\rangle=U|\psi\rangle`. Here 
:math:`U` represents the gate.

The simplest quantum gate is the bit-flip gate, which we denote by :math:`X`. It takes
:math:`|0\rangle\rightarrow X|0\rangle=|1\rangle`; in other words, it flips the zero 
to a one, or vice versa. This is similar to a classical NOT gate and has a matrix 
representation of 

.. math:: 
  ~~~~~~~~X =\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.

In the Composer it is given by a green gate with a X in the middle (see the example 
score file below). Try running it. Did you find that, unlike in the
example above, the qubit ended up in the excited state :math:`|1\rangle` 
(with high probability if you used the real device)? 

**Excited State**

.. raw:: html

  OpenQasm Input

.. literalinclude:: ../../../qiskit/openqasm/excited_state.qasm
  :language: c++
  :linenos:

.. raw:: html

  <a href="https://qiskit.org"  target="_blank">QISKit</a> example

.. literalinclude:: ../../../qiskit/python/excited_state.py
  :language: python
  :linenos:
