Introduction
============

.. toctree::
   :maxdepth: 1
   :glob:
   :hidden:

..
   *

| We’re at the start of a new stage in the information revolution. The
  first stage began around 1950 with a handful of expensive room-sized
  computers, used only by specialists. Today there are more computers in
  the world than people, and we rely on them for everything from
  communication to transportation, commerce, and (of course!) the
  Internet. All of our computers’ varied abilities are produced by
  manipulating zeros and ones using simple operations like **AND**,
  **OR**, and **NOT**, which are called *logic gates*. By doing so
  billions of times per second in billions of places at once, they keep
  our world humming along in the manner to which we have become
  accustomed.
| For over 35 years, IBM has been researching an utterly different kind
  of information and information processing, as different from ordinary
  “classical” information as a dream is from a book. Unlike dreams, this
  new kind of information, called *quantum information*, is both
  well-understood and useful. The basic unit of quantum information is
  called a **qubit** (pronounced CUE-bit), and a machine for storing and
  processing qubits is called a **quantum computer**. We’ve been
  building and testing increasingly powerful quantum computers for
  several years, and last year we made a 5-qubit one, housed at our
  Yorktown lab, available over the Internet to the general public. In
  other words, YOU now have a programmable quantum computer at your
  fingertips! We’ll soon be upgrading our public quantum computer, but
  even five qubits are enough to get a feel for quantum computing.
| Quantum theory, developed in the early 1900’s, revolutionized physics
  and chemistry by successfully explaining the weird behavior of tiny
  particles like atoms and electrons. In the late twentieth century it
  was discovered that it applied not just to these particles, but to
  information itself. This led to a revolution in the science and
  technology of information processing, opening the door to new types of
  computing and communication.
| By going through this Beginner’s Guide, we hope you will learn what’s
  different about quantum computing, and the new possibilities that it
  opens up. Some of these might include designing new materials and
  drugs, searching databases faster, and solving systems of linear
  equations with breathtaking efficiency, in ways that are currently
  impossible. To do all of this, quantum computers will use two
  fundamental properties of the quantum world: **superposition** and
  **entanglement**.
| So, what is **superposition**? Qubits can be in the “:math:`|0\rangle`”
  state (called a zero-ket), the “:math:`|1\rangle`” state (called the
  one-ket), or a linear combination of the two (superposition). The
  half-angle bracket notation :math:`|\rangle` is conventionally used to
  indicate qubits, as opposed to ordinary bits. When you measure the
  :math:`|0\rangle` quantum state, you get a classical 0, and when you
  measure the :math:`|1\rangle` quantum state, you get a classical 1. The
  :math:`|0\rangle` state is sometimes called the ground state because in
  many physical implementations of quantum computing, including ours, it
  is the lowest energy state.

| 

Now, for **entanglement**. Entanglement is a property of many quantum
superpositions and does not have a classical analog. In an entangled
state, the whole system can be described definitively, even though the
parts cannot. Observing one of two entangled qubits causes it to behave
randomly, but tells the observer exactly how the other qubit would act
if observed in a similar manner. Entanglement involves a correlation
between individually random behaviors of the two qubits, so it cannot be
used to send a message. Some people call it “instantaneous action at a
distance,” but this is a misnomer. There is no **action,** but rather
**correlation**; the correlation between the two qubits’ outcomes is
detected only after the two measurements when the observations are
compared. The ability of quantum computers to exist in entangled states
is responsible for much of their extra computing power, as well as many
other feats of quantum information processing that cannot be performed,
or even described, classically.

| 

To learn more about the concepts of superposition and
entanglement, `see <https://www.youtube.com/watch?v=Hi0BzqV_b44>`_ actor
Paul Rudd defeat Stephen Hawking in a game of Quantum Chess. The rules
can be
found `online <https://www.youtube.com/watch?v=jJoDKHKE2gA>`_,
and you
can `watch <https://www.youtube.com/watch?v=LikdmXfWO2A&t=24s>`_ the
inventor of the game, Chris Cantwell, play a friendly game with chess
expert Anna Rudolf. You can also find both a short and longer
introduction to quantum concepts by IBM Fellow `Charlie
Bennett <http://www.research.ibm.com/quantum/expertise.html>`_ on
our website.

If you want to see more of the math and theory behind the concepts, we
encourage you to dig into our full User Guide!

| 

**We anticipate that you will spend about 10-30 min on each section
(with the later sections requiring more time) as you read through this
guide and explore the sample quantum scores on the IBM Q Experience.**


