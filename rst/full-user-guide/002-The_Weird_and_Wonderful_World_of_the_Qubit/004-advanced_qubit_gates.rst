Advanced single qubit gates
===========================

Ok we are ready to hit the advance button. Go ahead and click the tick box. 
Doing this you should find that three orange gates :math:`\{u1,u2,u3\}` (and some 
more stuff we will touch on later) appear. These are the three physical single qubit 
gates of the IBM Q Experience which take in one, two and three parameters respectively.
These are the main single qubit gates and the rest you have learnt about are 
just special cases of these. 

Another convenient representation of a single qubit state is

.. math:: 
  ~~~~~~~~|\psi\rangle = \cos(\theta/2)|0\rangle + \sin(\theta/2)e^{i\phi}|1\rangle

where :math:`0 \leq \phi <2\pi`  and :math:`0\leq \theta \leq \pi`. From this it is clear that 
there is a one-to-one correspondence between qubit states (:math:`\mathbb{C}^2`) and the points on the 
surface of a unit sphere (:math:`\mathbb{R}^3`). This is called the Bloch sphere representation of a qubit state
(which will be discussed later)

As mentioned before single-qubit gates are represented by a :math:`2\times 2` unitary matrix :math:`U`. 
The action of the quantum gate is found by multiplying the matrix representing the gate with 
the vector which represents the quantum state.

.. math:: 
  ~~~~~~~~|\psi'\rangle = U|\psi\rangle,

A general unitary must be able to take the :math:`|0\rangle` to the above state and :math:`U^\dagger U = I`. 
That is,

.. math:: 
  ~~~~~~~~U = \begin{pmatrix} \cos(\theta/2) & -e^{i\lambda}\sin(\theta/2) \\ e^{i\phi}\sin(\theta/2) 
  & e^{i\lambda+i\phi}\cos(\theta/2) \end{pmatrix}

This is the most general form of a single qubit unitary.

The first physical gate, :math:`u1` is the phase gate and is given by  

.. math:: 
  ~~~~~~~~u1(\lambda) = U(0,0,\lambda) = \begin{pmatrix} 1 & 0 \\ 0 
  & e^{i\lambda} \end{pmatrix}.

This gate allows us to program a continuous quantum phase :math:`\lambda`. In the previous sections the :math:`T`, 
:math:`T^\dagger`, :math:`S`, :math:`S^\dagger` and :math:`Z`  are made using this gate. In the IBM Q Experience 
this is implemented as a frame change and takes zero time. 

The second gate is :math:`u2` which has the form

.. math:: 
  ~~~~~~~~u2(\phi,\lambda) = U(\pi/2,\phi,\lambda) = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & -e^{i\lambda} \\ e^{i\phi}
  & e^{i\lambda+i\phi} \end{pmatrix}.

From this gate the Hadamard is done by :math:`H= U_2(0,\pi)`.  IBM Q Experience 
this is implemented by a pre and post frame change and a :math:`X_{\pi/2}` pulse.

The 3rd gate is :math:`u3` which is just :math:`u3(\theta,\phi,\lambda) = U(\theta,\phi,\lambda)` and it is 
implemented using three frame changes and two :math:`X_{\pi/2}` pulses. 