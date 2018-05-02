Running your Quantum Scores
===========================

| Now that we've gotten familiar with the Composer, let's go over how to
  run a quantum score. 

| When you begin an experiment, you'll be prompted to give it a name, so
  that you can recognize it later. You will also see two choices: Real
  Quantum Processor, or Custom Topology.  In both cases, you create your
  score by dragging gates onto the stave, adding a measurement, and then
  hitting "Run" for the score to execute. 

Running on an Custom Quantum Processor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you select "Custom Topology," your only option is to run your score
in simulation. This is because the custom processor permits all-to-all
connectivity; the real device, in contrast, is limited by physical
connectivity. When you select Custom Topology, a dialogue box will ask
you to select the number of qubits and classical bits assigned to
different registers. We have set the maximum number of qubits to 20. The
execution of your circuit happens immediately (unless the number of
qubits is large) and the output can then be viewed in the Results (see
the next section). Try out the "Single Qubit Measurement" below.

Running on a Real Quantum Processor (Requires Units)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| If you select "Real Quantum Processor," the score you compose will be
  placed into the experimental queue when you hit "Run," and you will be
  notified via email when it has been executed on the actual quantum
  computer in our lab. 

You must have Units in your Quantum Experience account to use the Real
Quantum Processor.  If the score you are trying to run has previously
been run, you will be given the choice of seeing the results from the
cached execution right away (which costs no Units), or spending the
Units to re-run the score as a new execution (meaning it will go into
the experimental queue, and you will receive an email notification when
it is done). 

Note that many of the score examples found in this User Guide have
previous executions available for you to view and experiment with!

Once you hit "Run," your score's progress will be visible in the "My
Scores" tab, sorted by date executed. When your results are ready, you
will be able to view them from this tab. You can also re-edit your score
and execute it on the simulator while you wait for your results to
return. 

|
| **Single Qubit Measurement**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=c0e1386ab6ad50c7464096012f656334&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-c0e1386ab6ad50c7464096012f656334.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=c0e1386ab6ad50c7464096012f656334&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Single Qubit Measurement (Real)**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=68d7454c2e1e9e6dfd17d2c0289a387f&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-68d7454c2e1e9e6dfd17d2c0289a387f.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=68d7454c2e1e9e6dfd17d2c0289a387f&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>


