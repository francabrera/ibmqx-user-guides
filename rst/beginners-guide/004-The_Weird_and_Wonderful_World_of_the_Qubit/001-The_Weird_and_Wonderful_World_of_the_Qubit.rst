The Weird and Wonderful World of the Qubit
==========================================

.. toctree::
   :maxdepth: 1
   :glob:
   :hidden:

..
   *

A qubit is a quantum system consisting of two energy levels, labeled
:math:`|0\rangle` and :math:`|1\rangle`. The :math:`|0\rangle` state is often
called the ground state because it is the lower of the two energies.
Together, :math:`|0\rangle` and :math:`|1\rangle` make up what we call
“standard basis vectors”. Like all vectors, they point in a direction
and have a magnitude. Defining basis vectors is a really useful trick we
have borrowed from linear algebra. The basic idea is that once you have
defined these vectors, you can construct any other vector from a linear
combination of the basis vectors. 

| 
| Additionally, qubits also have a “phase”, which results from the fact
  that superpositions can be complex. To represent these superpositions,
  we put a coefficient such as a or b in front of the state like so:
  :math:`a|0\rangle+ b|1\rangle`. Here’s what the formula is saying:
  “The state is made up of a linear combination of :math:`|0\rangle` and
  :math:`|1\rangle`, where the proportion of each depends on the
  coefficients :math:`a` and :math:`b`.” The coefficients :math:`a` and :math:`b` could
  be positive, negative, or even complex. If we take the absolute value
  of :math:`a` or :math:`b` and square it (e.g. :math:`|a|^2`﻿or :math:`|b|^2` ), we
  get the probability of measuring the \ **0** or **1** outcome,
  respectively.

| 

The basis states :math:`|0\rangle` and :math:`|1\rangle` and their linear
combinations :math:`a|0\rangle`  + :math:`b|1\rangle` describe the state of
a single qubit. But because the coefficients a and b are not just real
numbers, but can be imaginary or even complex, visualizing a qubit
requires a special tool called the Bloch Sphere. The Bloch Sphere is a
sphere with a radius of one and a point on its surface represents the
state of a qubit.  Like a globe uses longitude and latitude to describe
points on the surface, the Bloch sphere can also use angles to describe
the state of a qubit.  This representation allows any qubit state,
including those with complex coefficients, to be represented as a point
on the surface of the Bloch sphere.  Points on the surface of the Bloch
sphere which lie along the  X, Y, or Z axis correspond to special states
as described below.

| |image0|

The qubit state is shown by the orange line in the picture. In the
picture, the state at the top of the sphere represents :math:`|0\rangle`
and the state at the bottom of the sphere represents :math:`|1\rangle`. 

When the qubit is in a superposition of :math:`|0\rangle` and
:math:`|1\rangle`, the vector will point somewhere between the two on the
sphere (i.e. the angle :math:`\theta` angle becomes somewhere between 0
(pointing straight up) – and 180 degrees, or :math:`\pi` radians (pointing
straight down). Note that in radians, 1/4 of a turn is represented by
:math:`\pi/2`). 

We have another degree of freedom on the sphere: rotations around the Z
axis, which can be described by the angle :math:`\phi`. When :math:`\phi` is
non-zero, this indicates a change in the \ *phase*\  of the qubit. This
Bloch Sphere depiction works only for single-qubit representations. For
the purpose of the schematic, we’ll assume that the length of the Bloch
vector is equal to the radius of the Bloch sphere.

| 

.. |image0| image:: https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/bloch-sphere0g2aifid2kpgb9.png

