Deutsch-Jozsa Algorithm
=======================

The Deutsch-Jozsa algorithm was the first to show a separation between
the quantum and classical difficulty of a problem. This algorithm
demonstrates the significance of allowing quantum amplitudes to take
both positive and negative values, as opposed to classical probabilities
that are always non-negative.

| 
| The Deutsch-Jozsa problem is defined as follows. Consider a function
  $$f(x)$$ that takes as input $$n$$-bit strings $$x$$ and returns $$0$$
  or $$1$$. Suppose we are promised that $$f(x)$$ is either a
  **constant** function that takes the same value $$c\\in \\{0,1\\}$$ on
  all inputs $$x$$, or a **balanced** function that takes each value
  $$0$$ and $$1$$ on exactly half of the inputs. The goal is to decide
  whether $$f$$ is constant or balanced by making as few function
  evaluations as possible. Classically, it requires $$2^{n-1}+1$$
  function evaluations in the worst case. Using the Deutsch-Jozsa
  algorithm, the question can be answered with just one function
  evaluation. In the quantum world the function $$f$$ is specified by an
  oracle circuit $$U\_f$$ (see the previous section on Grover's
  algorithm, such that $$U\_f \|x\\rangle =(-1)^{f(x)} \|x\\rangle$$).

| 
| To understand how the Deutsch-Jozsa algorithm works, let us first
  consider a typical interference experiment: a particle that behaves
  like a wave, such as a photon, can travel from the source to an array
  of detectors by following two or more paths simultaneously. The
  probability of observing the particle will be concentrated at those
  detectors where most of the incoming waves arrive with the same phase.
| |image0|\ Imagine that we can set up an interference experiment as
  above, with $$2^n$$ detectors and $$2^n$$ possible paths from the
  source to each of the detectors. We shall label the paths and the
  detectors with $$n$$-bit strings $$x$$ and $$y$$ respectively. Suppose
  further that the phase accumulated along a path $$x$$ to a detector
  $$y$$ equals $$C(-1)^{f(x)+x\\cdot y}$$, where

$$x\\cdot y=\\sum\_{i=1}^n x\_i y\_i$$

| is the binary inner product and $$C$$ is a normalizing coefficient.
  The probability to observe the particle at a detector $$y$$ can be
  computed by summing up amplitudes of all paths $$x$$ arriving at $$y$$
  and taking the absolute value squared:

| $$\\mathrm{Pr}(y)=\| C\\sum\_x (-1)^{f(x)+x\\cdot y} \|^2$$

| Normalization condition $$\\sum\_y \\mathrm{Pr}(y)=1$$ then gives
  $$C=2^{-n}$$. Let us compute the probability $$\\mathrm{Pr}(y=0^n)$$
  of observing the particle at the detector $$y=0^n$$ (all zeros
  string). We have $$\\mathrm{Pr}(y=0^n)=\| 2^{-n}\\sum\_x (-1)^{f(x)}
  \|^2$$
| If $$f(x)=c$$ is a constant function, we get
  $$\\mathrm{Pr}(y=0^n)=\|(-1)^c \|^2 =1$$. However, if $$f(x)$$ is a
  balanced function, we get $$\\mathrm{Pr}(y=0^n)=0$$, since all the
  terms in the sum over $$x$$ cancel each other.

| We can therefore determine whether $$f$$ is constant or balanced with
  certainty by running the experiment just once.
| Of course, this experiment is not practical since it would require an
  impossibly large optical table! However, we can simulate this
  experiment on a quantum computer with just $$n$$ qubits and access to
  the oracle circuit $$U\_f$$. Indeed, consider the following algorithm:
| Step 1. Initialize $$n$$ qubits in the all-zeros state
  $$\|0,\\ldots,0\\rangle$$.
| Step 2. Apply the Hadamard gate $$H$$ to each qubit.
| Step 3. Apply the oracle circuit $$U\_f$$.
| Step 4. Repeat Step 2.
| Step 5. Measure each qubit. Let $$y=(y\_1,\\ldots,y\_n)$$ be the list
  of measurement outcomes.
| We find that $$f$$ is a constant function if $$y$$ is the all-zeros
  string. Why does this work? Recall that the Hadamard gate $$H$$ maps
  :math:`|0\rangle` to the uniform superposition of :math:`|0\rangle` and
  :math:`|1\rangle`. Thus the state reached after Step 2 is $$2^{-n/2}
  \\sum\_x \|x\\rangle$$, where the sum runs over all $$n$$-bit strings.
  The oracle circuit maps this state to $$2^{-n/2} \\sum\_x (-1)^{f(x)}
  \|x\\rangle$$. Finally, let us apply the layer of Hadamards at Step 4.
  It maps a basis state $$\|x\\rangle$$ to a superposition
  $$2^{-n/2}\\sum\_y (-1)^{x\\cdot y} \|y\\rangle$$. Thus the state
  reached after Step 4 is $$\|\\psi\\rangle =\\sum\_y \\psi(y)
  \|y\\rangle$$, where $$\\psi(y)=2^{-n}\\sum\_x (-1)^{f(x)+x\\cdot
  y}$$.

| This is exactly what we need for the interference experiment described
  above. The final measurement at Step 5 plays the role of detecting the
  particle. As was shown above, the probability to measure $$y=0^n$$ at
  Step 5 is one if $$f$$ is a constant function and zero if $$f$$ is a
  balanced function. Thus we have solved the Deutsch-Jozsa problem with
  certainty by making just one function evaluation.

Example circuits
^^^^^^^^^^^^^^^^

| Suppose $$n=3$$ and $$f(x)=x\_0 \\oplus x\_1 x\_2$$. This function is
  balanced since flipping the bit $$x\_0$$ flips the value of $$f(x)$$
  regardless of $$x\_1,x\_2$$. To run the Deutsch-Jozsa algorithm we
  need an explicit description of the oracle circuit $$U\_f$$ as a
  sequence of quantum gates. To this end we need a $$Z\_0$$ gate such
  that $$Z\_0\|x\\rangle =(-1)^{x\_0} \|x\\rangle$$ and a controlled-Z
  gate $$CZ\_{1,2}$$ such that $$CZ\_{1,2} \|x\\rangle =(-1)^{x\_1x\_2}
  \|x\\rangle$$.  Using basic circuit identities (see the *Basic Circuit
  Identities and Larger Circuits* section), one can realize the
  controlled-Z gate as a CNOT sandwiched between two Hadamard gates.

.. |image0| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/interferencex663kgbfsoc1sjor.jpg

