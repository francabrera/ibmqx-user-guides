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

Suppose our task is to factor an integer $$N$$ with $$d$$ decimal
digits. The brute force algorithm goes through all primes $$p$$ up to
$$\\sqrt{N}$$ and checks whether $$p$$ divides $$N$$. In the worst case,
this would take time roughly $$\\sqrt{N}$$ which is exponential in the
number of digits $$d$$.  A more efficient algorithm known as the
quadratic sieve attempts to construct integers $$a,b$$ such that
$$a^2-b^2$$ is a multiple of $$N$$. Once such $$a,b$$ are found, one
checks whether $$a\\pm b$$ have common factors with $$N$$.  The
quadratic sieve method has asymptotic runtime exponential in
$$\\sqrt{d}$$. The most efficient classical factoring algorithm known as
general number field sieve achieves an asymptotic runtime exponential in
$$d^{1/3}$$.  The exponential runtime scaling limits applicability of
the classical factoring algorithms to numbers with a few hundred digits
 with the world record being $$d=232$$ (which took roughly 2,000 CPU
years).  In contrast, Shor's factoring algorithm has runtime
*polynomial* in $$d$$. The version of the algorithm described below due
to Alexey Kitaev requires roughly $$10d$$ qubits and has runtime
 roughly $$d^3$$.  

|image0|    ** **

| **Figure 1: classical vs quantum factoring algorithms**

**Period finding**.﻿﻿ ﻿
^^^^^^^^^^^^^^^^^^^^^^^

It has been known to mathematicians since 1970's that factoring becomes
easy if one can solve another hard problem: find a period of the modular
exponential function. The period finding problem is defined as
follows. Given integers $$N$$ and $$a$$, find the smallest positive
integer $$r$$  such that $$a^r-1$$ is a multiple of $$N$$. The number
$$r$$ is called the period of $$a$$ modulo $$N$$. Recall that in modular
arithmetics the remainder of a division $$a/N$$ is called the value of
$$a$$ modulo $$N$$ and denoted $$a\\pmod{N}$$. For example, $$1=16=91
\\pmod{15}$$. Thus the period of $$a$$ modulo $$N$$ is the smallest
positive integer $$r$$ such that $$a^r=1{\\pmod N}$$. For example,
suppose $$N=15$$ and $$a=7$$. Then 

| |image1|

that is, $$7$$ has period $$4$$ modulo $$15$$. Note that computing the
higher powers of $$7$$ would give rise to a periodic sequence:
$$7^{x+4}=7^x\\pmod{15}$$ for any integer $$x$$. Thus $$r=4$$ is the
period of the modular exponential function $$7^x$$.  In general the
period finding problem is well-defined if $$N$$ and $$a$$ are co-prime
(have no common factors). 

**From factoring to period finding**. 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Assume for a moment that we are given a period finding machine that
takes as input co-prime integers $$N,a$$ and outputs the period of $$a$$
modulo $$N$$. Let us show how to use the machine to find all prime
factors of $$N$$. For simplicity, assume that $$N$$ has only two
distinct prime factors:

| |image2|

First, pick a random integer $$a$$ between $$2$$ and $$N-1$$ and compute
the greatest common divisor gcd$$(N,a)$$. This can be done very
efficiently using `Euclid's
algorithm <http://en.wikipedia.org/wiki/Euclidean_algorithm>`__. If we
are lucky, $$N$$ and $$a$$ have some common prime factors in which case
gcd$$(N,a)$$ equals $$p\_1$$ or $$p\_2$$, so we are done. From now on
let us assume that gcd$$(N,a)=1$$, that is, $$N$$ and $$a$$ are
co-prime. Let $$r$$ be the period of $$a$$ modulo $$N$$ computed by the
machine. Repeat the above steps with different random choices of $$a$$
until $$r$$ is even.  It can be shown that a significant fraction of all
integers $$a$$  has even period, see Table 1 for examples, so on average
one needs only a few repetitions.  At this point we have found some pair
$$r,a$$ such that $$r$$ is even and $$r$$ is the smallest integer such
that $$a^r-1$$ is a multiple of $$N$$. Let us use the identity 

| |image3|

| The above shows that $$a^{r/2}-1$$ is not a multiple of $$N$$
  (otherwise the period of $$a$$ would be $$r/2$$). Assume for a moment
  that $$a^{r/2}+1$$ is not a multiple of $$N$$. Then neither of the
  integers $$a^{r/2}\\pm 1$$ is a multiple of $$N$$, but their product
  is.  This is possible only if $$p\_1$$ is a prime factor of
  $$a^{r/2}-1$$ and $$p\_2$$ is a prime factor of $$a^{r/2}+1$$ (or vice
  verse). Thus we can find $$p\_1$$ and $$p\_2$$ by computing
  gcd$$(N,a^{r/2}\\pm 1)$$, see Table 1 for examples.  In the remaining
  \`\`unlucky" case when $$a^{r/2}+1$$ is a multiple of $$N$$ we give up
  and try a different integer $$a$$.  For example, $$a=14$$ is the only
  unlucky integer in Table 1. In general,  it can be shown that the
  unlucky integers $$a$$ are not too frequent, so on average only two
  calls to the period finding machine are sufficient to factor $$N$$.

| |image4|    
| **Table 1: period of integers $$a$$ modulo $$15$$**

                                                                     

**Shor's algorithm**. 
^^^^^^^^^^^^^^^^^^^^^^

| Let us now show that a quantum computer can efficiently simulate the
  period finding machine.  As in the case of the\ `Deutsch-Jozsa
  algorithm </qstage/#/tutorial?sectionId=8443c4f713521c10b1a56a533958286b&pageIndex=3>`__,
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

Suppose we are given co-prime integers $$a,N$$. Our goal is compute the
period of $$a$$ modulo $$N$$, that is, the smallest positive integer
$$r$$ such that $$a^r=1\\pmod{N}$$. The basic idea is to construct a
unitary operator $$U\_a$$ that implements the modular
multiplication function $$x\\to ax \\pmod{N}$$. It can be shown that
eigenvalues of $$U\_a$$ are closely related to the period of $$a$$.
Namely, each eigenvalue of $$U\_a$$ has a form $$e^{i\\phi}$$, where
$$\\phi=2\\pi k/r$$ for some integer $$k$$. Furthermore, as we saw in
the previous section, eigenvalues of certain unitary operators can be
measured efficiently using the phase estimation
algorithm. Unfortunately, inferring $$r$$ from the measured eigenvalues
of $$U\_a$$ is only possible if the eigenvalues are measured *exactly*
(or with an exponentially small precision). For example, factoring a
1,000-digit number would require measuring the eigenvalue of $$U\_a$$
with a precision $$10^{-2000}$$. Such accuracy cannot be achieved by a
direct application of the phase estimation algorithm as this would
require too large pointer system. Here comes the main trick: we shall
estimate the eigenvalue of $$U\_a$$ by applying the phase estimation
algorithm to a family of unitary operators $$U\_b$$ with
$$b=a,a^2,a^4,a^8$$ etc. We stop at $$b=a^{2^p}$$ with $$2^p\\approx
N^2$$. Why does it work? The first observation is that  all operators
$$U\_b$$ are integer powers of $$U\_a$$. Namely, if $$b=a^t$$ then
$$U\_b=(U\_a)^t$$. This implies that the operators $$U\_b$$  have the
same eigenvectors. In particular, eigenvalues of the entire family
$$U\_b$$ can be measured simultaneously.  Second, implementing $$U\_b$$
is as easy as implementing $$U\_a$$ - one just need to precompute the
powers $$b=a,a^2,a^4,a^8,\\ldots \\pmod{N}$$ by the repeated squaring
method. Finally, even if the eigenvalues of $$U\_b$$ are measured with a
poor precision (say 10%), each squaring of $$a$$ reduces the error in
the estimated eigenvalue of $$U\_a$$ by a factor $$1/2$$.  Indeed,
consider an eigenvector of $$U\_a$$ with an eigenvalue
$$e^{i\\phi}$$. If $$b=a^2$$ then the eigenvalue of $$U\_b$$ is
$$e^{2i\\phi}$$. If $$b=a^4$$ then the eigenvalue of $$U\_b$$  is
$$e^{4i\\phi}$$ etc. Thus we can estimate
$$\\phi,2\\phi,4\\phi,\\ldots,2^p\\phi$$ with a constant precision (say
10%). We shall see that this is enough to estimate $$\\phi$$ with a
precision roughly $$2^{-p}$$.  For example,  one can achieve a precision
$$10^{-2000}$$ by a sequence of less than $$10^6$$  lousy measurements
of $$U\_b$$ with an error 10%. Furthermore, it can be shown that
estimating a few randomly picked eigenvalues $$\\phi=2\\pi k/r$$ with a
precision less than $$1/N^2$$ is enough to determine the period $$r$$
exactly (the idea is to find the best rational approximation to the
estimate of $$k/r$$ using continued fractions).

In order to use the phase estimation algorithm we need to construct a
quantum circuit implementing the modular multiplication operator. By
analogy with classical algorithms that can link standard library
functions, a quantum algorithm is allowed to call classical subroutines,
for example a subroutine for computing the modular multiplication.
Importantly, before such classical subroutines are incorporated into a
quantum circuit, they must be transformed into a *reversible
form. *\ More precisely, a quantum algorithm can call a classical
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
  form. How does it work? Suppose $$f(x)$$ represents some classical
  computation that takes as input $$n$$-bit strings $$x$$ and outputs
  $$m$$-bit strings $$f(x)$$. The first observation is that the answer
  $$f(x)$$ can be computed without erasing any intermediate data if we
  are allowed to use some extra memory. Indeed, let us write down an
  algorithm for computing $$f(x)$$ and compile it into a sequence of
  elementary logical gates such as AND, OR, etc. For concreteness,
  assume that each gate has two input wires and one output wire.  Let
  $$L$$ be the total number of gates. We shall extend the $$n$$-bit
  memory storing the input $$x$$ by adding $$L$$ bits initialized by
  zeros. These extra bits will serve as a scratch memory for storing
  intermediate data. We shall write the output of the  $$i$$-th gate to
  the $$i$$-th bit of the scratch memory and keep the values of
  the input bits. Once the computation is completed, the final answer
  $$f(x)$$ is contained in some designated output register within the
  scratch memory. The remaining part of the scratch memory contains some
  "garbage" bit string $$g(x)$$ (intermediate data).  Below we
  illustrate how it works for the example when $$f(x)$$ computes the
  3-bit Majority function. 

| |image5|

At this point the circuit is reversible as a whole, but its individual
gates are still irreversible. The next step is to transform each gate
into a reversible form. Consider as an example the AND gate with input
wires $$a,b$$ and output wire $$c$$ such that $$c=a\\wedge b$$. Let us
define its reversible version R-AND. One of the output wires of R-AND
must carry the output bit $$c$$ of the standard AND gate. To avoid
losing information, R-AND must have at least two other output wires
(note that in the case $$c=0$$ there are three possible input strings:
$$ab=00,01,10$$). The simplest version of R-AND has three input wires
and three output wires as shown below.

| |image6|

Here $$d$$ is a dummy input wire and $$\\oplus$$ denotes XOR operation
(addition modulo two). The gate expects to receive inputs with $$d=0$$
in which case $$c=a\\wedge b$$. If $$d=1$$ then the output data bit if
flipped. Note that all inputs of R-AND can be computed from its outputs
since $$d=c\\oplus (a\\wedge b)$$. Thus R-AND indeed acts reversibly
(technically, R-AND realizes a permutation on the set of 3-bit strings).
Note also that R-AND coincides with the `Toffoli
gate </qstage/#/tutorial?sectionId=8443c4f713521c10b1a56a533958286b&pageIndex=1>`__.
The same construction can be applied to any other gate with two input
wires and one output wire. Namely, if a gate F computes some Boolean
function $$c=F(a,b)$$ then its reversible version R-F would map inputs
$$a,b,d$$ to outputs $$a,b,c$$ where $$c=d\\oplus F(a,b)$$, see below.
Note that applying R-F twice implements the identity gate, that is, R-F
coincides with its own inverse. 

| |image7|

Suppose the original circuit is described by a sequence of $$L$$ gates
$$F\_1,\\ldots,F\_L$$. Replace each gate  $$F\_i$$  by its reversible
version $$G\_i=R$$-$$F\_i$$ constructed above.  We shall connect the
dummy input wire of $$G\_i$$ and its output wire $$c$$ to the $$i$$-th
bit of the scratch memory such that the gate always receives inputs with
$$d=0$$. The new circuit has $$n+L$$ input and $$n+L$$ output wires and
is composed from reversible $$3$$-bit gates. The final state generated
by the circuit can be written as $$x,g(x),f(x)$$, where $$f(x)$$ is the
final answer stored in the output register somewhere within the scratch
memory and $$g(x)$$ represents \`\`garbage" (intermediate data). Here we
assumed that the scratch memory is initially clean (all zeros). Thus we
have constructed a reversible circuit that maps $$x,0^L$$ to
$$x,g(x),f(x)$$. The final step is to get rid of the garbage $$g(x)$$
without erasing any information (which would render the circuit
irreversible). A solution is to copy the answer $$f(x)$$ to a clean
ancillary register of $$m$$ bits and then \`\`uncompute" $$f(x)$$ by
applying the circuit backwards in time. Below we sketch how this works.

 |image8|

Ignoring for simplicity all ancillary bits  that are initialized and
returned in the zero state, we obtained a reversible circuit on $$n+m$$
bits that maps input strings $$x,y$$ to output strings $$x,y\\oplus
f(x)$$. In the special case when the $$f(x)$$ is invertible one can use
similar tricks to  construct a reversible circuit that maps input
strings $$x$$ to output strings $$f(x)$$.  In practice, one would never
use the method described above since it requires too large scratch
memory. Several optimization techniques for constructing reversible
circuits have been proposed (such as uncomputing partial results more
often and reusing scratch memory bits). 

**Quantum circuits for modular multiplication**. 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Suppose now that  $$f(x)=ax\\pmod{N}$$ is the modular multiplication
function. Let $$n$$ be the number of binary digits in $$N$$. Using
$$n$$-bit strings to represent integers modulo $$N$$, one can implement
 $$f(x)$$ by a classical circuit $$U\_a$$ composed of 3-bit reversible
gates with $$n$$ input and output wires, as described above. The circuit
$$U\_a$$ may also use ancillary bits that are initialized and returned
in the 0 state. The state-of-the-art implementation would require
roughly $$n^2$$ gates and roughly $$2n$$ ancillary bits. For simplicity,
below we shall often ignore the ancillary bits.  Let us convert $$U\_a$$
to a quantum circuit  by replacing each classical gate with its quantum
counterpart. This is possible because, by construction, each gate of
$$U\_a$$ implements some permutation on the set of input bit strings
$$000,001,\\ldots,111$$. The corresponding quantum gate implements the
same permutation on the set of basis states
$$\|000\\rangle,\|001\\rangle,\\ldots,\|111\\rangle$$. We obtained a
quantum circuit  $$U\_a$$ acting on a register of $$n$$ qubits that maps
a basis state $$\|x\\rangle$$ to $$\|f(x)\\rangle$$. An example for
$$f(x)=7x\\pmod{15}$$ is shown below. Period finding algorithm requires
modular multiplication circuits $$U\_b$$ for
$$b=a,a^2,a^4,\\ldots,a^{2^p} \\pmod{N}$$, where $$2^p\\approx N^2$$.

| |image9|         
| **some basis states representing integers modulo $$15$$**

| 

| |image10|           
| **Modular multiplication operator  maps $$\|x\\rangle$$ to $$\|7x
  \\pmod{15}\\rangle$$**

   This quantum circuit implements $$U\_7$$ (see `Markov and Saeedi
2012 <http://arxiv.org/abs/1202.6614>`__) 

  |image11|       

**﻿Controlled operations and phase estimation**.﻿ 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let $$U=U\_a$$ be the modular multiplication operator. At this point we
know how to construct a quantum circuit implementing $$U$$ as well as
repeated squares of $$U$$ such as $$U^2,U^4,U^8$$, etc.  We also know
that eigenvalues of $$U$$ reveal information about the period of $$a$$
modulo $$N$$. The final step is to measure the eigenvalues. For that we
shall need a controlled version of $$U$$. A controlled unitary operator
is a quantum analogue of classical conditional statements such as
if-then-else. We already saw examples of controlled quantum
gates\ `earlier in the
tutorial </qstage/#/tutorial?sectionId=8443c4f713521c10b1a56a533958286b&pageIndex=1>`__. In
general, suppose $$U$$ is a quantum circuit acting on $$n$$ qubits. A
controlled version of $$U$$  is a unitary operator acting on a larger
system control+target, where control is a single qubit and target is a
register of $$n$$ qubits. Controlled-$$U$$ applies $$U$$ to the target
register if the control qubit is :math:`|1\rangle` state and does nothing
if the control qubit is :math:`|0\rangle`.

| |image12|
| Like their classical counterparts, controlled quantum operations are
  used in almost any quantum algorithm. We note that if $$U$$ can be
  realized by a short quantum circuit then so does
  controlled-$$U$$. Indeed, one can take the circuit realizing $$U$$ and
  replace each gate by its controlled version (with the same control
  qubit). The main distinction from the classical if-then-else construct
   is that the controlled qubit can be in a superposition of state
  $$\\alpha\|0\\rangle +\\beta\|1\\rangle$$. One could say that in the
  quantum world two branches of a conditional statement can be executed
  "at the same time".  Consider now a special case when the target
  register is prepared in some state $$\\psi$$ which is an eigenvector
  of  $$U$$, that is $$U\|\\psi\\rangle=e^{i\\phi}
  \|\\psi\\rangle$$. Then the only difference between the two branches
  of the controlled-$$U$$ operation is the phase shift $$e^{i\\phi}$$.
  In other words, the control qubit gets mapped from
   $$\\alpha\|0\\rangle+\\beta\|1\\rangle$$ to $$\\alpha\|0\\rangle
  +e^{i\\phi}\\beta \|1\\rangle$$, while the target register remains in
  the state $$\\psi$$. Thus we can describe that the action of
  controlled-$$U$$ on the composite system control+target by a
  single-qubit phase shift gate $$P$$ acting on the control qubit.

| |image13|

Below we focus on what happens with the control qubit only (keeping in
mind that it is part of the larger system control+target).  We shall
measure the eigenvalue $e^{i\\phi}$ using a pair of phase estimation
circuits shown below. 

| |image14|

| One can easily check that the probability of observing the measurement
  outcome $$0$$ is $$0.5(1+\\cos{(\\phi)})$$ for the first circuit and
  $$0.5(1-\\sin{(\\phi)})$$ for the second circuit.  One should keep in
  mind that $$P$$ represents the controlled-$$U$$ operator, so the
  circuit extracts information about the phase $$\\phi$$ by measuring
  interference between two branches of controlled-$$U$$ where one branch
  accumulates a phase factor $$e^{i\\phi}$$ and the other branch
  accumulates no phase. By repeating each circuit several time and
  collecting the measurement statistics we can estimate the
  probabilities which gives us an estimate $$\\phi$$. For concreteness,
  assume that we are willing to perform at most 100 measurements. Then
  the statistical error in our estimate of $$\\phi$$ is roughly 10%.
| To factor a number $$N$$ with 1,000 decimal digits the phase $$\\phi$$
  has to be estimated with a very high precision $$\\epsilon \\sim 1/N^2
  \\sim 10^{-2000}$$. To this end we shall perform the phase estimation
  for a family of unitary operators $$U^t$$, where $$t=1,2,4,8$$ etc. We
  stop at $$t=2^p$$ such that $$2^p\\approx 1/\\epsilon$$. Recall that
  we can efficiently implement $$U^t$$ for very large values of $$t$$
   by classically computing $$b=a^{t}\\pmod{N}$$ and using the identity
  $$U^t=(U\_a)^t=U\_b$$. Since all operators $$U^t$$ have the same
  eigenvector $$\\psi$$, we can do all phase estimations with the same
  target register (initialized in the eigenvector
  $$\|\\psi\\rangle$$). For simplicity, let us assume that the phase
  estimations are performed sequentially in which case only one control
  qubit is needed. The controlled-$$U^2$$ operator gives rise to a phase
  shift $$P^2$$ by angle $$2\\phi$$ on the control qubit. Thus we can
  estimate $$2\\phi$$ with a precision 10%  by performing roughly 100
  measurements. This gives an estimate of $$\\phi$$  with a precision
  5%.  More precisely, since the phase $$\\phi$$ lives on the unit
  circuit, we get a pair of candidate angles $$\\phi'$$ and
  $$\\phi''=\\phi'+\\pi$$ such that one of them approximates $$\\phi$$
  with a precision 5% and the other is very far from $$\\phi$$
  (approximately by:math:`\pi`).  However, we have already estimated
  $$\\phi$$ itself with a precision 10%. This is enough to select one of
  the candidate angles $$\\phi'$$ and $$\\phi''$$. Applying this
  argument inductively several times shows that estimating
   $$\\phi,2\\phi,\\ldots,2^p\\phi$$ with a constant precision (say,
  10%) is enough to estimate $$\\phi$$ with a precision roughly
  $$2^{-p}\\sim \\epsilon$$. Overall we would need approximately
  $$M=100\\log\_2{(1/\\epsilon)}\\sim 10^6$$ measurements which
  translates to $$10^6$$ controlled modular multiplication operators. In
  general, $$M$$ scales as $$\\log{(N)}$$ with some extra factors doubly
  logarithmic in $$N$$. Since each controlled modular multiplication
  operator requires a quantum circuit of size $$\\log^2{(N)}$$, the
  overall complexity of the factoring algorithm scales as
  $$\\log^3{(N)}\\sim d^3$$. 

We have not explained yet how to initialize the target register in the
eigenvector of $$U$$. Fortunately, all eigenvectors are equally good for
our purposes: we are not interested in any particular eigenvalue  but
rather want to measure a random eigenvalue drawn from the uniform
distribution. Thus one can initialize the target register in an
arbitrary state that has equal weight on each eigenvector of $$U$$. For
example, one can choose the initial state as the basis vector
$$\|0\\ldots01\\rangle$$ encoding the integer $$x=1$$. 

**
**

| 

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

