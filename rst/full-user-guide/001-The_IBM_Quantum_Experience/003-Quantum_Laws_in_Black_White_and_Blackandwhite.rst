Quantum Laws in Black, White, and Blackandwhite
===============================================

| Quantum laws are, as far as we know, the most fundamental physical
  laws; they are inviolable. Here is our version of quantum physics
  distilled into five key laws\ **.** If the math is new to you, just
  print yourself a copy of these laws and skip them for now; while you
  work through the rest of the tutorial, return to them every now and
  then to see how they tie into what you are learning.

**Quantum is a system like everything else. **

To each physical system there corresponds a Hilbert space (1) of
dimensionality equal to the system's maximum number of reliably
distinguishable states (2).  

**﻿A quantum state is a configuration of the system.**

| Each direction (ray) in the Hilbert space corresponds to a possible
  state of the system (3), with two states being reliably
  distinguishable if and only if their directions are orthogonal (inner
  product is zero).

**A quantum state changes; it naturally wants to evolve, but it can always be undone.**

| Evolution of a closed system is a unitary (4) transformation on its
  Hilbert space.

**Scaling - how parts make a whole.**

| The Hilbert space of a composite system is the tensor product of the
  Hilbert space of the parts (5).

**Quantum measurements are probabilistic.**

| Each possible measurement (6) on a system corresponds to a resolution
  of its Hilbert space into orthogonal subspaces :math:`\{\Pi_j\}` where
  :math:`\sum_j \Pi_j = 1`. On state :math:`|\psi\rangle` the result
  :math:`j` occurs with probability :math:`P(j) = \langle \psi
  |\Pi_j|\psi\rangle` and the state after the measurement is
  :math:`|\psi_j\rangle = \Pi_j |\psi\rangle/\sqrt{P(j)}`.
| ﻿
| These five principles are the foundation for the whole quantum world.
| **Clarifications**

    .. raw:: html

       <div style="text-align: left;">

    .. rubric:: 
       :name: section

    #. A Hilbert space is a linear vector space with complex
       coefficients and inner products :math:`\langle \phi|\psi\rangle =
       \sum_i \phi_{i}^{*}\psi_i`.
    #. For a single qubit, there are two standard orthogonal states
       (*computational basis states*) that are conventionally denoted
        :math:`|0\rangle =\begin{pmatrix}1\\0\end{pmatrix}` and
       :math:`|1\rangle =\begin{pmatrix}0\\1\end{pmatrix}`.
    #. Other qubit states include  :math:`|+\rangle
       =\frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}`,
       :math:`|-\rangle
       =\frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix}`, 
       :math:`|\circlearrowright\rangle
       =\frac{1}{\sqrt{2}}\begin{pmatrix}1\\i\end{pmatrix}` and
       :math:`|\circlearrowleft\rangle
       =\frac{1}{\sqrt{2}}\begin{pmatrix}1\\-i\end{pmatrix}`
    #. *Unitary* means linear and inner-product-preserving.
    #. A two-qubit system can exist in a product state such as
       :math:`|00\rangle` or :math:`|0+\rangle` but also in an
       *entangled* state :math:`(|00\rangle+|11\rangle)/\sqrt{2}`, in
       which neither qubit has a definite state, even though the pair
       together does. 
    #. Measurement causes the system to behave probabilistically and
       forget its pre-measurement state, unless that state happens to
       lie entirely with one of the subspaces :math:`\Pi_j`.

    .. raw:: html

       </div>
