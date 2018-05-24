Deutsch-Jozsa Algorithm
=======================

The Deutsch-Jozsa algorithm was the first to show a separation between
the quantum and classical difficulty of a problem. This algorithm
demonstrates the significance of allowing quantum amplitudes to take
both positive and negative values, as opposed to classical probabilities
that are always non-negative.

| 
| The Deutsch-Jozsa problem is defined as follows. Consider a function
  :math:`f(x)` that takes as input :math:`n`-bit strings :math:`x` and returns :math:`0`
  or :math:`1`. Suppose we are promised that :math:`f(x)` is either a
  **constant** function that takes the same value :math:`c\in \{0,1\}` on
  all inputs :math:`x`, or a **balanced** function that takes each value
  :math:`0` and :math:`1` on exactly half of the inputs. The goal is to decide
  whether :math:`f` is constant or balanced by making as few function
  evaluations as possible. Classically, it requires :math:`2^{n-1}+1`
  function evaluations in the worst case. Using the Deutsch-Jozsa
  algorithm, the question can be answered with just one function
  evaluation. In the quantum world the function :math:`f` is specified by an
  oracle circuit :math:`U_f` (see the previous section on Grover's
  algorithm, such that :math:`U_f |x\rangle =(-1)^{f(x)} |x\rangle`).

| 
| To understand how the Deutsch-Jozsa algorithm works, let us first
  consider a typical interference experiment: a particle that behaves
  like a wave, such as a photon, can travel from the source to an array
  of detectors by following two or more paths simultaneously. The
  probability of observing the particle will be concentrated at those
  detectors where most of the incoming waves arrive with the same phase.
| |image0|\ Imagine that we can set up an interference experiment as
  above, with :math:`2^n` detectors and :math:`2^n` possible paths from the
  source to each of the detectors. We shall label the paths and the
  detectors with :math:`n`-bit strings :math:`x` and :math:`y` respectively. Suppose
  further that the phase accumulated along a path :math:`x` to a detector
  :math:`y` equals :math:`C(-1)^{f(x)+x\cdot y}`, where

:math:`x\cdot y=\sum_{i=1}^n x_i y_i`

| is the binary inner product and :math:`C` is a normalizing coefficient.
  The probability to observe the particle at a detector :math:`y` can be
  computed by summing up amplitudes of all paths :math:`x` arriving at :math:`y`
  and taking the absolute value squared:

| :math:`\mathrm{Pr}(y)=| C\sum_x (-1)^{f(x)+x\cdot y} |^2`

| Normalization condition :math:`\sum_y \mathrm{Pr}(y)=1` then gives
  :math:`C=2^{-n}`. Let us compute the probability :math:`\mathrm{Pr}(y=0^n)`
  of observing the particle at the detector :math:`y=0^n` (all zeros
  string). We have :math:`\mathrm{Pr}(y=0^n)=| 2^{-n}\sum_x (-1)^{f(x)}
  |^2`
| If :math:`f(x)=c` is a constant function, we get
  :math:`\mathrm{Pr}(y=0^n)=|(-1)^c |^2 =1`. However, if :math:`f(x)` is a
  balanced function, we get :math:`\mathrm{Pr}(y=0^n)=0`, since all the
  terms in the sum over :math:`x` cancel each other.

| We can therefore determine whether :math:`f` is constant or balanced with
  certainty by running the experiment just once.
| Of course, this experiment is not practical since it would require an
  impossibly large optical table! However, we can simulate this
  experiment on a quantum computer with just :math:`n` qubits and access to
  the oracle circuit :math:`U_f`. Indeed, consider the following algorithm:
| Step 1. Initialize :math:`n` qubits in the all-zeros state
  :math:`|0,\ldots,0\rangle`.
| Step 2. Apply the Hadamard gate :math:`H` to each qubit.
| Step 3. Apply the oracle circuit :math:`U_f`.
| Step 4. Repeat Step 2.
| Step 5. Measure each qubit. Let :math:`y=(y_1,\ldots,y_n)` be the list
  of measurement outcomes.
| We find that :math:`f` is a constant function if :math:`y` is the all-zeros
  string. Why does this work? Recall that the Hadamard gate :math:`H` maps
  :math:`|0\rangle` to the uniform superposition of :math:`|0\rangle` and
  :math:`|1\rangle`. Thus the state reached after Step 2 is :math:`2^{-n/2}
  \sum_x |x\rangle`, where the sum runs over all :math:`n`-bit strings.
  The oracle circuit maps this state to :math:`2^{-n/2} \sum_x (-1)^{f(x)}
  |x\rangle`. Finally, let us apply the layer of Hadamards at Step 4.
  It maps a basis state :math:`|x\rangle` to a superposition
  :math:`2^{-n/2}\sum_y (-1)^{x\cdot y} |y\rangle`. Thus the state
  reached after Step 4 is :math:`|\psi\rangle =\sum_y \psi(y)
  |y\rangle`, where :math:`\psi(y)=2^{-n}\sum_x (-1)^{f(x)+x\cdot
  y}`.

| This is exactly what we need for the interference experiment described
  above. The final measurement at Step 5 plays the role of detecting the
  particle. As was shown above, the probability to measure :math:`y=0^n` at
  Step 5 is one if :math:`f` is a constant function and zero if :math:`f` is a
  balanced function. Thus we have solved the Deutsch-Jozsa problem with
  certainty by making just one function evaluation.

Example circuits
^^^^^^^^^^^^^^^^

| Suppose :math:`n=3` and :math:`f(x)=x_0 \oplus x_1 x_2`. This function is
  balanced since flipping the bit :math:`x_0` flips the value of :math:`f(x)`
  regardless of :math:`x_1,x_2`. To run the Deutsch-Jozsa algorithm we
  need an explicit description of the oracle circuit :math:`U_f` as a
  sequence of quantum gates. To this end we need a :math:`Z_0` gate such
  that :math:`Z_0|x\rangle =(-1)^{x_0} |x\rangle` and a controlled-Z
  gate :math:`CZ_{1,2}` such that :math:`CZ_{1,2} |x\rangle =(-1)^{x_1x_2}
  |x\rangle`.  Using basic circuit identities (see the *Basic Circuit
  Identities and Larger Circuits* section), one can realize the
  controlled-Z gate as a CNOT sandwiched between two Hadamard gates.
 
  
|
| **DJ N=3 Example**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=dda7fb160013ea06bc75d0204439c9a6&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-570b68405ba63ca75c724d3f40aa2010.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=dda7fb160013ea06bc75d0204439c9a6&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **DJ N=3 Constant**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=1f234d4750fe47817393d8e1c8f8943d&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-4568159e2e0816fb088fec7ee6970100.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=1f234d4750fe47817393d8e1c8f8943d&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>
   

.. |image0| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/interferencex663kgbfsoc1sjor.jpg

