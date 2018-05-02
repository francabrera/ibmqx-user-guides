Quantum Repetition Code
=======================

Rather than have a general discussion of codes and error-correction, we
will instead look at some of the simplest examples. One of the most
straightforward error-correcting codes is the *repetition code*. To
encode a 1 bit message in the repetition code, we simply copy it several
times (say 3 times): :math:`0` encodes to :math:`000` and :math:`1` encodes to
:math:`111`. Suppose now that we store the *codeword* :math:`000` or :math:`111` in
a memory for a period of time and, during that time, errors occur. A
simple model of errors is to suppose that each bit can flip randomly
with some probability :math:`p<1/2` and that the error process acts
independently on each bit. If one error occurs, the stored codeword
becomes one of :math:`\{001,010,100\}` or one of :math:`\{110,101,011\}`,
respectively. Given an encoded message :math:`abc`, the original message is
the value indicated by a majority of the bits
:math:`\mathrm{MAJ}(a,b,c)=ab\oplus bc\oplus ca`. For example, if we read
:math:`001` from the memory, the majority value is obviously :math:`0`, but we
could also have computed it from the formula for
:math:`\mathrm{MAJ}(0,0,1)`. This recovery procedure works if only one
error occurs; it fails otherwise. However, correcting even a single
error is enough to reduce the probability of failure, since the
probability of more than one error is :math:`3p^2(1-p)+p^3=3p^2-2p^3`, which
is less than :math:`p` whenever :math:`p<1/2`. The reduction in error rate can
be surprisingly large: if :math:`p` is 1 percent, the failure probability
after encoding is less than 0.03 percent.

The repetition code is a classical error-correcting code, but there is a
closely related quantum repetition code that is one of the simplest
quantum codes. Again, rather than defining quantum codes in general, we
will describe a 3-qubit quantum bit-flip code and look at how to encode,
decode, and detect errors.

| To encode a single-qubit message :math:`|\psi\rangle=\alpha
  |0\rangle+\beta |1\rangle` in the 3-qubit quantum bit-flip code,
  we apply a quantum circuit that encodes the messages :math:`0` and :math:`1`
  in superposition so that :math:`|\psi\rangle` encodes to :math:`\alpha
  |000\rangle + \beta |111\rangle`. A very important quantum
  result is that, for arbitrary :math:`\alpha`, we cannot create identical
  copies of :math:`|\psi\rangle`, like (:math:`\alpha |0\rangle + \beta
  |1\rangle`)(:math:`\alpha |0\rangle + \beta |1\rangle`)(:math:`\alpha
  |0\rangle + \beta |1\rangle`), which is the way the classical
  repetition code would operate. Instead, we can make repetitions with
  the codewords. Now, when the message is an equal superposition
  :math:`\frac{1}{\sqrt{2}}(|0\rangle+|1\rangle)`, the encoded message
  happens to be an entangled state, since it cannot be written as a
  tensor product of two or more states. The "*Encoder into bit-flip
  code*" example encodes qubit 2 into the quantum bit-flip code. The
  first three gates in the example prepare qubit 2 in the state
  :math:`\cos(\pi/8)|0\rangle-i\sin(\pi/8)|1\rangle` and the
  remaining gates encode this state into the code.

| Suppose that we store the quantum codeword for a period of time and
  the qubits begin to decohere. It is not obvious, but the error
  operators that arise from independent decoherence processes on each
  qubit can be written as linear combinations of the identity operator
  and the Pauli operators :math:`X`, :math:`Y=-iZX`, and :math:`Z`. Since quantum
  mechanics is a linear theory, it suffices to correct only the bit-flip
  :math:`X` and phase-flip :math:`Z` errors [`Shor
  (1995) <http://journals.aps.org/pra/abstract/10.1103/PhysRevA.52.R2493>`__].
  This is a remarkable observation. By correcting only a discrete set of
  errors, weighted sums of those errors -- and hence a continuum of
  errors -- can be corrected as well.

| That said, the quantum bit-flip code is unable to correct any
  phase-flip errors that occur (hence its name). A phase flip on any
  qubit changes the encoded message to :math:`\alpha |000\rangle - \beta
  |111\rangle`, but this state is an encoding of the 1 qubit message
  :math:`\alpha |0\rangle - \beta |1\rangle`, which is a valid
  codeword too. Hence, the quantum bit-flip code is not "strong enough"
  to correct realistic errors since it is unable to correct phase
  errors. While we do not discuss them here, there are quantum codes
  that can detect and correct the most general types of errors, such as
  Shor's code [`Shor
  (1995) <http://journals.aps.org/pra/abstract/10.1103/PhysRevA.52.R2493>`__].

| The quantum bit-flip code does correct bit-flip errors. We will
  briefly describe two procedures for detecting and correcting a
  bit-flip error using the 3-qubit code.

| The second example below, "*Bit-flip encoder and decoder*," implements
  a reversible majority voter to decode the bit-flip code. The identity
  gates in the circuit represent noise, and you can replace them with
  various operations, such as bit flips :math:`X`, to test the decoder.
  Following the identity gates, a pair of CNOT gates (with Hadamard
  gates) computes :math:`abc\mapsto a\oplus b, b, c\oplus b`. The
  remaining T, CNOT, and H gates that target qubit 2 compute
  :math:`\mathrm{MAJ}(a,b,c)` into qubit 2, which we characterize using
  state tomography. Qubits 1 and 3 carry information about what errors
  occurred and remain unobserved. Even without explicitly inserting any
  errors, an experiment or realistic simulation will decode to a
  different point on the Bloch sphere because (a) the codeword is
  unprotected against phase errors and (b) the encoder and decoder are
  not ideal operations.

| The third example below, "*Encoder into bit-flip code with parity
  checks*," implements parity measurements to detect errors. The first
  set of gates prepares the input state to the encoder, in this case
  :math:`\cos(\pi/8)|0\rangle-i\sin(\pi/8)|1\rangle`. The second set
  of gates is the encoder followed by a SWAP, so that qubits 0, 1, and 3
  contain the codeword. The third and final set of gates implements two
  parity computations: the parity of qubits 0 and 1 is computed into
  qubit 4, and the parity of qubits 1 and 3 is computed into qubit 2.
  Let's call the outcome of measuring qubit 4 by the name :math:`s_0` and
  the outcome of measuring qubit 2 by the name :math:`s_1`. The pair of
  bits :math:`s=s_0s_1` is called the *error syndrome*. If no error or
  just a single bit-flip error occurs, the error syndrome :math:`s` reveals
  the location of the bit-flip error. Specifically, if :math:`s=00` then no
  error occurred, if :math:`s=01` then qubit 3 is flipped, if :math:`s=10` then
  qubit 0 is flipped, and if :math:`s=11` then qubit 1 is flipped.
  Importantly, the act of measuring the error syndrome discretizes the
  error! After measuring quantum codeword in the standard basis, we
  obtain three outcome bits :math:`abc` that are correlated with an error
  syndrome :math:`s` and can use :math:`s` to correct the outcome bits. For
  example, if we measure the outcome :math:`001` (qubits 0, 1, 3) with error
  syndrome :math:`01` (qubits 2 and 4) then we correct :math:`001` to :math:`000`.
  Each three bit outcome :math:`abc` is corrected to one of :math:`000` or
  :math:`111`, and we expect to observe these with probability near
  :math:`\cos^2(\pi/8)` and :math:`\sin^2(\pi/8)`, respectively, if the
  bit-flip error rate it not too high.

| 

|
| **Encoder into bit-flip code (qubits 1-3)**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=74154f1a9b7afaa85e52795ab985e503&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-7bf1fe8b112a27f1defdd1797e52dba0.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=74154f1a9b7afaa85e52795ab985e503&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Bit-flip encoder and decoder (tomography)**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=c318faf262d3e567c71d1acfd981254f&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-512686ae13a97aaed71304b5d819cb7e.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=c318faf262d3e567c71d1acfd981254f&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Encoder into bit-flip code with parity checks (qubits 0,1,3)**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=b25b8a91a6f8355fff5a96b3a51078bd&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_42263efc45184c7ca4742512588a1942/codes/code-570b68405ba63ca75c724d3f40aae778.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=b25b8a91a6f8355fff5a96b3a51078bd&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>
