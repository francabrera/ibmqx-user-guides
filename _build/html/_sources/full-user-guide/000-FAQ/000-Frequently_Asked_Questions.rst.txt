Frequently Asked Questions
==========================

General questions about quantum information science
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



**What does “quantum” mean?
**

| Quantum theory is a revolutionary advancement in physics and chemistry
  that emerged in the early twentieth century. It is an elegant
  mathematical theory able to explain the counterintuitive behavior of
  subatomic particles, most notably the phenomenon of **entanglement**.
  In the late twentieth century it was discovered that quantum theory
  applies not only to atoms and molecules, but to bits and logic
  operations in a computer. This realization has been bringing about a
  revolution in the science and technology of information processing,
  making possible kinds of computing and communication hitherto unknown
  in the Information Age.

| **What is a quantum computer?**
| A quantum computer is a device able to manipulate delicate quantum
  states in a controlled fashion, not dissimilar to the way an ordinary
  computer manipulates its bits.

**Can a quantum computer solve NP-complete problems?**

| We do not believe that quantum computers are likely to provide any
  more than a quadratic speedup to NP-complete problems. This is the
  consensus view of the quantum information research community, and in
  fact the idea that quantum computers can solve NP-complete problems
  efficiently has been described as "`the *central* crock about quantum
  computing <http://www.scottaaronson.com/democritus/lec10.html>`__".

**What is a qubit?**

A qubit (pronounced “cue-bit” and short for quantum bit) is the physical
carrier of quantum information. It is the quantum version of a bit, and
its quantum state can take values of :math:`|0\rangle`, :math:`|1\rangle`,
or both at once, which is a phenomenon known as **superposition**.\ **
**



**What is a superposition?**

A superposition is a weighted sum or difference of two or more states;
for example, the state of the air when two or more musical tones are
sounding at once. Ordinary, or “classical,” superpositions commonly
occur in macroscopic phenomena involving waves.

**How are quantum superpositions different?**

Quantum theory predicts that a computer with :math:`n` qubits can exist in a
superposition of all :math:`2^n` of its distinct logical states
:math:`|000..0\rangle`, through :math:`|111…1\rangle`. This is exponentially
more than a classical superposition. Playing :math:`n` musical tones at once
can only produce a superposition of :math:`n` states.

**How is superposition different from probability?**

A set of :math:`n` coins, each of which might be heads or tails, can be
described as a probabilistic mixture of :math:`2^n` states, but it actually
**is** in only one of them—we just don’t know which. For this reason,
quantum superposition is more powerful than classical probabilism.
Quantum computers capable of holding their data in superposition can
solve some problems exponentially faster than any known deterministic or
probabilistic classical algorithm. A more technical difference is that
while probabilities must be positive (or zero), the weights in a
superposition can be positive, negative, or even complex numbers.

**How is a quantum superposition different from exponential
parallelism?**

Just as a superposition is stronger than a probabilistic mixture, so it
is weaker than actually having an exponentially large army of real
computers (which is an unrealistic proposition in any case, since the
observable universe isn’t big enough to hold :math:`2^{100}` of anything).
The power of quantum computers remains to be explored, but it is
considered to be strictly weaker than exponential parallelism, and
strictly stronger than probabilism.

**What is entanglement?**

Entanglement is a property of most quantum superpositions and does not
occur in classical superpositions. In an entangled state, the whole
system is in a definite state, even though the parts are not. Observing
one of two entangled particles causes it to behave randomly, but tells
the observer how the other particle would act if a similar observation
were made on it. Because entanglement involves a correlation between
individually random behaviors of the two particles, it cannot be used to
send a message. Therefore, the term “instantaneous action at a
distance,” sometimes used to describe entanglement, is a misnomer. There
is no **action** (in the sense of something that can be used to exert a
controllable influence or send a message) -- only **correlation**,
which, though uncannily perfect, can only be detected afterward when the
two observers compare notes. The ability of quantum computers to exist
in entangled states is responsible for much of their extra computing
power, as well as many other feats of quantum information processing
that cannot be performed, or even described, classically.

**What is the uncertainty principle?**

| In quantum physics, we cannot simultaneously know two non-commuting
  variables (like the position and momentum of a particle). This implies
  that a quantum system in a perfectly definite state can be certain
  under one measurement and completely random under another.  Moreover,
  if a quantum system starts out in an arbitrary unknown state, no
  measurement can reveal complete information about that state; and the
  more information the measurement reveals, the more the state is
  disturbed.  This is a underlying principle of quantum cryptography.

**What is a quantum gate?**

A quantum gate is an operation that is applied to a qubit to change its
state. To generate entanglement you must have at least a two-qubit gate
equivalent to the CNOT. 

General questions about the IBM Quantum Experience
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**What is the IBM Quantum Experience?**
'''''''''''''''''''''''''''''''''''''''

The IBM Quantum Experience is a cloud-based platform where you can
learn, research, and interact with a real quantum computer housed in an
IBM Research lab.  **
**

**What is the Quantum Composer?**

| The Quantum Composer is a graphical interface tool where you can drag
  and drop different operations to control qubits. The Quantum Composer
  permits you to develop your own quantum algorithms, which we call
  Quantum Scores.

**What is a Quantum Score?**

A Quantum Score is the set of instructions, or algorithm, to a quantum
computer. It is a series of gates versus time played on different
qubits, much like a musical score. **
**

**What is the Quantum Sphere?**

The Quantum Sphere is a graphical representation of the output of a
Quantum Score. It provides the user a way to easily visualize properties
of the measurements performed on a number of qubits, all in one
diagram.\ **
**

Questions about quantum computers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**What is a universal quantum computer?**

A universal quantum computer is a machine that can simulate an arbitrary
quantum state from an arbitrary input quantum state. **
**

**What is a \ **universal** fault-tolerant quantum computer?
**

A universal fault-tolerant quantum computer is the grand challenge of
quantum computing. It is device that can properly perform universal
quantum operations using unreliable components. **
**

**When will I have a quantum computer?**

You have access to one now with the Quantum Experience. **** It is small
at the moment, with a five-qubit processor, but it is a work-in-progress
that we are continually improving. **
**

| **What does a quantum computer look like?**

A quantum computer looks like nothing you have on your desk, or in your
office, or in your pocket. It is housed in a large unit known as a
dilution refrigerator and is supported by multiple racks of electronic
pulse-generating equipment. However, you can access our quantum computer
with very familiar personal computing devices, such as laptops, tablets,
and smartphones.

Questions about our qubits and experiments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**What is the qubit that you are physically using?**

| The qubit we use is a fixed-frequency superconducting transmon qubit.
  It is a Josephson-junction-based qubit that is insensitive to charge
  noise. For more information on this type of qubit please see here
  (`Koch *et al.*
  2007 <http://journals.aps.org/pra/abstract/10.1103/PhysRevA.76.042319>`__).
  We use fixed-frequency qubits, as opposed to tunable qubits, to
  minimize our sensitivity to external magnetic field fluctuations that
  could corrupt the quantum information.

**How do you make the qubits?**

The superconducting qubits are fabricated at IBM. The devices are made
on silicon wafers with superconducting metals such as niobium and
aluminum. Details about the fabrication processes are given in these
references (`Chow *et al.*
2014 <http://www.nature.com/ncomms/2014/140624/ncomms5015/full/ncomms5015.html>`__,
`Córcoles *et al.*
2015 <http://www.nature.com/ncomms/2015/150429/ncomms7979/full/ncomms7979.html>`__).

**What are the properties of these qubits?**

The properties of the qubits can be seen below the Quantum Composer.
Properties such as relaxation time (:math:`T_1`), coherence time (:math:`T_2`),
readout errors, and gate errors are given, posted from the last
calibration experiment run on the actual quantum processor device. 

**Where do the qubits live?**

The quantum processor itself is housed inside of a printed circuit board
package. This package is mounted inside of a light-tight, magnetic-field
shielding can, which sits at the coldest stage at the bottom of a
dilution refrigerator, housed in one of IBM's Quantum Computing labs. 

**What's a dilution refrigerator?**

| A dilution refrigerator is the machine we use to cool down our quantum
  processor device. The refrigerator cools the device down to around 15
  miliKelvin. It works by circulating a mixture of two helium isotopes,
  :math:`^{3}`He and :math:`^{4}`He, in a closed cycle within a complex system
  of pipes and chambers.

**What happens when I hit the "Run" button?**

The graphical quantum score is first interpreted, then compiled to run
efficiently on a particular qubit configuration. The compiled version is
translated into a sequence of operations performed by equipment in our
lab to control the qubits. The output is then passed back to the user,
and a note is sent to your email address to alert you that the quantum
hardware has run your experiment.

**How are quantum gates performed in the system?**

Quantum gates are performed by sending electromagnetic impulses at
microwave frequencies to the qubits through coaxial cables. These
electromagnetic pulses have a particular duration, frequency, and phase
that determine the angle of rotation of the qubit state around a
particular axis of the Bloch sphere. For single-qubit operations, only
one pulse type needs to be calibrated, namely :math:`X_{\pi/2}`. From that
pulse, we can create all the gates you find in the Quantum Composer
library. For example, we implement the :math:`S` gate with the help of a
phase transform performed purely in software, which affects the physical
implementation of subsequent gates; however, this does not mean that the
gate is necessarily error-free, as doing a software phase transform
still requires very good phase stability from our instruments! Another
example is the Hadamard gate performed by the sequence
:math:`SX_{\pi/2}S`.

**What about two-qubit gates?**

| Two-qubit gates typically require tuning to calibrate the interaction
  between the two qubits during the gate duration, and minimizing the
  interaction at any other time. Since our qubits of choice are
  fixed-frequency transmons, we cannot tune the interaction by bringing
  them closer in frequency during the two-qubit gate. Instead, we
  exploit the cross-resonance effect (`Chow *et al*.,
  2011 <http://journals.aps.org/prl/abstract/10.1103/PhysRevLett.107.080502>`__),
  by driving one of the qubits (called **control**) with a microwave
  pulse tuned at the frequency of the second qubit (called **target**).
  By doing this, we can actively increase the strength of the coupling
  between them. The nature of the cross-resonance effect also allows us
  to perform rotations in the target qubit conditioned on the state of
  the control qubit, a key characteristic of the CNOT operation required
  for a universal quantum gate set. From our cross-resonance microwave
  pulse, we only need to perform an additional frame change :math:`S` on the
  control qubit and a :math:`X_{\pi/2}` on the target to implement a CNOT.

**How are measurements performed in the system?**

We must perform the qubit measurements in a way that does not destroy
the qubit quantum state. One method is to weakly couple each qubit to a
microwave resonator whose resonance characteristics depend on the state
of the qubit. Once the qubit operations are completed in your score, you
can measure the qubits by sending a microwave tone to their resonators
and analyzing the signal it reflects back. The phase and amplitude of
this reflected signal will be different depending on the qubit state.
These signals in the resonator are boosted via a chain of amplifiers
inside of our dilution refrigerator, including a quantum-limited
amplifier at 15 mK, and a high-electron mobility transistor amplifier at
4 K. 

| Do not forget to include measurements in your score! Because the
  measurement of a qubit in a superposition state seems random -- the
  outcome is sometimes 0 and sometimes 1 -- you must repeat the
  measurement multiple times to determine the likelihood of a qubit
  being in a particular state. When performing the experiment, you will
  be asked how many "shots" or experiments to run in order to determine
  the qubit state probabilities. 

**How often is the system tuned up?**

| We perform a full round of single- and two-qubit calibrations, as well
  as measurements of relaxation time, coherence time, and gate errors
  two times a day at 8AM and 8PM EST. Each full calibration round takes
  about one hour.  During calibration, you will notice that the device
  will be "Down for Maintenance."

Questions about running the simulator versus the experiment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**What does the simulator do?**

| The simulator computes the quantum state we expect a circuit to
  produce. 

**What is the difference between ideal and realistic simulator?**

| The ideal simulator treats each gate as a unitary matrix and composes
  the gates to find the output state. This simulator tells us what to
  expect when all of the operations are perfect. The realistic
  simulator, on the other hand, numerically solves a system of
  differential equations known as a
  `master <https://en.wikipedia.org/wiki/Master_equation>`__ equation.
  The master equation we solve includes dissipation and phase noise, as
  well as time-dependent terms for gates and interactions between
  adjacent qubits. The various interaction strengths are computed from
  realistic parameters and an effective
  `Hamiltonian <https://en.wikipedia.org/wiki/Hamiltonian_%28quantum_mechanics%29>`__.
  The results are qualitatively similar to what is observed in a typical
  experiment.

**How many experiments can I run?**

| You can run as many experiments as you have Units to run; each
  experiment execution requires between 3 and 5 Units. No Units are
  required to perform simulations or to recall results of an experiment
  that was run previously.

**How do I gain more Units?**

Depending on your usage pattern and by requesting upgraded status, the
team will consider converting users from Standard to Expert. 

**What happens when I run out of Units?**

| You can still run simulations or recall the result of the experiments
  that have been run previously, but you must wait for the Units to
  replenish, which happens either once your execution has run off the
  queue, or 24 hours, whichever is greater.

**What is the difference between "Current Units" and "Promo Units"?**

The maximum number of "Current Units" available is based on your user
level.  A Standard User has a maximum of 15 credits, and these credits
are replenished upon the greater of 24 hours or when your execution has
run off the queue. On the other hand, "Promo Units" are extra units that
allow you to run extra executions but, once used, these credits won't be
replenished. If you have "Promo Units", these will be used first rather
than "Current Units".

**What are the different user levels?**

| Everyone begins as a Standard User. This level of user is advised to
  work through the entire User Guide, running scores in either
  Simulation mode or viewing cached results (both options require no
  Units). At the beginning, you will have 5 Units and 6 additional promo
  Units. Upon completion of the User Guide, the Standard User is given
  15 Units for use on the actual quantum hardware. Request a
  replenishment of Units via the Account page. Once you have gotten
  familiar with the tool, tell us about yourself and request an upgrade
  to the Expert User level. 

How do I join IBM Quantum Computing?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We are always interested in meeting the brightest and most inquisitive
minds! Are you a `quantum
thinker <http://ibm-research.jobs/l/recruiting/jobsearchaction/1ed388e3-9ff9-11e4-b295-bc764e10782d/4fc7376b-11b4-11e6-bc9f-bc764e11b6f3/false?term=quantum&tags=&jobTypes=&locations=&postalCode=&distance=1000000>`__? 
