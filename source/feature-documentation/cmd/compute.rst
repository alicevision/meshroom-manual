``meshroom_compute``
====================

Execute a graph of processes.

.. list-table:: arguments
    :header-rows: 1

    * - argument
      - description
    * - graphFile
      - Filepath to a graph file.
    * - ``--node``
      - Process the node. It will generate an error if the dependencies are not already computed.
    * - ``--toNode``
      - Process the node with its dependencies.
    * - ``--forceStatus``
      - Force computation if status is RUNNING or SUBMITTED.
    * - ``--forceCompute``
      - Compute in all cases even if already computed.
    * - ``--extern``
      - Use this option when you compute externally after submission to a render farm from meshroom.
    * - ``--cache``
      - Custom cache folder to write computation results. If not set, the default cache folder will be used.
    * - ``-i``, ``-iteration``
      - Index of a chunk to compute.
