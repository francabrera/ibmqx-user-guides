GHZ States
==========

Perhaps even stranger than Bell states are their three-qubit
generalization, the *GHZ states*. An example of one of these states
is :math:`\frac{1}{\sqrt{2}}(|000\rangle- |111\rangle)`. The measured
results should be half :math:`|000\rangle` and half :math:`|111\rangle`. GHZ
states are named after Greenberger, Horne, and Zeilinger, who were the
first to study them in 1997. GHZ states are also known as "Schroedinger
cat states" or just "cat states."

In the 1990 paper by N. David Mermin, *What's wrong with these elements
of reality?*, the GHZ states demonstrate an even stronger violation of
local reality than Bell's inequality. Instead of a *probabilistic*
violation of an inequality, the GHZ states lead to a *deterministic*
violation of an equality.

|image0|\ Imagine you have three independent systems which we denote by
a blue, red, and green box. You are asked to solve the following
problem: in each box there are two questions, labeled :math:`X` and :math:`Y`,
that have only two possible outcomes, :math:`+1` or :math:`-1`. You must come up
with a solution to the following set of identities.

| :math:`XYY=1`.

:math:`YXY =1`.

:math:`YYX=1`.

.. raw:: html

   <div>

:math:`XXX = -1`.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Try it! 

After a while you will realize this is not possible. The simple way to
show this is the following: if we multiply the first three equations
together, we can simplify squared quantities and obtain :math:`XXX=1`, which
contradicts the fourth identity.

Amazingly enough, a GHZ state can provide a solution to this problem.
Then we have to accept what quantum mechanics teaches us: there are
not local hidden elements of reality associated with each qubit which
predetermine the outcomes of measurements in the :math:`X` and :math:`Y`
bases. So, as Mermin pointed out, the GHZ test described above
contradicts the possibility of physics being described by local reality!
As opposed to the Bell test, which provides only a statistical evidence
for the contradiction, the GHZ test can rule out the local reality
description with certainty after a single run of the experiment (not
including the effects of noise and imperfections in our system). 

|image1|

.. raw:: html

   <div>

| To make this state we use the following circuit, which is slightly
  different to the standard way of creating a GHZ (in our hardware the
  CNOT gates are constrained in their orientation). In the first part of
  the circuit, the ground state is taken to a superposition
  :math:`\frac{1}{2}(|001\rangle+ |011\rangle + |101\rangle
  +|111\rangle)`. The two CNOTs now entangle all the qubits into the
  state :math:`\frac{1}{2}(|001\rangle + |010\rangle + |100\rangle +
  |111\rangle)`. The final three Hadamard gates map this to the GHZ
  state :math:`\frac{1}{\sqrt{2}}(|000\rangle - |111\rangle)`.

To make the measurements in the :math:`X` and :math:`Y` basis we again rotate
the measurement using the circuits you have seen before. For example,
consider the :math:`XXX` measurement. Note that flipping all three qubits of
the GHZ state gives the same state with the minus sign. In other words,
the GHZ state is a :math:`-1` eigenvector of a three-qubit Pauli operator
:math:`XXX`. This implies 

:math:`XXX=-1`

for each realization of the experiment. Next consider the Pauli operator
:math:`XYY`. One can check that the GHZ state is a :math:`+1` eigenvector of
:math:`XYY`. Therefore,

:math:`XYY=1`

| for each realization of the experiment. Likewise,

:math:`YXY=1`, and :math:`YYX=1`.

One can verify this by running the experiments using the circuits
provided below. 

| Here you can see the results we got when we ran this experiment on the
  processor: 

                    |image2|\ 

| EXAMPLE CIRCUITS:

| The first circuit shown below creates a GHZ state and then measures
  all qubits in the standard basis. The measured results should be half
  :math:`000` and half :math:`111`. The remaining four circuits describe the GHZ
  test. Each circuit prepares the GHZ state and then measures the three
  qubits by choosing the measurement bases according to :math:`YYX`,
  :math:`YXY`, :math:`XYY`, and :math:`XXX` respectively. 

.. raw:: html

   </div>

.. raw:: html

   </div>
   
   
|
| **3Q GHZ State**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=479450d7f0d95a28e4fa155576c25c03&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-512686ae13a97aaed71304b5d814a41f.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=479450d7f0d95a28e4fa155576c25c03&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **3Q GHZ State YYX-Measurement**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=0e6a68c3cd23d638b8093ad4d067d45f&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-d9c40f27d67d4bf722209faa34a86971.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=0e6a68c3cd23d638b8093ad4d067d45f&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **3Q GHZ State YXY-Measurement**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=09ed38c0975b6f51d6945603177805c3&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-570b68405ba63ca75c724d3f40a8c8fa.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=09ed38c0975b6f51d6945603177805c3&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **3Q GHZ State XYY-Measurement**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=ae3e60e47e4c28f29edcb5a9a49519c3&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-0e6a68c3cd23d638b8093ad4d06b9d72.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=ae3e60e47e4c28f29edcb5a9a49519c3&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **3Q GHZ State XXX-Measurement**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=ba07eaf7c8c75a9f9c5cf12a947ce1e0&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-b9096192e0ccec3ff6ac2156b7cff400.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=ba07eaf7c8c75a9f9c5cf12a947ce1e0&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>



.. |image0| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-02%20at%2012.42.45%20AMl8kxsz2b6cs4te29.png
.. |image1| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-02%20at%2012.42.54%20AMjqrs28j545p6tj4i.png
.. |image2| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/Screen%20Shot%202016-05-03%20at%2010.30.31%20PM5vv145poc8qfflxr.png

