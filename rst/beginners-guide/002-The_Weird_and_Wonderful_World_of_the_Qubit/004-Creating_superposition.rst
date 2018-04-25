Creating Superposition
======================

| Now that we know how to switch between :math:`|0\rangle`
  and :math:`|1\rangle`, let's explore superposition, which is the concept
  of generating a new quantum state which is a combination of the basis
  states :math:`|0\rangle` and :math:`|1\rangle`. To make superposition
  states, we will expand our set of gates to include \ *H* (which you
  saw earlier in the guide). In the Quantum Composer, this is the blue
  gate labeled *H*.

| |image0|

|

.. cssclass:: h2

The Hadamard Gate

Place the *H* gate, known as the Hadamard gate, on one of the qubits
(which starts in the :math:`|0\rangle` state) and run the standard
measurement. Did you find that the qubit behaves half the time like
a :math:`|0\rangle` and half the time like a :math:`|1\rangle`? Before the
measurement forced the qubit to choose a final state, the qubit's
state was neither :math:`|0\rangle` nor :math:`|1\rangle` but rather a
uniquely quantum state, a superposition, consisting of an
equal-weighted combination of these two states. 

|   
  
The special case where the *H* gate is applied to the :math:`|0\rangle`
state is given its own symbol and definition: :math:`|+\rangle =
\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)`. This is a fancy way
of saying that this new state that we call “\ :math:`|+\rangle`\ ”
has a 1/2 probability of giving the outcome 0 and 1/2 probability of
giving the outcome 1 (remember how the coefficient squared gives the
probability of the outcome?). You can think of the *H* gate as a
rotation around the X+Z axis, shown below with a dotted line. This is
the standard representation of a superposition state, and **points
along +X on the Bloch sphere**.

*π rotation around X+Z axis (exchanges X and Z):*

| |image3|

|

:math:`|+\rangle` *superposition state, the standard representation of a superposition:*

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=3033b263493f8f4eacad676036b70f22&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-3033b263493f8f4eacad676036b70f22.png" style="width: 100%; max-width: 600px;"></a>
  <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=3033b263493f8f4eacad676036b70f22&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

| 
| 

Below is a sample histogram showing the results of running the above
circuit 100 times. Although on average we expect this circuit to yield 0
and 1 with equal probabilities, any finite set of trials is unlikely to
produce this result exactly, just as 100 fair coin tosses generally
won't yield exactly 50 heads and 50 tails.

| |image2|


.. cssclass:: h2

The Superposition Basis (X Basis)

Together with the state :math:`|-\rangle = \frac{1}{\sqrt{2}}(|0\rangle
- |1\rangle)`, which is **a vector pointing along –X on the Bloch
Sphere**, we can define a new basis (or measurement direction) called
the superposition basis. The :math:`|-\rangle` state is made using the
circuit below. The *X* gate flips the :math:`|0\rangle` to a
:math:`|1\rangle`, and then the *H* gate rotates the qubit around the X+Z
direction to produce the :math:`|-\rangle` state.

:math:`|-\rangle` *Superposition State Bloch representation:*


| |image4|

When you run this circuit you will find that, like before, the outcomes are equal.
Different states give the same outcomes! 

:math:`|-\rangle` *Superposition Composer circuit diagram:*

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=69105edada81f30718a6872b1133ee2d&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-69105edada81f30718a6872b1133ee2d.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=69105edada81f30718a6872b1133ee2d&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

:math:`|-\rangle` *Superposition Composer Result Histogram:*

| |image6|

When you measure along the standard basis Z (which is the only direction
we can access with our pink Z measurement gate), we are not able to
access information about the qubit’s phase. 


.. cssclass:: h2

:math:`|+\rangle` and :math:`|-\rangle` States

To tell the difference between the states :math:`|+\rangle` and
:math:`|-\rangle`, we need to \ *measure*\  in the superposition basis.
Experimentally, we cannot physically measure along the different
directions of the Bloch Sphere; however, we can make it look like we’re
changing the measurement by rotating our qubit state using gates before
performing the standard measurement (which can only measure along “+Z”).
To measure in the X basis, we rotate the qubit’s state until the qubit’s
component that previously pointed along X points now in the “+Z”
direction, which is accomplished by applying a Hadamard gate before the
measurement. 

|image7|

|

Try the above measurements of the superposition :math:`|+\rangle` and
:math:`|-\rangle` states in the X basis. You should find that 100% of the
time the outcome is 0 and 1 respectively. That is, if we make a
measurement in the standard (“Z”) basis, the outcome is completely
random. But, in the X basis, it has a deterministic outcome!

:math:`|+\rangle` *state measured in X basis:*

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=61eed74ff0b30d2476bdac5d454f0024&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-61eed74ff0b30d2476bdac5d454f0024.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=61eed74ff0b30d2476bdac5d454f0024&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

| |image9|

:math:`|-\rangle` *state measured in X basis:*

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=b8c9dbdafa24ade6bc96be2916487493&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-b8c9dbdafa24ade6bc96be2916487493.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=b8c9dbdafa24ade6bc96be2916487493&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>



.. |image0| image:: data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADYAAAA2CAYAAACMRWrdAAAAAXNSR0IArs4c6QAAAAlwSFlzAAALEwAACxMBAJqcGAAAAm1pVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDUuNC4wIj4KICAgPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAgICAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgICAgICAgICAgeG1sbnM6dGlmZj0iaHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8iPgogICAgICAgICA8dGlmZjpYUmVzb2x1dGlvbj43MjwvdGlmZjpYUmVzb2x1dGlvbj4KICAgICAgICAgPHRpZmY6WVJlc29sdXRpb24+NzI8L3RpZmY6WVJlc29sdXRpb24+CiAgICAgICAgIDx0aWZmOlJlc29sdXRpb25Vbml0PjI8L3RpZmY6UmVzb2x1dGlvblVuaXQ+CiAgICAgICAgIDx0aWZmOkNvbXByZXNzaW9uPjE8L3RpZmY6Q29tcHJlc3Npb24+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDx0aWZmOlBob3RvbWV0cmljSW50ZXJwcmV0YXRpb24+MjwvdGlmZjpQaG90b21ldHJpY0ludGVycHJldGF0aW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4K0ULlwgAAAj5JREFUaAXtWktOwzAQHafpR7SCDWJVQWGHxIIVa86AuEdViSU7uAC3YVGx5BCIM0BFCxL9pLyJErGxEzfxlBB5JFOIn8fz5k1cO0ENX+drqpOBzVlXkaLxZ72IRUTDkyaFFNSLF0GrABXIrZbmif03Wb1iXrGKZMCXYkWEsA7DK2adqooAvWIVEcI6DK+YdapS4Fqlv5k/GWODM3sw9oTGnjIdIQJuoC3hZJVxLGqi3wZXIBb3pRgpuj9q0eSiQ7eHLSL8rTVcf8CBkHE3fTDEAdGluSeG6PYaaFCti88s24VajOuxao5NhFiEUyxbRhHG/alIebgYvOEPEWIbxiACry0xmVUx0WDJNRbXm+YewvWsBbOsjKLETncUXR5gBdHUhQKxQUdDuCyjZLwosev9BnH7CxMl9vwR0eNbRIFGmAhlegXS5z1Np4NMiBIbTyK6e/nG7kIT6Yqo326DmEwIMl4THk0Wg798tU+bFfHOS8o0t7XUVNv164ltN9/lZxNRLEh2iXm3UDp5Hq4IzdR3kbHGMVN8+b5j2/HFa3qGTbH1YNxMYAui6GmWPXtGYMYuXu648Z4q3lcZkLxsxgfNHJxhuPYyznmjAb/4k7AFnC6SfGXV2ZwnB04lWIexyBCzDdQWV4CwyD1WIA7nQzwx5ykVdugVE06wc/deMecpFXboFRNOsHP3XjHnKRV26BUTTrBz914x5ykVdhga3zgKTyzmHo8l+IlEODrmF8EFzf3Bt2Agv8PWiIn/2fkHtm5mLH8+iCoAAAAASUVORK5CYII=
.. |image1| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/1q-hgate8rwln2i8kpc1h5mi.png
.. |image2| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/4-4ygaleeu23g4on7b9.png
.. |image3| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/h-gateic85jejrw0l766r.png
.. |image4| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/x-h-gatehj08yk31ihog8pvi.png
.. |image5| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/-superpostionsate-2pyvl6vu05y3w61or.png
.. |image6| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/-superpostionsate-3fstlnp0jvk95p14i.png
.. |image7| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/hadamard-gate07x3vqw802t3ayvi.png
.. |image8| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/1q-hgate-xmeasm9641j8qcl3di.png
.. |image9| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/h-h-gates4dutkkydoaqt1emi.png
.. |image10| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/1q-x-hgates-xmeas5a5ys1vws2ejc3di.png

