Non-Clifford Gates
==================

The most general operation that a quantum computer can perform is a
unitary matrix in :math:`2^n` dimensions. A finite set of gates that can
approximate any unitary matrix arbitrarily well is known as a `universal
gate
set <https://en.wikipedia.org/wiki/Quantum_gate#Universal_quantum_gates>`__.
This is similar to how certain sets of classical logic gates, such as
{AND, NOT}, are `functionally
complete <https://en.wikipedia.org/wiki/Functional_completeness>`__ and
can be used to build any Boolean function.

Up to this point, all the gates we have discussed (:math:`X, Y, Z, H, S,
S^\dagger,` and CNOT) are members of a special group of gates known as
the Clifford group. These gates can be simulated efficiently on a
classical computer (see the
`Gottesman-Knill <https://en.wikipedia.org/wiki/Gottesman%E2%80%93Knill_theorem>`__
theorem). Therefore, the Clifford group is not universal. It cannot
harness the full power of quantum computation; for that, we must include
at least one non-Clifford gate in our circuits.    

Any unitary matrix can be written as a combination of single- and
two-qubit gates [`*Barenco et al.,
1995* <http://journals.aps.org/pra/abstract/10.1103/PhysRevA.52.3457?cm_mc_uid=43781767191014577577895&cm_mc_sid_50200000=1460741020>`__].
(This is unlike classical reversible computing, where 3-bit gates such
as `Toffoli <https://en.wikipedia.org/wiki/Toffoli_gate>`__ are
additionally required for functional completeness.) It turns out that
adding almost any non-Clifford gate to single-qubit Clifford gates and
CNOT gates is universal. There are several popular choices for
non-Clifford gates, but we implement :math:`T` as well as :math:`T^\dagger`.
These are given by

                                             |image0|

The :math:`T` gate essentially makes it possible to reach all different
points of the Bloch sphere. We can see that by increasing the number of
:math:`T`-gates in our circuit (the so-called *:math:`T`-depth*) we start to
cover the Bloch sphere more densely with states we can reach. The
following figures depict the attainable states by increasing :math:`T`-depth
from 0, 1, ... up to 5. In the final Bloch sphere for :math:`T`-depth 5, we
have highlighted a few points in red, green, and blue, which correspond
to the Clifford+:math:`T` scores given below. Run these circuits to see if
you end up at those points!

| 
|  |image1|\ |image2|\ |image3|\ |image4|\  \ |image5|\ |image6|

T-Depths are 0, 1, 2, 3, 4, and 5. 

| 

|
| **Red State**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=4c0c46c51bc95c280e3cecc7140121c0&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-86e01da97076b98d2319178fd24a021b.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=4c0c46c51bc95c280e3cecc7140121c0&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Green State**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=4c0c46c51bc95c280e3cecc71432020c&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-10910faa24c7d6aacafbfe41a9fbf900.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=4c0c46c51bc95c280e3cecc71432020c&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Blue State**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=82f8e7eaf1640aed285a4e982a12571f&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-95469a8631bfe86cdf55b0a254df561e.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=82f8e7eaf1640aed285a4e982a12571f&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>
   
|

.. |image0| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/images-classroom/Screen%20Shot%202016-05-02%20at%2012.45.45%20AMfhgoazwxmbgctyb9.png
.. |image1| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/images-classroom/int_t_0fi382bh9mhg2e29.png
.. |image2| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/images-classroom/int_t_13fid4cebb6ueg66r.png
.. |image3| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/images-classroom/int_t_27u4tzjysgoczyqfr.png
.. |image4| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/images-classroom/int_t_3q0962f566hqto6r.png
.. |image5| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/images-classroom/int_t_4twgt6a9985hilik9.png
.. |image6| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/images-classroom/int_t_5coloriqn3cbzw7b9.png

