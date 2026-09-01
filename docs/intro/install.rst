Install Guide
=============

Being a modern Python framework, FTMGram requires an up to date version of Python to be installed in your system.
We recommend using the latest versions of both Python 3 and pip.


-----

Install FTMGram
----------------

Bleeding Edge
-------------

You can install the development version from the git appropriate branch using this command:

    .. code-block:: text

        $ pip uninstall -y ftmgram && pip install ftmgram

-   or, with :doc:`TgCrypto <../topics/speedups>` as extra requirement (recommended):

    .. code-block:: text

        $ pip install ftmgram[fast]

Verifying
---------

To verify that FTMGram is correctly installed, open a Python shell and import it.
If no error shows up you are good to go.

.. parsed-literal::

    >>> from ftmgram import __version__
    >>> __version__
    '2.0.106-TL-158'

.. _`Github repo`: http://github.com/TelegramPlayGround/FTMGram
