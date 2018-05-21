Grover's Algorithm
==================

We are now in a good place to discuss our first quantum algorithms and
subroutines. Let's begin with `Grover's search
algorithm <http://arxiv.org/abs/quant-ph/9605043>`__ and the *amplitude
amplification trick*.

You have likely heard that one of the many advantages a quantum computer
has over a classical computer is its superior speed searching databases.
Grover's algorithm demonstrates this capability. This algorithm can
speed up an unstructured search problem quadratically, but its uses
extend beyond that; it can serve as a general trick or subroutine to
obtain quadratic run time improvements for a variety of other
algorithms. This is called the amplitude amplification trick. But before
we start the simulations, let's look at the unstructured search problem.

Unstructured search
^^^^^^^^^^^^^^^^^^^

Suppose you are given a large list of :math:`N` items. Among these items
there is one item with a unique property that we wish to locate; we will
call this one the winner :math:`w`. Think of each item in the list as a box
of a particular color. Say all items in the list are gray except the
winner :math:`w`, which is pink.

| |image0|

To find the pink box -- the *marked item* -- using classical
computation, one would have to check on average :math:`N/2` of these boxes,
and in the worst case, all :math:`N` of them. On a quantum computer,
however, we can find the marked item in roughly :math:`\sqrt{N}` steps with
Grover's amplitude amplification trick. It was proven (even before
Grover's algorithm was discovered!) that this speedup is in fact the
most we can hope for [`Bennett,
1997 <http://arxiv.org/abs/quant-ph/9701001>`__]. A quadratic speedup is
indeed a substantial time-saver for finding marked items in long lists.
Additionally, the algorithm does not use the list's internal structure,
which makes it *generic;* this is why it immediately provides a
quadratic quantum speed-up for many classical problems.  

The Oracle
^^^^^^^^^^

| How will the list items be provided to the quantum computer? A common
  way to encode such a list is in terms of a function :math:`f` which returns
  :math:`f(x) = 0` for all unmarked items :math:`x` and :math:`f(w) = 1` for the winner.
  To use a quantum computer for this problem, we must provide the items
  in superposition to this function, so we encode the function into a
  unitary matrix called an *oracle*. First we choose a binary encoding
  of the items :math:`x, w \in \{0,1\}^n` so that :math:`N = 2^n`; now we can
  represent it in terms of qubits on a quantum computer. Then we define
  the oracle matrix :math:`U_f` to act on any of the simple, standard basis
  states :math:`| x \rangle` by

| :math:`U_f | x \rangle = (-1)^{f(x)}  |  x \rangle.`

We see that if :math:`x` is an unmarked item, the oracle does nothing to the
state. However, when we apply the oracle to the basis state :math:`| w
\rangle`, it maps :math:`U_f | w \rangle = -| w \rangle`.
Geometrically, this unitary matrix corresponds to a reflection about the
origin for the marked item in an :math:`N = 2^n` dimensional vector space.

Amplitude amplification
^^^^^^^^^^^^^^^^^^^^^^^

So how does the algorithm work? Before looking at the list of items, we
have no idea where the marked item is. Therefore, any guess of its
location is as good as any other, which can be expressed in terms of a
quantum state called a *uniform superposition*:

:math:`|s \rangle = \frac{1}{\sqrt{N}} \sum_{x = 0}^{N -1} | x
\rangle.`

| If at this point we were to measure in the standard basis :math:`\{ | x
  \rangle \}`, this superposition would collapse, according to the
  fifth quantum law, to any one of the basis states with the same
  probability of :math:`\frac{1}{N} = \frac{1}{2^n}`. Our chances of
  guessing the right value :math:`w` is therefore :math:`1` in :math:`2^n`, as could be
  expected. Hence, on average we would need to try about :math:`N = 2^n` times
  to guess the correct item.

Enter the procedure called amplitude amplification, which is how a
quantum computer significantly enhances this probability. This procedure
stretches out (amplifies) the amplitude of the marked item, which
shrinks the other items' amplitude, so that measuring the final state
will return the right item with near-certainty. 

This algorithm has a nice geometrical interpretation in terms of two
reflections, which generate a rotation in a two-dimensional plane. The
only two special states we need to consider are the winner :math:`| w
\rangle` and the uniform superposition :math:`| s \rangle`. These two
vectors span a two-dimensional plane in the vector space
:math:`\mathbb{C}^N.` They are not quite perpendicular because :math:`| w
\rangle` occurs in the superposition with amplitude :math:`N^{-1/2}` as well.
We can, however, introduce an additional state :math:`|s'\rangle` that is in
the span of these two vectors, which is perpendicular to :math:`| w \rangle`
and is obtained from :math:`|s \rangle` by removing :math:`| w \rangle` and
rescaling. 

| **step 0** The amplitude amplification procedure starts out in the
  uniform superposition :math:`| s \rangle`.  (The uniform superposition is
  easily constructed from :math:`| s \rangle = H^{\otimes n} | 0
  \rangle^n`, as was shown in a previous section.) At :math:`t = 0` the
  initial state is :math:`| \psi_0 \rangle =   |s \rangle`.

| |image1|

| The left graphic corresponds to the two-dimensional plane spanned by
  :math:`|w\rangle, |s\rangle`. The right graphic is a bar graph of the
  amplitudes of the state :math:`| \psi_t \rangle` for the case :math:`N = 2^2 =
  4`. The average amplitude is indicated by a dashed line.

| **step 1** We apply the oracle reflection :math:`U_f` to the state :math:`U_f |
  \psi_t \rangle =  | \psi_{t'} \rangle`.

| |image2|

Geometrically this corresponds to a reflection of the state
:math:`|\psi_t\rangle` about :math:`-|w\rangle`. This transformation means
that the amplitude in front of the :math:`|w\rangle` state becomes negative,
which in turn means that the average amplitude has been lowered.

| **step 2** We now apply an additional reflection :math:`U_s` about the
  state :math:`|s\rangle`. In the
  `bra-ket <https://en.wikipedia.org/wiki/Bra%E2%80%93ket_notation>`__
  notation this reflection is written :math:`U_s = 2|s\rangle\langle s| -
  \mathbb{1}`. This transformation maps the state to :math:`U_s |
  \psi_{t'} \rangle` and completes the transformation
  :math:`|\psi_{t+1}\rangle = U_s U_f | \psi_t \rangle`. 

| |image3|

Two reflections always correspond to a rotation. The transformation
:math:`U_s U_f` rotates the initial state :math:`|s\rangle` closer towards the
winner :math:`|w\rangle`. The action of the reflection :math:`U_s` in the
amplitude bar diagram can be understood as a reflection about the
average amplitude. Since the average amplitude has been lowered by the
first reflection, this transformation boosts the negative amplitude of
:math:`|w\rangle` to roughly three times its original value, while it
decreases the other amplitudes. We then go to **step 1** to repeat the
application. This procedure will be repeated several times to zero in on
the winner. 

| After :math:`t` steps the state will have transformed to

| :math:`| \psi_t \rangle = (U_s U_f)^t  | \psi_0 \rangle.` 

| How many times do we need to apply the rotation? It turns out that
  roughly :math:`\sqrt{N}` rotations suffice. This becomes clear when looking
  at the amplitudes of the state :math:`| \psi_t \rangle`. We can see that
  the amplitude of :math:`| w \rangle` grows linearly with the number of
  applications :math:`\sim t N^{-1/2}`. However, since we are dealing with
  amplitudes and not probabilities, the vector space's dimension enters
  as a square root. Therefore it is the amplitude, and not just the
  probability, that is being amplified in this procedure.

|                                                 |image4|

Example circuits
^^^^^^^^^^^^^^^^

| Let us now examine a simple example. The smallest circuit for which
  this can be implemented involves 2 qubits, i.e. :math:`N = 2^2`, which means
  there are four possible oracles :math:`U_f`, one for each choice of the
  winner. The first part of this example creates the uniform
  superposition. The second part tags the state with :math:`U_f`, which is
  made from a control-Z gate, made from a CNOT (as described in the last
  section). The final part of the circuit performs :math:`U_s`. 

|
| **Grover N=2 A=00**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=ac042c16f1d2bf7312503e842e7ffbcc&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-d9c40f27d67d4bf722209faa34a8fd1c.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=ac042c16f1d2bf7312503e842e7ffbcc&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Grover N=2 A=01**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=34bf6d8078127a4cbb85dcba18d71547&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-0eb40f5d1eed7b2d8fd23c2c8771e941.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=34bf6d8078127a4cbb85dcba18d71547&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Grover N=2 A=10**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=e554e35d344f1e346c3b7cd30c5d1939&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-ac12517d7526a77d19ce104d971bbd01.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=e554e35d344f1e346c3b7cd30c5d1939&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Grover N=2 A=11**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=764735cc22581811f9f382d3b3c644f0&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-cab6cbd8d09fa9a72bd276d9c2c22376.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=764735cc22581811f9f382d3b3c644f0&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>



.. |image0| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Picture1zdnvcphw1b07wrk9.png
.. |image1| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Picture15h8emcr7mucy2e29.png
.. |image2| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Picture1fj26kfen5xrsh5mi.png
.. |image3| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Picture1j1gz5ve3zwyd5cdi.png
.. |image4| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-04%20at%201.50.25%20AM0qbyzkc53sj1yvi.png

