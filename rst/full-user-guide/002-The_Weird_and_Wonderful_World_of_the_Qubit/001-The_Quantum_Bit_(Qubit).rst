The Quantum Bit (Qubit)
=======================

| In this section you will meet the qubit. You will also see a bit of
  mathematical notation, including some concepts from linear algebra.
| A qubit is a quantum system consisting of two levels, labeled
  :math:`|0\rangle` and :math:`|1\rangle` (here we are using Dirac's bra-ket
  notation), and is represented by a two-dimensional vector space over
  the complex numbers :math:`\mathbb{C}^2`. This means that a qubit takes
  two complex numbers to fully describe it. The computational (or
  standard) basis corresponds to the two levels :math:`|0\rangle` and
  :math:`|1\rangle`, which correspond to the following vectors:
|                                               |image0|
| The qubit does not always have to be in either :math:`|0\rangle` or
  :math:`|1\rangle`; it can be in an arbitrary quantum state, denoted
  :math:`|\psi\rangle`, which can be any *superposition*
  :math:`|\psi\rangle=\alpha |0\rangle + \beta |1\rangle`, of the
  basis vectors. The superposition quantities :math:`\alpha` and :math:`\beta`
  are complex numbers; together they obey
  :math:`|\alpha|^2+|\beta|^2=1`.
| Interesting things happen when quantum systems are measured, or
  observed. Quantum measurement is described by the `Born
  rule <https://en.wikipedia.org/wiki/Born_rule>`__. In particular, if a
  qubit in some state :math:`|\psi\rangle` is measured in the standard
  basis, the result **0** is obtained with probability
  :math:`|\alpha|^2`, and the result **1** is obtained with the
  complementary probability :math:`|\beta|^2`. Interestingly, a quantum
  measurement takes any superposition state of the qubit, and projects
  it to either the state :math:`|0\rangle` or the state :math:`|1\rangle`
  with a probability determined from the parameters of the
  superposition.
| What we have described here is the abstract notion of a qubit. The
  prototype quantum computer you interact with in the IBM Quantum
  Experience uses a physical type of qubit called a *superconducting
  transmon qubit*, which is made from superconducting materials such as
  niobium and aluminum, patterned on a silicon substrate.
| Physically, for this superconducting qubit to behave as the abstract
  notion of the qubit, the device must be at drastically low
  temperatures. In the IBM Quantum Lab, we keep the temperature so cold
  (15 milliKelvin in a dilution refrigerator) that there is no ambient
  noise or heat to excite the superconducting qubit. Once our system has
  gotten cold enough, which takes several days, the superconducting
  qubit reaches equilibrium at the ground state :math:`|0\rangle`. 

To get a sense for what "ground state" means, try running the first
score file below in simulation mode (or look at some cached runs on the
real device). Here, the qubit is initially prepared in the ground state
:math:`|0\rangle`, then is followed by the standard measure. From your
execution results, you should find in the ideal case (and with very high
probability for the cached runs) that the qubit is still in the ground
state. In the real device runs, you can observe that there is some
error, with some shots giving a :math:`|1\rangle` instead, which is due to
imperfect measurements and some residual heating of the qubit. 

|image1|

| The output for every score you run will be in the My Scores tab. Click
  the little bar graph icon next to the time stamp for your quantum
  score to see the results (if the results are not yet ready, or if
  there has been an error, you will see a yellow or red symbol on the
  bar graph icon). This will take you to the Results screen, where you
  can view the outcomes.


|
| **1Q Measurement**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=f03e4cfa53ccf70b3bea5e0955b6f458&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-f03e4cfa53ccf70b3bea5e0955b6f458.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=f03e4cfa53ccf70b3bea5e0955b6f458&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>


.. |image0| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-01%20at%209.56.21%20AMw7bbvnq72lprdx6r.png
.. |image1| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/ground_stategoftc7s5fwkrcnmi.png

