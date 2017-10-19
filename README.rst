IBM Quantum Experience user guides
==================================
The repository contains the user guides from the `IBM Q experience <https://quantumexperience.ng.bluemix.net>`__ 


| If quantum physics sounds challenging to you, you are not alone. All
  of our intuitions are based on day-to-day experiences and are defined
  by classical physics — so most of us find the concepts in quantum
  physics counterintuitive at first. In order to comprehend the quantum
  world, you must let go of your beliefs about our physical world, and
  develop an intuition for a completely different (and often surprising)
  set of laws.

The users guides
----------------

The user guide is divided in two.

`Beginner's Guide <rst/beginners-guide/>`__: You can find a simple aproach about Quantum Computing and
how use the IBM Q Experice tools, like Quantum Composer, or the QISKit example.

`Full User's Guide <rst/full-user-guide/>`__: This section contain the more full coverage from Quantum Computing
and in particular several examples and algorithm.

Contributors (alphabetically)
-----------------------------

Lev Bishop, Antonio Córcoles, Abigail Cross, Andrew Cross, Jay M. Gambetta.


Installation and setup
----------------------

1. Get the tools
~~~~~~~~~~~~~~~~

You'll need:

-  Install `Python 3 <https://docs.python.org/3/using/index.html>`__.
-  `Jupyter <http://jupyter.readthedocs.io/en/latest/install.html>`__
   client is needed to run the tutorials, not to use as a library.
-  Mac OS X users will find Xcode useful:
   https://developer.apple.com/xcode/
-  Optionally download Git: https://git-scm.com/download/.

2. Get the code
~~~~~~~~~~~~~~~

Clone the qiskit-qx-user-guides repository and navigate to its folder on your local
machine:

-  If you have Git installed, run the following commands:

.. code:: sh

    git clone https://github.com/QISKit/ibmqx-user-guides.git
    cd ibmqx-user-guide

-  If you don't have Git installed, click the "Clone or download" button
   at the URL shown in the git clone command, unzip the file if needed,
   then navigate to that folder in a terminal window.

3. Setup the environment
~~~~~~~~~~~~~~~~~~~~~~~~

To use as a library install the dependencies:

.. code:: sh

    # Depending on the system and setup to append "sudo -H" before could be needed.
    pip3 install -r requires.txt

4. Generate documentation
~~~~~~~~~~~~~~~~~~~~~~~~~

To generate HTML documenatation run

.. code:: sh
   
    make doc

You can find the generated documenatation in `_build/html <_build/html>`_

Do you want to help?
====================

If you'd like to contribute please take a look to our `contribution guidelines <CONTRIBUTING.rst>`__.

Documentation
-------------

The documentation for the project is in the ``rst`` directory. The
documentation for the python SDK is auto-generated from python
docstrings using `Sphinx <www.sphinx-doc.org>`_ for generating the
documentation. All the documents are created using RST format. You can 
find more info about it in:

- `Wikipedia <https://en.wikipedia.org/wiki/ReStructuredText>`_
- `Oficial web <http://docutils.sourceforge.net/rst.html>`_
- `Sphinx-doc quickstart <http://www.sphinx-doc.org/en/stable/rest.html>`_

You can generate the documentation in format HTML using.

.. code:: sh

    make doc

You can export the documenatation in other formats like "epub", "text" or others.

.. code:: sh

    make epub

You can find more info about this formats using:

.. code:: sh

    make help

Test
~~~~

The examples are include from the "test" folder, you can test all of them,
features often imply changes in the existent tests or new ones are
needed. Once they're updated/added run this be sure they keep passing:

.. code:: sh

    make test


Other QISKit projects
---------------------

- `ibmqx backend information <https://github.com/QISKit/ibmqx-backend-information>`__ Information about the different IBM Q experience backends.
- `OpenQasm <https://github.com/QISKit/openqasm>`__ Examples and tools for the OpenQASM intermediate representation.
- `Python API <https://github.com/QISKit/qiskit-api-py>`__ API Client to use IBM Q experience in Python.
- `Python SDK <https://github.com/QISKit/qiskit-sdk-py>`__ Software development kit for working with quantum programs in Python.
- `Tutorial <https://github.com/QISKit/qiskit-tutorial>`__ Jupyter notebooks for using QISKit.

Licenses
--------

This project is licensed under the Apache License 2.0 - see the `LICENSE <LICENSE>`__ file for details.

The Sphinx theme is based on `Sphinx Bootstrap Theme <https://github.com/ryan-roemer/sphinx-bootstrap-theme/blob/master/README.rst>`__
by Ryan Roemer, which is licensed under the `MIT license <https://github.com/ryan-roemer/sphinx-bootstrap-theme/blob/v0.6.0/LICENSE.txt>`__.
