Shor's algorithm
================

| Although any integer number has a unique decomposition into a product
  of primes, finding the prime factors is believed to be a hard problem.
  In fact, the security of our online transactions rests on the
  assumption that factoring integers with a thousand or more digits is
  practically impossible. This assumption has been challenged in 1995
  when Peter Shor proposed a polynomial-time quantum algorithm for the
  factoring problem. Shor's algorithm is arguably the most dramatic
  example of how the paradigm of quantum computing changed our
  perception of which problems should be considered tractable. In this
  section we briefly summarize some basic facts about factoring,
  highlight main ingredients of the Shor's algorithm, and illustrate how
  it works using a toy factoring problem.

**Complexity of factoring**. 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Suppose our task is to factor an integer :math:`N` with :math:`d` decimal
digits. The brute force algorithm goes through all primes :math:`p` up to
:math:`\sqrt{N}` and checks whether :math:`p` divides :math:`N`. In the worst case,
this would take time roughly :math:`\sqrt{N}` which is exponential in the
number of digits :math:`d`.  A more efficient algorithm known as the
quadratic sieve attempts to construct integers :math:`a,b` such that
:math:`a^2-b^2` is a multiple of :math:`N`. Once such :math:`a,b` are found, one
checks whether :math:`a\pm b` have common factors with :math:`N`.  The
quadratic sieve method has asymptotic runtime exponential in
:math:`\sqrt{d}`. The most efficient classical factoring algorithm known as
general number field sieve achieves an asymptotic runtime exponential in
:math:`d^{1/3}`.  The exponential runtime scaling limits applicability of
the classical factoring algorithms to numbers with a few hundred digits
 with the world record being :math:`d=232` (which took roughly 2,000 CPU
years).  In contrast, Shor's factoring algorithm has runtime
*polynomial* in :math:`d`. The version of the algorithm described below due
to Alexey Kitaev requires roughly :math:`10d` qubits and has runtime
 roughly :math:`d^3`.  

|image0|    ** **

| **Figure 1: classical vs quantum factoring algorithms**

**Period finding**.﻿﻿ ﻿
^^^^^^^^^^^^^^^^^^^^^^^

It has been known to mathematicians since 1970's that factoring becomes
easy if one can solve another hard problem: find a period of the modular
exponential function. The period finding problem is defined as
follows. Given integers :math:`N` and :math:`a`, find the smallest positive
integer :math:`r`  such that :math:`a^r-1` is a multiple of :math:`N`. The number
:math:`r` is called the period of :math:`a` modulo :math:`N`. Recall that in modular
arithmetics the remainder of a division :math:`a/N` is called the value of
:math:`a` modulo :math:`N` and denoted :math:`a\pmod{N}`. For example, :math:`1=16=91
\pmod{15}`. Thus the period of :math:`a` modulo :math:`N` is the smallest
positive integer :math:`r` such that :math:`a^r=1{\pmod N}`. For example,
suppose :math:`N=15` and :math:`a=7`. Then 

| |image1|

that is, :math:`7` has period :math:`4` modulo :math:`15`. Note that computing the
higher powers of :math:`7` would give rise to a periodic sequence:
:math:`7^{x+4}=7^x\pmod{15}` for any integer :math:`x`. Thus :math:`r=4` is the
period of the modular exponential function :math:`7^x`.  In general the
period finding problem is well-defined if :math:`N` and :math:`a` are co-prime
(have no common factors). 

**From factoring to period finding**. 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Assume for a moment that we are given a period finding machine that
takes as input co-prime integers :math:`N,a` and outputs the period of :math:`a`
modulo :math:`N`. Let us show how to use the machine to find all prime
factors of :math:`N`. For simplicity, assume that :math:`N` has only two
distinct prime factors:

| |image2|

First, pick a random integer :math:`a` between :math:`2` and :math:`N-1` and compute
the greatest common divisor gcd:math:`(N,a)`. This can be done very
efficiently using `Euclid's
algorithm <http://en.wikipedia.org/wiki/Euclidean_algorithm>`__. If we
are lucky, :math:`N` and :math:`a` have some common prime factors in which case
gcd:math:`(N,a)` equals :math:`p_1` or :math:`p_2`, so we are done. From now on
let us assume that gcd:math:`(N,a)=1`, that is, :math:`N` and :math:`a` are
co-prime. Let :math:`r` be the period of :math:`a` modulo :math:`N` computed by the
machine. Repeat the above steps with different random choices of :math:`a`
until :math:`r` is even.  It can be shown that a significant fraction of all
integers :math:`a`  has even period, see Table 1 for examples, so on average
one needs only a few repetitions.  At this point we have found some pair
:math:`r,a` such that :math:`r` is even and :math:`r` is the smallest integer such
that :math:`a^r-1` is a multiple of :math:`N`. Let us use the identity 

| |image3|

| The above shows that :math:`a^{r/2}-1` is not a multiple of :math:`N`
  (otherwise the period of :math:`a` would be :math:`r/2`). Assume for a moment
  that :math:`a^{r/2}+1` is not a multiple of :math:`N`. Then neither of the
  integers :math:`a^{r/2}\pm 1` is a multiple of :math:`N`, but their product
  is.  This is possible only if :math:`p_1` is a prime factor of
  :math:`a^{r/2}-1` and :math:`p_2` is a prime factor of :math:`a^{r/2}+1` (or vice
  verse). Thus we can find :math:`p_1` and :math:`p_2` by computing
  gcd:math:`(N,a^{r/2}\pm 1)`, see Table 1 for examples.  In the remaining
  \`\`unlucky" case when :math:`a^{r/2}+1` is a multiple of :math:`N` we give up
  and try a different integer :math:`a`.  For example, :math:`a=14` is the only
  unlucky integer in Table 1. In general,  it can be shown that the
  unlucky integers :math:`a` are not too frequent, so on average only two
  calls to the period finding machine are sufficient to factor :math:`N`.

| |image4|    
| **Table 1: period of integers :math:`a` modulo :math:`15`**

                                                                     

**Shor's algorithm**. 
^^^^^^^^^^^^^^^^^^^^^^

| Let us now show that a quantum computer can efficiently simulate the
  period finding machine.  As in the case of the\ `Deutsch-Jozsa
  algorithm <rst/full-user-guide/004-Quantum_Algorithms/080-Deutsch-Jozsa_Algorithm.rst>`__,
  we shall exploit quantum parallelism and constructive interference to
  determine whether a complicated function has a certain global property
  that cannot be learned by evaluating the function only at a few
  points. However, instead of detecting the property of being a balanced
  function, we seek to detect and measure periodicity of the modular
  exponentiation function. The fact that interference makes it easier to
  measure periodicity should not come as a big surprise. After all,
  physicists routinely use scattering of electromagnetic waves and
  interference measurements to determine periodicity of physical objects
  such as crystal lattices. Likewise, Shor's algorithm exploits
  interference to measure periodicity of arithmetic objects.

Suppose we are given co-prime integers :math:`a,N`. Our goal is compute the
period of :math:`a` modulo :math:`N`, that is, the smallest positive integer
:math:`r` such that :math:`a^r=1\pmod{N}`. The basic idea is to construct a
unitary operator :math:`U_a` that implements the modular
multiplication function :math:`x\to ax \pmod{N}`. It can be shown that
eigenvalues of :math:`U_a` are closely related to the period of :math:`a`.
Namely, each eigenvalue of :math:`U_a` has a form :math:`e^{i\phi}`, where
:math:`\phi=2\pi k/r` for some integer :math:`k`. Furthermore, as we saw in
the previous section, eigenvalues of certain unitary operators can be
measured efficiently using the phase estimation
algorithm. Unfortunately, inferring :math:`r` from the measured eigenvalues
of :math:`U_a` is only possible if the eigenvalues are measured *exactly*
(or with an exponentially small precision). For example, factoring a
1,000-digit number would require measuring the eigenvalue of :math:`U_a`
with a precision :math:`10^{-2000}`. Such accuracy cannot be achieved by a
direct application of the phase estimation algorithm as this would
require too large pointer system. Here comes the main trick: we shall
estimate the eigenvalue of :math:`U_a` by applying the phase estimation
algorithm to a family of unitary operators :math:`U_b` with
:math:`b=a,a^2,a^4,a^8` etc. We stop at :math:`b=a^{2^p}` with :math:`2^p\approx
N^2`. Why does it work? The first observation is that  all operators
:math:`U_b` are integer powers of :math:`U_a`. Namely, if :math:`b=a^t` then
:math:`U_b=(U_a)^t`. This implies that the operators :math:`U_b`  have the
same eigenvectors. In particular, eigenvalues of the entire family
:math:`U_b` can be measured simultaneously.  Second, implementing :math:`U_b`
is as easy as implementing :math:`U_a` - one just need to precompute the
powers :math:`b=a,a^2,a^4,a^8,\ldots \pmod{N}` by the repeated squaring
method. Finally, even if the eigenvalues of :math:`U_b` are measured with a
poor precision (say 10%), each squaring of :math:`a` reduces the error in
the estimated eigenvalue of :math:`U_a` by a factor :math:`1/2`.  Indeed,
consider an eigenvector of :math:`U_a` with an eigenvalue
:math:`e^{i\phi}`. If :math:`b=a^2` then the eigenvalue of :math:`U_b` is
:math:`e^{2i\phi}`. If :math:`b=a^4` then the eigenvalue of :math:`U_b`  is
:math:`e^{4i\phi}` etc. Thus we can estimate
:math:`\phi,2\phi,4\phi,\ldots,2^p\phi` with a constant precision (say
10%). We shall see that this is enough to estimate :math:`\phi` with a
precision roughly :math:`2^{-p}`.  For example,  one can achieve a precision
:math:`10^{-2000}` by a sequence of less than :math:`10^6`  lousy measurements
of :math:`U_b` with an error 10%. Furthermore, it can be shown that
estimating a few randomly picked eigenvalues :math:`\phi=2\pi k/r` with a
precision less than :math:`1/N^2` is enough to determine the period :math:`r`
exactly (the idea is to find the best rational approximation to the
estimate of :math:`k/r` using continued fractions).

In order to use the phase estimation algorithm we need to construct a
quantum circuit implementing the modular multiplication operator. By
analogy with classical algorithms that can link standard library
functions, a quantum algorithm is allowed to call classical subroutines,
for example a subroutine for computing the modular multiplication.
Importantly, before such classical subroutines are incorporated into a
quantum circuit, they must be transformed into a *reversible
form.*\ More precisely, a quantum algorithm can call a classical
subroutine only if it is compiled into a sequence of reversible logical
gates such as CNOT or Toffoli gate (in particular, the number of input
and output wires in each gate must be the same). The subroutine is
allowed to use a scratch memory similar to local variables used by the
standard library functions. However, once the subroutine is completed,
the scratch memory must be totally clean (say, all zeros). The reason is
that a quantum algorithm operates on coherent superpositions of
different classical states. Leaving information about the inputs or the
outputs in the scratch memory could potentially destroy quantum
coherence and prevent the algorithm from seeing interference between
different states. Since the notion of reversible classical circuits
 plays an important role in the Shor's algorithm and many other quantum
algorithms, below we briefly discuss methods for constructing such
circuits. 

**Reversible classical circuits**. 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| An important insight made in 1973 by our IBM colleague Charles Bennett
  is that any classical computation can be transformed into a reversible
  form. How does it work? Suppose :math:`f(x)` represents some classical
  computation that takes as input :math:`n`-bit strings :math:`x` and outputs
  :math:`m`-bit strings :math:`f(x)`. The first observation is that the answer
  :math:`f(x)` can be computed without erasing any intermediate data if we
  are allowed to use some extra memory. Indeed, let us write down an
  algorithm for computing :math:`f(x)` and compile it into a sequence of
  elementary logical gates such as AND, OR, etc. For concreteness,
  assume that each gate has two input wires and one output wire.  Let
  :math:`L` be the total number of gates. We shall extend the :math:`n`-bit
  memory storing the input :math:`x` by adding :math:`L` bits initialized by
  zeros. These extra bits will serve as a scratch memory for storing
  intermediate data. We shall write the output of the  :math:`i`-th gate to
  the :math:`i`-th bit of the scratch memory and keep the values of
  the input bits. Once the computation is completed, the final answer
  :math:`f(x)` is contained in some designated output register within the
  scratch memory. The remaining part of the scratch memory contains some
  "garbage" bit string :math:`g(x)` (intermediate data).  Below we
  illustrate how it works for the example when :math:`f(x)` computes the
  3-bit Majority function. 

| |image5|

At this point the circuit is reversible as a whole, but its individual
gates are still irreversible. The next step is to transform each gate
into a reversible form. Consider as an example the AND gate with input
wires :math:`a,b` and output wire :math:`c` such that :math:`c=a\wedge b`. Let us
define its reversible version R-AND. One of the output wires of R-AND
must carry the output bit :math:`c` of the standard AND gate. To avoid
losing information, R-AND must have at least two other output wires
(note that in the case :math:`c=0` there are three possible input strings:
:math:`ab=00,01,10`). The simplest version of R-AND has three input wires
and three output wires as shown below.

| |image6|

Here :math:`d` is a dummy input wire and :math:`\oplus` denotes XOR operation
(addition modulo two). The gate expects to receive inputs with :math:`d=0`
in which case :math:`c=a\wedge b`. If :math:`d=1` then the output data bit if
flipped. Note that all inputs of R-AND can be computed from its outputs
since :math:`d=c\oplus (a\wedge b)`. Thus R-AND indeed acts reversibly
(technically, R-AND realizes a permutation on the set of 3-bit strings).
Note also that R-AND coincides with the `Toffoli
gate <rst/full-user-guide/004-Quantum_Algorithms/061-Basic_Circuit_Identities_and_Larger_Circuits.rst>`__.
The same construction can be applied to any other gate with two input
wires and one output wire. Namely, if a gate F computes some Boolean
function :math:`c=F(a,b)` then its reversible version R-F would map inputs
:math:`a,b,d` to outputs :math:`a,b,c` where :math:`c=d\oplus F(a,b)`, see below.
Note that applying R-F twice implements the identity gate, that is, R-F
coincides with its own inverse. 

| |image7|

Suppose the original circuit is described by a sequence of :math:`L` gates
:math:`F_1,\ldots,F_L`. Replace each gate  :math:`F_i`  by its reversible
version :math:`G_i=R`-:math:`F_i` constructed above.  We shall connect the
dummy input wire of :math:`G_i` and its output wire :math:`c` to the :math:`i`-th
bit of the scratch memory such that the gate always receives inputs with
:math:`d=0`. The new circuit has :math:`n+L` input and :math:`n+L` output wires and
is composed from reversible :math:`3`-bit gates. The final state generated
by the circuit can be written as :math:`x,g(x),f(x)`, where :math:`f(x)` is the
final answer stored in the output register somewhere within the scratch
memory and :math:`g(x)` represents \`\`garbage" (intermediate data). Here we
assumed that the scratch memory is initially clean (all zeros). Thus we
have constructed a reversible circuit that maps :math:`x,0^L` to
:math:`x,g(x),f(x)`. The final step is to get rid of the garbage :math:`g(x)`
without erasing any information (which would render the circuit
irreversible). A solution is to copy the answer :math:`f(x)` to a clean
ancillary register of :math:`m` bits and then \`\`uncompute" :math:`f(x)` by
applying the circuit backwards in time. Below we sketch how this works.

 |image8|

Ignoring for simplicity all ancillary bits  that are initialized and
returned in the zero state, we obtained a reversible circuit on :math:`n+m`
bits that maps input strings :math:`x,y` to output strings :math:`x,y\oplus
f(x)`. In the special case when the :math:`f(x)` is invertible one can use
similar tricks to  construct a reversible circuit that maps input
strings :math:`x` to output strings :math:`f(x)`.  In practice, one would never
use the method described above since it requires too large scratch
memory. Several optimization techniques for constructing reversible
circuits have been proposed (such as uncomputing partial results more
often and reusing scratch memory bits). 

**Quantum circuits for modular multiplication**. 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Suppose now that  :math:`f(x)=ax\pmod{N}` is the modular multiplication
function. Let :math:`n` be the number of binary digits in :math:`N`. Using
:math:`n`-bit strings to represent integers modulo :math:`N`, one can implement
 :math:`f(x)` by a classical circuit :math:`U_a` composed of 3-bit reversible
gates with :math:`n` input and output wires, as described above. The circuit
:math:`U_a` may also use ancillary bits that are initialized and returned
in the 0 state. The state-of-the-art implementation would require
roughly :math:`n^2` gates and roughly :math:`2n` ancillary bits. For simplicity,
below we shall often ignore the ancillary bits.  Let us convert :math:`U_a`
to a quantum circuit  by replacing each classical gate with its quantum
counterpart. This is possible because, by construction, each gate of
:math:`U_a` implements some permutation on the set of input bit strings
:math:`000,001,\ldots,111`. The corresponding quantum gate implements the
same permutation on the set of basis states
:math:`|000\rangle,|001\rangle,\ldots,|111\rangle`. We obtained a
quantum circuit  :math:`U_a` acting on a register of :math:`n` qubits that maps
a basis state :math:`|x\rangle` to :math:`|f(x)\rangle`. An example for
:math:`f(x)=7x\pmod{15}` is shown below. Period finding algorithm requires
modular multiplication circuits :math:`U_b` for
:math:`b=a,a^2,a^4,\ldots,a^{2^p} \pmod{N}`, where :math:`2^p\approx N^2`.

| |image9|         
| **some basis states representing integers modulo :math:`15`**

| 

| |image10|           
| **Modular multiplication operator  maps :math:`|x\rangle` to :math:`|7x
  \pmod{15}\rangle`**

   This quantum circuit implements :math:`U_7` (see `Markov and Saeedi
2012 <http://arxiv.org/abs/1202.6614>`__) 

  |image11|       

**﻿Controlled operations and phase estimation**.﻿ 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let :math:`U=U_a` be the modular multiplication operator. At this point we
know how to construct a quantum circuit implementing :math:`U` as well as
repeated squares of :math:`U` such as :math:`U^2,U^4,U^8`, etc.  We also know
that eigenvalues of :math:`U` reveal information about the period of :math:`a`
modulo :math:`N`. The final step is to measure the eigenvalues. For that we
shall need a controlled version of :math:`U`. A controlled unitary operator
is a quantum analogue of classical conditional statements such as
if-then-else. We already saw examples of controlled quantum
gates\ `earlier in the
tutorial <rst/full-user-guide/004-Quantum_Algorithms/061-Basic_Circuit_Identities_and_Larger_Circuits.rst>`__. In
general, suppose :math:`U` is a quantum circuit acting on :math:`n` qubits. A
controlled version of :math:`U`  is a unitary operator acting on a larger
system control+target, where control is a single qubit and target is a
register of :math:`n` qubits. Controlled-:math:`U` applies :math:`U` to the target
register if the control qubit is :math:`|1\rangle` state and does nothing
if the control qubit is :math:`|0\rangle`.

| |image12|
| Like their classical counterparts, controlled quantum operations are
  used in almost any quantum algorithm. We note that if :math:`U` can be
  realized by a short quantum circuit then so does
  controlled-:math:`U`. Indeed, one can take the circuit realizing :math:`U` and
  replace each gate by its controlled version (with the same control
  qubit). The main distinction from the classical if-then-else construct
   is that the controlled qubit can be in a superposition of state
  :math:`\alpha|0\rangle +\beta|1\rangle`. One could say that in the
  quantum world two branches of a conditional statement can be executed
  "at the same time".  Consider now a special case when the target
  register is prepared in some state :math:`\psi` which is an eigenvector
  of  :math:`U`, that is :math:`U|\psi\rangle=e^{i\phi}
  |\psi\rangle`. Then the only difference between the two branches
  of the controlled-:math:`U` operation is the phase shift :math:`e^{i\phi}`.
  In other words, the control qubit gets mapped from
   :math:`\alpha|0\rangle+\beta|1\rangle` to :math:`\alpha|0\rangle
  +e^{i\phi}\beta |1\rangle`, while the target register remains in
  the state :math:`\psi`. Thus we can describe that the action of
  controlled-:math:`U` on the composite system control+target by a
  single-qubit phase shift gate :math:`P` acting on the control qubit.

| |image13|

Below we focus on what happens with the control qubit only (keeping in
mind that it is part of the larger system control+target).  We shall
measure the eigenvalue :math:`e^{i\phi}` using a pair of phase estimation
circuits shown below. 

| |image14|

| One can easily check that the probability of observing the measurement
  outcome :math:`0` is :math:`0.5(1+\cos{(\phi)})` for the first circuit and
  :math:`0.5(1-\sin{(\phi)})` for the second circuit.  One should keep in
  mind that :math:`P` represents the controlled-:math:`U` operator, so the
  circuit extracts information about the phase :math:`\phi` by measuring
  interference between two branches of controlled-:math:`U` where one branch
  accumulates a phase factor :math:`e^{i\phi}` and the other branch
  accumulates no phase. By repeating each circuit several time and
  collecting the measurement statistics we can estimate the
  probabilities which gives us an estimate :math:`\phi`. For concreteness,
  assume that we are willing to perform at most 100 measurements. Then
  the statistical error in our estimate of :math:`\phi` is roughly 10%.
| To factor a number :math:`N` with 1,000 decimal digits the phase :math:`\phi`
  has to be estimated with a very high precision :math:`\epsilon \sim 1/N^2
  \sim 10^{-2000}`. To this end we shall perform the phase estimation
  for a family of unitary operators :math:`U^t`, where :math:`t=1,2,4,8` etc. We
  stop at :math:`t=2^p` such that :math:`2^p\approx 1/\epsilon`. Recall that
  we can efficiently implement :math:`U^t` for very large values of :math:`t`
   by classically computing :math:`b=a^{t}\pmod{N}` and using the identity
  :math:`U^t=(U_a)^t=U_b`. Since all operators :math:`U^t` have the same
  eigenvector :math:`\psi`, we can do all phase estimations with the same
  target register (initialized in the eigenvector
  :math:`|\psi\rangle`). For simplicity, let us assume that the phase
  estimations are performed sequentially in which case only one control
  qubit is needed. The controlled-:math:`U^2` operator gives rise to a phase
  shift :math:`P^2` by angle :math:`2\phi` on the control qubit. Thus we can
  estimate :math:`2\phi` with a precision 10%  by performing roughly 100
  measurements. This gives an estimate of :math:`\phi`  with a precision
  5%.  More precisely, since the phase :math:`\phi` lives on the unit
  circuit, we get a pair of candidate angles :math:`\phi'` and
  :math:`\phi''=\phi'+\pi` such that one of them approximates :math:`\phi`
  with a precision 5% and the other is very far from :math:`\phi`
  (approximately by :math:`\pi`).  However, we have already estimated
  :math:`\phi` itself with a precision 10%. This is enough to select one of
  the candidate angles :math:`\phi'` and :math:`\phi''`. Applying this
  argument inductively several times shows that estimating
   :math:`\phi,2\phi,\ldots,2^p\phi` with a constant precision (say,
  10%) is enough to estimate :math:`\phi` with a precision roughly
  :math:`2^{-p}\sim \epsilon`. Overall we would need approximately
  :math:`M=100\log_2{(1/\epsilon)}\sim 10^6` measurements which
  translates to :math:`10^6` controlled modular multiplication operators. In
  general, :math:`M` scales as :math:`\log{(N)}` with some extra factors doubly
  logarithmic in :math:`N`. Since each controlled modular multiplication
  operator requires a quantum circuit of size :math:`\log^2{(N)}`, the
  overall complexity of the factoring algorithm scales as
  :math:`\log^3{(N)}\sim d^3`. 

We have not explained yet how to initialize the target register in the
eigenvector of :math:`U`. Fortunately, all eigenvectors are equally good for
our purposes: we are not interested in any particular eigenvalue  but
rather want to measure a random eigenvalue drawn from the uniform
distribution. Thus one can initialize the target register in an
arbitrary state that has equal weight on each eigenvector of :math:`U`. For
example, one can choose the initial state as the basis vector
:math:`|0\ldots01\rangle` encoding the integer :math:`x=1`. 


|
| **Multi7x1Mod15**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=858317af73c7a5ed31f676db5b15913f&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-858317af73c7a5ed31f676db5b15913f.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=858317af73c7a5ed31f676db5b15913f&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Multi7x7Mod15**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=c97d1b1f88e0615685200e6cd6d4b8d2&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-c97d1b1f88e0615685200e6cd6d4b8d2.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=c97d1b1f88e0615685200e6cd6d4b8d2&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Multi7x4Mod15**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=858317af73c7a5ed31f676db5b62695e&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-858317af73c7a5ed31f676db5b62695e.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=858317af73c7a5ed31f676db5b62695e&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **Multi7x13Mod15**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=858317af73c7a5ed31f676db5b9099fd&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-858317af73c7a5ed31f676db5b9099fd.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=858317af73c7a5ed31f676db5b9099fd&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>

|
| **PhaseEstimationTgate**

.. raw:: html

   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=0a1742807714ccbf73df68bbef062fae&sharedCode=true" target="_parent"><img src="https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/codes/code-0a1742807714ccbf73df68bbef062fae.png" style="width: 100%; max-width: 600px;"></a>
   <a href="https://quantumexperience.ng.bluemix.net/qx/editor?codeId=0a1742807714ccbf73df68bbef062fae&sharedCode=true" target="_blank" style="text-align: right; display: block;">Open in composer</a>





.. |image0| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/shor-figure1l0qpbqeb138fr.png
.. |image1| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/shor-equation3fjaulqz4sqe3766r.png
.. |image2| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/shor-equation21ma2bwliskjd1jor.png
.. |image3| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/shor-equation1vm27qee4bcma38fr.png
.. |image4| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/shor-table9nl8715xk3d3rf6r.png
.. |image5| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/majority-example6x8rb37gj64dkj4i.png
.. |image6| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/and-circuit2u342pzqqlnv1jor.png
.. |image7| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/rgatearl3s2mvkon4gqfr.png
.. |image8| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/uncomputel5yqmeuw09gam7vi.png
.. |image9| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/shor-encodingo3tdoo4oaytd42t9.png
.. |image10| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/shor-u79r0hm5m0hot21emi.png
.. |image11| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/multi7xmod159bozodtkjb9h33di.png
.. |image12| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/cont18osk7q79jzx8byb9.png
.. |image13| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/cont22hp10kmu28146lxr.png
.. |image14| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/pejy6u84yb7ucpiudi.png

