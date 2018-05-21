Quantum Phase Estimation
========================

Quantum phase estimation is one of the most important subroutines in
quantum computation. It serves as a central building block for many
quantum algorithms and implements a measurement for essentially any
`Hermitian
operator <https://en.wikipedia.org/wiki/Hermitian_adjoint>`__. Recall
that a quantum computer initially only permits us to measure individual
qubits. If we want to measure a more complex observable, such as the
energy described by a Hamiltonian :math:`H`, we resort to quantum phase
estimation. The routine prepares an eigenstate of the Hermitian operator
in one register and stores the corresponding eigenvalue in a second
register. 

John von Neumann's measurement scheme
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Quantum phase estimation is a discretization of von Neumann's
prescription to measure a Hermitian observable :math:`H = \sum_j E_j
|\psi_j \rangle \langle \psi_j|`. The scheme that von Neumann
envisioned is the following. We consider a quantum system that supports
the observable :math:`H`, which we want to measure. We assume that we are only
able to measure simpler observables, in our case single qubits, or as in
the original setting the location of a single particle. It is therefore
our goal to reduce the measurement of the complex observable :math:`H` to a
measurement of the simpler observable, e.g. the location. This simple
observable is then referred to as the pointer. To map the complex
observable on to the  simpler one we'll make use of a convenient
observation from quantum mechanics. It is known that the momentum
operator :math:`\hat{p}` generate shifts for single particles. 

|image0|

That is, if we apply the unitary :math:`\exp(- i \hat{p} \lambda)` to some
wave packet :math:`\psi(x)`, then this wave packet will be shifted by
:math:`\lambda` in the positive direction.

| The scheme now assumes that we can apply the unitary evolution
  :math:`\exp(-i H \otimes \hat{p} t )` to both the system and the
  pointer register as illustrated in the following picture

| 
| |image1|\ This picture essentially describes von Neumann"s measurement
  scheme. We now follow the steps and first adjoin an ancilla -- the
  pointer -- which is a continuous quantum variable initialized in the
  state :math:`|0\rangle` (the origin), so that the system+pointer is
  initialized in the state :math:`|\psi\rangle|0\rangle`, where
  :math:`|\psi\rangle` is the initial state of the system. Then we evolve
  according to the new Hamiltonian :math:`K = H\otimes\hat{p}` for a time
  :math:`t`, so the evolution is given by 

:math:`e^{-it H\otimes \hat{p}} = \sum_{j=1}^{2^N}
|\psi_{j}\rangle\langle \psi_{j}|\otimes e^{-itE_j \hat{p}}.`

We now observe the action of this measurement apparatus. Suppose that
:math:`|\psi\rangle` is an
`eigenstate <https://en.wikipedia.org/wiki/Introduction_to_eigenstates>`__
:math:`|\psi_{j}\rangle` of :math:`H`, we find that the system evolves to
:math:`e^{-it H\otimes \hat{p}}|\psi_{j}\rangle|0\rangle =
|\psi_{j}\rangle |x = tE_j\rangle.` A measurement of the
position of the pointer with sufficiently high accuracy will provide an
approximation to :math:`E_j`.

The quantum algorithm
^^^^^^^^^^^^^^^^^^^^^

| To carry out the above operation efficiently on a quantum computer, we
  discretize the pointer using :math:`r` qubits, replacing the continuous
  quantum variable with a :math:`2^r`-dimensional space, where the
  computational basis states :math:`|z\rangle` of the pointer represent
  the basis of momentum eigenstates of the original continuous quantum
  variable. The label :math:`z` is the binary representation of the integers
  :math:`0` through :math:`2^r-1`. In this representation, the discretization of
  the momentum operator becomes

| :math:`\hat{p} = \sum_{j=1}^r 2^{-j}
  \frac{\mathbb{I}-\sigma^z_j}{2}.`
  xx
| With this normalization :math:`\hat{p}|z\rangle =
  \frac{z}{2^r}|z\rangle`. Now the discretized Hamiltonian :math:`K =
  H\otimes \hat{p}` is a sum of terms involving at most :math:`k+1`
  qubits, if :math:`H` is a Hamiltonian involving terms of at most :math:`k`
  qubits. Thus we can simulate the dynamics of :math:`K` using standard
  methods. In terms of the momentum eigenbasis the initial (discretized)
  state of the pointer is written :math:`| x=0\rangle =
  \frac{1}{2^{r/2}}\sum_{z=0}^{2^r-1} |z\rangle`. This state can
  be prepared efficiently on a quantum computer by first initializing
  the qubits of the pointer in the state :math:`|0\rangle \cdots
  |0\rangle` and applying an (inverse) `quantum Fourier
  transform <https://en.wikipedia.org/wiki/Quantum_Fourier_transform>`__.
  Since we have a very simple initial state, the Fourier transform can
  be represented by a product of Hadamard matrices. The discretized
  evolution of the system+pointer now can be written

| :math:`e^{-it  H\otimes \hat{p}}|\psi_{j}\rangle|x=0\rangle =
  \frac{1}{2^{r/2}}\sum_{z=0}^{2^r-1} e^{-iE_j
  zt/2^r}|\psi_{j}\rangle z\rangle.`

| Performing an inverse quantum Fourier transform on the pointer leaves
  the system in the state :math:`|\psi_{j}\rangle\otimes|\phi\rangle`,
  where

:math:`| \phi\rangle  = \sum_{x=0}^{2^r-1} \left(
\frac{1}{2^{r}}\sum_{z=0}^{2^r-1}e^{\frac{2\pi
i}{2^r}\left(x-\frac{E_j t}{2\pi}\right)z} \right)|x\rangle,`

| which is strongly peaked near the location :math:`x = \lfloor
  \frac{E_jt}{2\pi} \rfloor`. To ensure that there are no overflow
  errors we need to choose :math:`t < \frac{2\pi}{\|H\|}`. (We assume
  here, for simplicity, that :math:`H\geq 0`.) It is easy to see that
  actually performing the simulation of :math:`K` for :math:`t=1` is a product of
  :math:`r` simulations of the evolution according to :math:`\frac{1}{2^{r}}
  H\otimes \frac{\mathbb{I}-\sigma^z_k}{2}` for :math:`1, 2, 2^2,
  \ldots, 2^{r-1}` units of time, respectively. This results in the
  general circuit for quantum phase estimation:

|                                       |image2|

In order to implement the full circuit on a quantum computer, we still
need to decompose the controlled unitaries :math:`e^{-i H  \frac{t}{2^k}}` as
well as the inverse quantum Fourier transform denoted by :math:`QFT^{-1}` into
our elementary gates.

Example circuit
^^^^^^^^^^^^^^^

| The example below demonstrates quantum phase estimation for a toy
  single-qubit Hamiltonian :math:`\sigma^x` acting on qubit :math:`Q_2`. Qubit
  :math:`Q_3` serves as a pointer system. In this example the quantum
  Fourier transform on the pointer system is equivalent to the Hadamard
  gate :math:`H` on :math:`Q_3`. The discretized evolution of the
  system+pointer system is described by the CNOT gate. The final
  measurement outcome on the pointer qubit :math:`Q_3` is :math:`0` or :math:`1`
  depending on whether :math:`Q_2` is prepared in the :math:`+1` or :math:`-1`
  eigenstate of :math:`\sigma^x`. In this example, qubit :math:`Q_2` is
  initialized in a state :math:`Z H|0\rangle` which is :math:`-1` eigenvector
  :math:`\sigma^x`. Accordingly, the measurement outcome is :math:`1`. 
  

|
| **Phase Estimation Circuit (-)**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=bc8e23382f4bb64da16c0a4579f9dc8a&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-512686ae13a97aaed71304b5d8194b97.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=bc8e23382f4bb64da16c0a4579f9dc8a&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Phase Estimation Circuit (+)**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=b5a0e7376ded40cd7dc1022e778ebd71&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-4568159e2e0816fb088fec7ee697315f.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=b5a0e7376ded40cd7dc1022e778ebd71&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

.. |image0| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-04%20at%203.38.02%20PMn0sfx8psrw0l766r.png
.. |image1| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-04%20at%203.38.25%20PMf1vr8qjhvh5dygb9.png
.. |image2| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-04%20at%203.38.36%20PMa2xe59tw6hvt2o6r.png

