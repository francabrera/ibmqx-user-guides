Entanglement and Bell Tests
===========================

One of the infamous counterintuitive ideas of quantum mechanics is that
two systems that appear too far apart to influence each other can
nevertheless behave in ways that, though individually random, are too
strongly correlated to be described by any classical local theory. 

To understand this, we have outlined a simple Bell test experiment here.
Imagine you have two systems (see blue and red systems below). Within
each there are two measurements performed: :math:`A`, :math:`A'`, :math:`B` and
:math:`B'`, that have outcomes :math:`1` (or :math:`-1`). Bell showed that if these
measurements are chosen correctly for a given entangled state, the
statistics can not be explained by any local hidden variable theory, and
that there must be correlations that are beyond classical. 

|                          |image0|

| In 1969 \ `John
  Clauser <https://en.wikipedia.org/wiki/John_Clauser>`__\ , \ `Michael
  Horne <https://en.wikipedia.org/w/index.php?title=Michael_Horne&action=edit&redlink=1>`__\ ,
  \ `Abner Shimony <https://en.wikipedia.org/wiki/Abner_Shimony>`__\ ,
  and \ `Richard
  Holt <https://en.wikipedia.org/w/index.php?title=Richard_Holt_%28physicist%29&action=edit&redlink=1>`__\ 
  derived the following CHSH inequality :math:`|\mathrm{C}|\leq 2` where

                         |image1|

and the correlated expectation is given by 

|                          |image2|

with :math:`0` giving outcome :math:`+1` and :math:`1` giving outcome :math:`-1`. A
correlation of 1 means both observables have even parity, and a
correlation of -1 means both observables have odd parity.

It is simple to show that this inequality must be true if the theory
obeys the following two assumptions, *locality* and *realism*:

**               Locality**\ : No information can travel faster than the
speed of light. There is a hidden variable :math:`\lambda` that defines all
the correlations so that

                            |image3|

and :math:`C` becomes 

                      |image4|

.. raw:: html

   <div>

              **Realism**: All observables have a definite value
independent of the measurement (+1 or -1). This implies that either
:math:`|B(\lambda)+B'(\lambda)|=2` (or :math:`0`) while
:math:`|B(\lambda)-B'(\lambda)| = 0` (or :math:`2`) respectively. That is,
:math:`|\mathrm{C}|= 2`, and noise will only make this smaller. 

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Perfectly reasonable, right? However, as you see, :math:`|C|>2`. How is
this possible? The above assumptions must not be valid, and this is one
of those astonishing counterintuitive ideas necessary to accept in the
quantum world. Before you launch the scores below, let's try to
understand what is happening and how each observable is measured and
combined to give :math:`|C|`.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

The Bell experiment we provide uses the entangled state
:math:`\frac{1}{\sqrt{2}}(|00\rangle+|11\rangle)`, and the two
measurements for system A are :math:`Z` and :math:`X`, while the two for B are
:math:`W=\frac{1}{\sqrt{2}}(Z+X)` and :math:`V=\frac{1}{\sqrt{2}}(Z-X)`. 

.. raw:: html

   </div>

.. raw:: html

   <div>

                            |image5|\ 

.. raw:: html

   </div>

.. raw:: html

   <div>

For an ideal implementation the four correlated expectation values
give, 

.. raw:: html

   </div>

.. raw:: html

   <div>

                      |image6|\ 

.. raw:: html

   </div>

which gives :math:`|C|=2\sqrt{2}`. 

To run this experiment with our hardware, we need the following quantum
score and 4 measurements. 

|                             |image7|

In the first part of the experiment, the qubits are initially prepared in
the ground state :math:`|00\rangle`. The :math:`H` takes the first qubit to
the equal superposition :math:`\frac{|00\rangle+|10\rangle}{\sqrt{2}}`,
and the CNOT gate flips the second qubit if the first is excited, making
the state :math:`\frac{|00\rangle+|11\rangle}{\sqrt{2}}`. This is the
entangled state (commonly called a *Bell state*) required for this test.
In the first experiment, the measurements are of the observable :math:`Z` and
:math:`W= \frac{1}{\sqrt{2}}(X+Z)`.  To rotate the measurement basis to
the :math:`W` axis, use the sequence of gates :math:`S`-:math:`H`-:math:`T`-:math:`H`,
then perform a standard measurement. The correlator :math:`\langle ZW
\rangle` should be close to :math:`1/\sqrt{2}`, and is found using the
above equation. 

| In the second experiment, the two observables are :math:`Z` and :math:`V=
  \frac{1}{\sqrt{2}}(-X+Z)`. To rotate to this basis, we use the
  sequence of gates :math:`S`-:math:`H`-:math:`T^\dagger`-:math:`H`, then perform a
  standard measurement. The correlator :math:`\langle ZV \rangle` is found
  in a similar way as before; it should be close to :math:`1/\sqrt{2}`.

Finally, in the third and fourth experiment, the correlators :math:`\langle
XW\rangle` and :math:`\langle XV\rangle ` are measured, and should be
close to :math:`1/\sqrt{2}` and :math:`-1/\sqrt{2}` respectively. The :math:`W`
and :math:`V` measurement are performed the same way as above, and the :math:`X`
via a Hadamard gate before a standard measurement. 

Here you can see the results of this experiment on the
processor: 

|                      |image8|

Try it out for yourself! Compare what we got with the simulations (with
both ideal and realistic parameters). 

|
| **Bell State ZZ-Measurement**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=479450d7f0d95a28e4fa155576a9bcbd&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-512686ae13a97aaed71304b5d814465c.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=479450d7f0d95a28e4fa155576a9bcbd&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Bell State ZW-Measurement**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=e21164be4db4b6f5698f254a30184862&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-95469a8631bfe86cdf55b0a254df7c4b.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=e21164be4db4b6f5698f254a30184862&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Bell State ZV-Measurement**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=e21164be4db4b6f5698f254a30191fac&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-6769d2329c7fb8be2514f419db538ac5.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=e21164be4db4b6f5698f254a30191fac&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Bell State XW-Measurement**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=e21164be4db4b6f5698f254a301a9363&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-7bf1fe8b112a27f1defdd1797e5084ae.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=e21164be4db4b6f5698f254a301a9363&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Bell State XV-Measurement**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=479450d7f0d95a28e4fa155576ae55fb&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-95469a8631bfe86cdf55b0a254df8b59.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=479450d7f0d95a28e4fa155576ae55fb&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>



.. |image0| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-01%20at%2011.01.47%20PMp7ywz1fvomuhxgvi.png
.. |image1| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-01%20at%2011.58.25%20PM26fjth9ka5nah5mi.png
.. |image2| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-02%20at%2012.00.28%20AMh9cbwavb76uyds4i.png
.. |image3| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-02%20at%2012.05.08%20AM6dngnqakg0wo2yb9.png
.. |image4| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-02%20at%209.08.24%20PMxpufzfh3hxagu8fr.png
.. |image5| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-03%20at%2012.31.29%20AMggfwizai6qen4s4i.png
.. |image6| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-03%20at%2012.32.31%20AMo3gyvxtqqepzaor.png
.. |image7| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-03%20at%201.15.27%20AMj7c275k02qyf1or.png
.. |image8| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-03%20at%201.15.37%20AMbfusp4upndrc0udi.png

