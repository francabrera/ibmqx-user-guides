Histogram representation (Bar graph)
====================================

In the histogram/bar graph representation, the combination of 0’s and
1’s at the bottom of each bar represents the measured state of the
qubit(s), and the height of the bar represents how frequently the
outcome occured in the different runs of the experiment. Note that the
more qubits you use, the more 0’s and 1’s it takes to represent the
outcome(s). To save space, outcomes that did not occur are omitted from
the histogram, and several low frequency outcomes may be combined into a
bar labeled “other values.”

To try this out for yourself, go into the Composer and create a new
experiment with three qubits. Drag a pink measurement gate over to each
of them and click “Run” or “Simulate.” At this point, there should be
only one possible outcome, 000. That’s because all of the qubits began
in the :math:`|0\rangle` state and we haven’t changed them with any gates.
Now, drag a blue *H* gate to each of the qubits before the measurement.
The *H* gate puts each of the qubits into an equal superposition state.
Now you should see that there are many more possible outcomes. We’ll go
into more detail about the *H* gate in a later section.

|
| **3-qubit measurement, ground state**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=f45e53d09688085a2363c7fc60406e9c&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-f45e53d09688085a2363c7fc60406e9c.png" style="width: 100%; max-width: 600px;"></a>
      <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=f45e53d09688085a2363c7fc60406e9c&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>


| |image1|


|
| **3-qubit measurement, full superposition of states**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=db03d34bf6ad5c4f27777fc3c8adb769&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-db03d34bf6ad5c4f27777fc3c8adb769.png" style="width: 100%; max-width: 600px;"></a>
   
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=db03d34bf6ad5c4f27777fc3c8adb769&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>


|image3|


.. |image0| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/3qh8ftza7f3gtlnmi.png
.. |image1| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/p2-1xvj9gkvh8rakvgqfr.png
.. |image2| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/3q-hgates95aaa44i92ro1or.png
.. |image3| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/p3-1xx44xfuxkcj2rcnmi.png

