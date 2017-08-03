IBM Quantum Experience Documentation
====================================

| If quantum physics sounds challenging to you, you are not alone. All
  of our intuitions are based on day-to-day experiences and are defined
  by classical physics — so most of us find the concepts in quantum
  physics counterintuitive at first. In order to comprehend the quantum
  world, you must let go of your beliefs about our physical world, and
  develop an intuition for a completely different (and often surprising)
  set of laws.

The users guides for the IBM Q experience
-----------------------------------------
This repository content the two User Guides from IBM Q Experience.

`Beginner Guide <rst/beginners-guide/>`__: You can find a simple aproach about Quantum Computing and
how use the IBM Q Experice tools, like Quantum Composer, or the QISKit example.

`Full User Guide <rst/full-user-guide/>`__: This section contain the more full coverage from Quantum Computing
and in particular several examples and algorithm.

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

    git clone https://github.com/QISKit/qiskit-qx-user-guides.git
    cd qiskit-qx-user-guide

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

You can find the generated documenatation into the `_build/html <_build/html>`_

Do you want to help?
====================

Documentation
-------------

The documentation for the project is in the ``doc`` directory. The
documentation for the python SDK is auto-generated from python
docstrings using `Sphinx <www.sphinx-doc.org>`_ for generating the
documentation. Please follow `Google's Python Style
Guide <https://google.github.io/styleguide/pyguide.html?showone=Comments#Comments>`_
for docstrings. A good example of the style can also be found with
`sphinx's napolean converter
documentation <http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_.


.. code:: sh

					make doc

Test
~~~~

The examples are include from the "test" folder, you can test all of them,
features often imply changes in the existent tests or new ones are
needed. Once they're updated/added run this be sure they keep passing:

.. code:: sh

					make test

:sunglasses: If you'd like to contribute please take a look to our
`contribution guidelines <CONTRIBUTING.rst>`__.

License
-------

QISKit is released under the `Apache license, version
2.0 <https://www.apache.org/licenses/LICENSE-2.0>`__.