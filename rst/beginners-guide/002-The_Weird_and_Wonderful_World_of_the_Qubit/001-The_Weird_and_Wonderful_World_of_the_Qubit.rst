The Weird and Wonderful World of the Qubit
==========================================

.. toctree::
   :maxdepth: 1
   :glob:
   :hidden:

..
   *

Now that we have a basic understanding of quantum properties and how to 
use the Quantum Composer, let's dive into the weird and wonderful world of the qubit!

A **qubit** (short for **quantum bit**) is a quantum system consisting of 
two energy levels, labeled :math:`|0\rangle` and :math:`|1\rangle`. 
The :math:`|0\rangle` state is often called the ground state because it 
is the lower of the two energies. Together, :math:`|0\rangle` and :math:`|1\rangle` 
make up what we call“standard basis vectors”. Like all vectors, they point in a direction 
and have a magnitude. Defining basis vectors is a really useful trick we 
have borrowed from linear algebra. The basic idea is that once you have 
defined these vectors, you can construct any other vector from a linear 
combination of the basis vectors. 

| 

Additionally, qubits also have a **phase**, which results from the fact
that superpositions can be complex. To represent these superpositions,
we put a coefficient such as a or b in front of the state like so:
:math:`a|0\rangle+ b|1\rangle`. Here’s what the formula is saying:
“The state is made up of a linear combination of :math:`|0\rangle` and
:math:`|1\rangle`, where the proportion of each depends on the
coefficients :math:`a` and :math:`b`.” The coefficients :math:`a` and :math:`b` could
be positive, negative, or even complex. If we take the absolute value
of :math:`a` or :math:`b` and square it (e.g. :math:`|a|^2`﻿or :math:`|b|^2` ), we
get the probability of measuring the \ **0** or **1** outcome, respectively.

| 

In this chapter, we will dig deeper into how we can use single qubit gates to manipulate quantum states, as well as the concepts of superposition and phase.
