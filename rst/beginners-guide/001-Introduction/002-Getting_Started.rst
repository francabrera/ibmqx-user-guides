Getting Started
===============

.. toctree::
   :maxdepth: 1
   :glob:
   :hidden:

   *

The **Quantum Composer** is a graphical user interface for programming a
quantum processor. Think of it as a tool to construct quantum algorithms
using a library of well-defined measurements and gates (operations that
change the state of the qubit).

Throughout this guide, you'll try out many different experiments (feel
free to explore on your own as well). When you first click on the
"Composer" tab, you’ll name your experiment and choose between running
a \ *real* quantum processor or a \ *custom* quantum processor
(simulator). If you choose custom, you'll select the number of qubits in
the experiment and the number of classical bits in the classical bit
register (you can keep this the same as the number of qubits). In the
real processor, the possible connectivity between the qubits is limited
by the experimental setup; there are also some errors in the measurement
due to experimental imperfections. In the custom processor, however,
quantum gates can be placed anywhere. While there are no experimental
errors, you will still observe that random outcomes can occur due to the
nature of quantum information. In this guide, we will show the results
of running experiments on the custom processor (to avoid confusion about
deviations that occur due to experimental errors). We encourage you to
run some experiments on both the custom and real processors so that you
can understand the differences.

The Composer enables you to create a quantum score -- not a score as in
a sporting match, but rather in the musical sense. In a quantum score,
just as with music, time progresses from left to right. Each line
represents a qubit (as well as what happens to that qubit over time).
Just as with musical notes, each qubit has a different frequency. A
quantum algorithm (circuit) begins by preparing the qubits in
well-defined states (for example, “:math:`|0\rangle`” in the picture
below), then executing a series of single- and two-qubit gates in time
from left to right.

| |image0|

Quantum gates are represented by square boxes; they play a frequency for
different durations, amplitudes, and phases. These are called
single-qubit gates. To apply a gate to a qubit, simply drag the gate box
into the qubit staff. To delete, simply double-tap the box or drag it to
the trash bin.

Once you’ve populated the staff with all of the gates and measurements
you’d like, click “Run” (only available for the real processor) or
“Simulate” to generate results for your experiment. Each circuit must
end with a measurement gate in order to run the experiment.

**Single Qubit Measurement:**


| |image1|

In the above example, we created a single-qubit score with one classical
bit in the classical bit register. We measured Qubit “0” and stored the
measurement result in the 0th position of the classical bit register
(this is the line below the score labeled 'c').

After performing a quantum measurement, a qubit's information becomes a
classical bit, meaning it loses the quantum properties of superposition
and entanglement. Each qubit in the measurement either takes the value
0, e.g., if the qubit is measured in state :math:`|0\rangle`; or 1, e.g.,
if the qubit is measured in state :math:`|1\rangle`. Sometimes your qubit
has an equal chance of being a :math:`|0\rangle` or a :math:`|1\rangle`,
such as when it’s in an equal superposition state. In those cases, when
you repeat the experiment many times on the real device (what we call
“shots” in the pull-down menu of Simulate, e.g., 1024 times), you’ll
find that about half the time you measure 0 and half the time you
measure 1.

In the IBM Q Experience, the results of your quantum scores are shown in
a standard histogram/bar graph representation.

.. |image0| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/p0-1xkkbcfvusaotuik9.png
.. |image1| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/p1-1xg3szp1jk40f3whfr.png

