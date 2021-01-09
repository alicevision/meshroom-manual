Submitters
==========

Meshroom supports external graph computation through this API.
This allows the process to run on a render farm to reduce computation time.

API
+++

.. code-block:: python

    from meshroom.core.submitter import BaseSubmitter


    class MySubmitter(BaseSubmitter):
        def __init__(self, parent=None):
            super(MySubmitter, self).__init__(name='Submitter', parent=parent)

        def submit(self, nodes, edges, filepath):
            # submit task to render farm

.. list-table:: ``submit``
    :header-rows: 1

    * - argument
      - type
      - description
    * - ``nodes``
      - list (meshroom.core.node.Node)
      - All of the nodes that need to be submitted
    * - ``edges``
      - set (meshroom.core.node.Node: meshroom.core.node.Node)
      - {A: B} A depends on B
    * - ``filepath``
      - string
      - Path to .mg file.
