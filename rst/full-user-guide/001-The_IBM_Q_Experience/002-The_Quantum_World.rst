The Quantum World
=================

Today’s computers perform calculations and process information using the
standard (or as a physicist would say, “classical”) model of
computation, which dates back to
`Turing <https://en.wikipedia.org/wiki/Alan_Turing>`__ and `von
Neumann <https://en.wikipedia.org/wiki/John_von_Neumann>`__. In this
model, all information is reducible to bits, which can take the values
of either 0 or 1 - and all processing can be performed via simple
`logic gates <https://en.wikipedia.org/wiki/Logic_gate>`__ (AND, OR,
NOT, NAND) acting on one or two bits at a time. At any point in its
computation, a classical computer’s state is entirely determined by the
states of all its bits, so that a computer with :math:`n` bits can exist in
one of :math:`2^n` possible states, ranging from :math:`00...0`  to :math:`11...1`.

The power of the quantum computer, meanwhile, lies in its much richer
repertoire of states. A quantum computer also has bits - but instead of 0
and 1, its quantum bits, or *qubits*, can represent a 0, 1, or linear combination of both, 
which is a property known as **superposition**. This on its own is
no special thing, since a computer whose bits can be intermediate
between 0 and 1 is just an analog computer, scarcely more powerful than
an ordinary digital computer. However, a quantum computer takes
advantage of a special kind of superposition that allows for *exponentially many* 
logical states at once, all the states from
:math:`|00...0\rangle` to :math:`|11...1\rangle`. This is a powerful feat, and
no classical computer can achieve it. The vast majority of these quantum
superpositions, and the ones most useful for quantum computation, are
**entangled** - they are states of the whole computer that do not
correspond to any assignment of digital or analog states of the
individual qubits. While not as powerful as exponentially many classical
computers, a quantum computer is significantly more powerful than any
one classical computer - whether it be deterministic, probabilistic, or
analog. For a few famous problems (such as factoring large numbers), a
quantum computer is clearly the winner over a classical computer. A
working quantum computer could factor numbers in a day that would take a
classical computer millions of years.

One might think that the difficulty in understanding quantum computing
or quantum physics lies in "hard math"... but mathematically, quantum
concepts are only a bit more complex than high school algebra. Quantum
physics is hard because, like Einstein’s theory of relativity, it
requires internalizing ideas that are simple but counter-intuitive.
What is strange about relativity is the concept that time and space
are interconnected, when common sense tells us they should act
independently. If you begin to explain relativity to a person new to
the idea by jumping straight to time and space, you will likely get
a blank stare in return. A better way to start is as Einstein did, by
explaining that relativity follows from a simple physical principle:
the speed of light is the same for all uniformly moving observers.
This one modest idea then becomes extremely profound and leads, by
inexorable logic, to Einsteinian spacetime.

The counter-intuitive ideas of quantum physics are: 

1. *a physical system in a* **definite state** *can still behave* **randomly**. 
2. *two systems that are* **too far apart** *to influence each other can nevertheless behave in ways that, though* **individually random**, *are somehow* **strongly correlated**. 

Unfortunately, unlike relativity, there is no single simple physical principle from
which these conclusions follow. The best we can do is to distill
quantum mechanics down to a few abstract-sounding mathematical laws,
from which all the observed behavior of quantum particles (and qubits
in a quantum computer) can be deduced and predicted. And, as with
relativity, we must guard against attempting to describe quantum
concepts in classical terms.
