The Results
===========

After performing a quantum measurement, a qubit's information becomes a
classical bit, and in our system (as is standard) the measurements are
performed in the computational basis. For each qubit the measurement
either takes the value 0 if the qubit is measured in state
:math:`|0\rangle` and value 1 if the qubit is measured in state
:math:`|1\rangle`. 

In a given run of a quantum circuit with :math:`n` measurements, the
result will be one of the :math:`2^n` possible n-bit binary strings. If
the experiment is run a second time, even if the measurement is
perfect and has no error, the outcome may be different due to the
fundamental randomness of quantum physics. The results of a quantum
circuit executed many different times can be represented as a
distribution over the full :math:`2^n` possible outcomes. It is not
scalable to represent all possible outcomes; therefore, we keep only
those outcomes that happen in a given experiment and represent them as 
a histogram. 

The histogram/bar graph representation is the simple to understand. 
The height of the bar represents the fraction of instances the outcome
comes up in the different runs on the experiment. Only those outcomes
that occurred with non-zero occurrences are included. If all the bars
are small for visualization only (not if you download the data) they
are collected into single bar called other values. In general this is
not a problem as a good quantum circuit should not have many outcomes
only circuits that have the final state in a large superposition will
give many outcomes and these would take exponential measurements to
measure. 

**Superposition +++++**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=8ea323460b6f03cb9002b802139af008&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-8ea323460b6f03cb9002b802139af008.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=8ea323460b6f03cb9002b802139af008&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>