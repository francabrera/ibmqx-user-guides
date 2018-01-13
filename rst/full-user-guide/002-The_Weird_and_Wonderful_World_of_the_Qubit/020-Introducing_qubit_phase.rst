Introducing qubit phase
=======================

| Now that we have the :math:`|0\rangle` and :math:`|1\rangle` states under
  our belt, let's explore superposition, which is the concept that
  adding quantum states together (similar to overlaying two waves)
  results in a new quantum state. To make superpositions, we will expand
  our set of gates to include :math:`\{H, S, S^\dagger\}`. In the Quantum
  Composer, these are the blue set of gates. They are represented by the
  matrices 
|                        |image0|
| In the first score below, we apply :math:`H`, known as the Hadamard gate,
  on one of the qubits that has been prepared in the
  :math:`|0\rangle` state; we then follow up with the standard
  measurement. Run the circuit and observe the result. The qubit should
  spend half its time in the :math:`|0\rangle` state and the other half in
  the :math:`|1\rangle` state. Before the measurement forced the qubit to
  choose a final state, the qubit was in both states at once. This
  superposition effect is often over-emphasized, and has become part of
  an often-misused analogy that a quantum computer is more powerful
  because it somehow "does everything at once."

So what is happening mathematically? 

When we apply the :math:`H` gate to :math:`|0\rangle`, we make the state
:math:`|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)` (we've
performed a size-2 discrete Fourier transform). This is the standard
representation of a superposition state. We can define the state
:math:`|-\rangle = \frac{1}{\sqrt{2}}(|0\rangle -|1\rangle)`, which
with :math:`|+\rangle` forms a new basis called the *diagonal* (or
conjugate) basis. It is made using the second circuit below. The :math:`H`
creates the above superposition, and then the :math:`Z`, which previously
did nothing, now flips the phase (:math:`|1\rangle` to :math:`-|1\rangle`).
When you run this circuit you will find that, like before, the outcomes
are equal. Different states give the same outcomes!

To tell the difference between these states, we need to measure in the
diagonal basis. In our experiments we cannot physically change the
measurement; however, we can effectively change the measurement using
gates before measurement. To measure in the diagonal basis, the standard
basis (:math:`Z`) is rotated to the diagonal basis (:math:`X`) with a Hadamard
gate before the measurement. 

| |image1|                                                  

Try Superposition (+) X Measurement and Superposition (-) X Measurement
below in simulation. You should find that 100% of the time the outcome
is 0 and 1 respectively. That is, if we make a measurement in the
standard basis, the outcome is completely uniform -- but in the diagonal
basis, it has deterministic outcome.  No measurement can distinguish all
four kinds of states :math:`|0\rangle`, :math:`|1\rangle`, :math:`|+\rangle`,
:math:`|-\rangle`. This is not a limitation of the measurement, but a
fundamental consequence of the uncertainty principle. (This limitation
gives rise to the possibility of quantum money and quantum
cryptography.) 

|image2|

A third commonly-used basis is the *circular* (or :math:`Y`) basis:
:math:`|\circlearrowright\rangle =
\frac{1}{\sqrt{2}}(|0\rangle+i|1\rangle)`, :math:`|\circlearrowleft\rangle
= \frac{1}{\sqrt{2}}(|0\rangle-i|1\rangle)`. To make the
:math:`|\circlearrowright\rangle` state we will use :math:`S`, the phase
gate. This gate applies a complex phase to :math:`|1\rangle`. By applying
an :math:`H` followed by an :math:`S` gate to the :math:`|0 \rangle` state, you
can obtain :math:`|\circlearrowright \rangle`. Try to figure out how to
get the :math:`|\circlearrowleft\rangle` on your own. 

Like the above example, measurement in the standard basis will not give
you different statistics. Even measurement in the diagonal basis will be
random. To measure in this basis, we must rotate the standard basis
(:math:`Z`) to the circular basis (:math:`Y`). To do this, use an :math:`S^\dagger`
followed by :math:`H` before your measurement.

| |image3|                                                  

|  Try out the last example. It should give you 1, since it is a
  measurement of :math:`|\circlearrowright\rangle` in the circular
  basis. 
  
  
|
| **Superposition (+) Z-Measurement**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=5306b82998001797c6ef04345641bab8&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-5306b82998001797c6ef04345641bab8.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=5306b82998001797c6ef04345641bab8&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Superposition (-) Z-Measurement**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=5306b82998001797c6ef0434564767f0&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-5306b82998001797c6ef0434564767f0.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=5306b82998001797c6ef0434564767f0&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Superposition (+) X-Measurement**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=7c2bba34e2503c02aa981dcca8fa718f&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-7c2bba34e2503c02aa981dcca8fa718f.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=7c2bba34e2503c02aa981dcca8fa718f&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Superposition (-) X-Measurement**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=ba9448cba01a6e174b2cbccad444da1a&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-ba9448cba01a6e174b2cbccad444da1a.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=ba9448cba01a6e174b2cbccad444da1a&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Superposition (+i) Y-Measurement**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=5306b82998001797c6ef0434561ebdeb&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-5306b82998001797c6ef0434561ebdeb.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=5306b82998001797c6ef0434561ebdeb&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Superposition (-i) Y-Measurement**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=89524da231758e94d5784382510c722d&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-89524da231758e94d5784382510c722d.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=89524da231758e94d5784382510c722d&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>




.. |image0| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-01%20at%2010.10.18%20AMuowlp7a3sq69a4i.png
.. |image1| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-01%20at%2011.50.10%20PM2zdd8eau6jxuhaor.png
.. |image2| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/hadamardhhz7mtz2witl0udi.png
.. |image3| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-01%20at%2011.50.16%20PMpyrs6zll64t8d7vi.png

