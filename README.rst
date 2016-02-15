Temporal UUID64
===============
A time-based 64-bit UUID generator


Overview
--------

The time-based UUID consists of two components: a timestamp and a node ID.

.. code-block::

    +----------------------+--------------------+
    |  48-bit (timestamp)  |  16-bit (node_id)  |
    +----------------------+--------------------+

