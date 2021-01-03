Nodes
=====

Meshroom uses a nodes to control the reconstruction.
A node represents a task that can be executed.

Attributes
++++++++++

This is how we control what goes in the node and what comes out.
There are many types of attributes that are used.

Edges
+++++

File attributes can be connected.
This represents a dependency for that node.
If the output of node A and node B is connected to the input of node C,
C will not be executed until A and B are successful.
This makes it easy to set up complicated workflows.

Hashes
++++++

Every node has a hash based on its attributes.
If an attribute that changes the output of the node is changed,
that node will now have a different hash and so any previous computation done by this node will be invalid and so the progress is now gone.
Any nodes that depend on this node will also change their hash because their file input attribute changed the directory which is based on the hash of the first node.
And then that happens to any nodes that depend on those nodes and so on.
Since all of the data is still stored in the cache folder under the previous hash,
no time is lost if the attribute is changed back to the first value because the new hash will match the first hash.

Files
+++++

Every node has associated log(s), status(es) and statistics files.
These allow the progress and performance of the process to be monitored.

API
+++

Naming
######

Use UpperCamelCase for both the class (like normal) and the file.
For example 'CameraInit.py' contains 'class CameraInit'

Node Type
#########

.. code-block:: python

    from meshroom.core import desc


    class MyNode(desc.CommandLineNode):
        command = 'myExecutable {allParams}'

    # or

    class MyNode(desc.Node):
        def processChunk(self, chunk):
            # code for the node to run goes here

        # optional
        def stopProcess(self, chunk):
            # code here runs when the stop button is clicked

For ``desc.CommandLineNode``, ``{allParams}`` is the name of the group.
All parameters in this group will be added to the command in the form
``--name value``.
To add only the value to the command, use
``{myParameterValue}``
for a parameter called ``myParameter``.

Class variables
###############

Node
~~~~

``cpu``, ``gpu``, ``ram``:

Used for submitters to be efficient in allocating resources.

.. list-table::
    :header-rows: 1

    * - level
      - value
      - description
    * - ``desc.Level.NONE``
      - 0
      - Does not use this resource.
    * - ``desc.Level.NORMAL``
      - 1
      - Uses this resource but not much.
    * - ``desc.Level.INTENSIVE``
      - 2
      - Uses a lot of this resource.

``size``:

.. list-table::
    :header-rows: 1

    * - size
      - description
    * - ``desc.DynamicNodeSize``
      - Expresses a dependency to an input attribute to define
        the size of a Node in terms of individual tasks for parallelization.
        If the attribute is a link to another node, Node's size will be the same as this connected node.
        If the attribute is a ListAttribute, Node's size will be the size of this list.
    * - ``desc.MultiDynamicNodeSize``
      - Expresses dependencies to multiple input attributes to
        define the size of a node in terms of individual tasks for parallelization.
        Works as DynamicNodeSize and sum the sizes of each dependency.
    * - ``desc.StaticNodeSize``
      - Expresses a static Node size in terms of individual tasks for parallelization.

``parallelization``:
``desc.Parallelization(blockSize)`` defines a parallel task with a given block size.

``documentation``:
Text is displayed in the 'documentation' tab in the GUI.

CommandLineNode
~~~~~~~~~~~~~~~

``commandLine``:
the command to execute

``commandLineRange``:
the command arguments for a range start and end for a parallelized node using ``'{rangeStart}'`` and ``'{rangeBlockSize}'``

Parameters
~~~~~~~~~~
2 class variables can be defined, ``inputs`` and ``outputs``,
both of which are of type list containing parameter objects.

.. list-table:: General arguments (applies to all attributes)
    :header-rows: 1

    * - argument
      - type
      - default
      - description
    * - ``name``
      - string
      -
      - The command line option or how the parameter will be accessed by ``chunk.node.myParameterName.value``.
    * - ``label``
      - string
      -
      - What it is called in the GUI.
    * - ``description``
      - string
      -
      - Description shown in the GUI.
    * - ``value``
      - depends
      -
      - Default value of an input attribute or value of output attribute.
    * - ``uid``
      - list
      -
      - Controls if the parameter effects the node hash.
    * - ``group``
      - string
      - ``'allParams'``
      - To control if it is added to the command line.
    * - ``advanced``
      - boolean
      - ``False``
      - To make it hidden by default in the GUI.
    * - ``enabled``
      - boolean
      - ``True``
      - Enabled by default but can be disabled if a criteria is met.

Extra arguments:

.. list-table:: ``desc.ListAttribute``
    :header-rows: 1

    * - argument
      - type
      - default
      - description
    * - ``elementDesc``
      - attribute description
      -
      - The attribute description of elements to store in that list.
    * - ``joinChar``
      - string
      - ``' '``
      - Character to join the attributes for the command line.

.. list-table:: ``desc.GroupAttribute``
    :header-rows: 1

    * - argument
      - type
      - default
      - description
    * - ``groupDesc``
      - list (attribute descriptions)
      -
      - The description of the attributes composing this group.
    * - ``joinChar``
      - string
      - ``' '``
      - Character to join the attributes for the command line.

.. list-table:: ``desc.IntParam``, ``desc.FloatParam``
    :header-rows: 1

    * - argument
      - type
      - default
      - description
    * - ``range``
      - tuple (int/float)
      -
      - (minimum, maximum, step)

.. list-table:: ``desc.ChoiceParam``
    :header-rows: 1

    * - argument
      - type
      - default
      - description
    * - ``values``
      - tuple (string)
      -
      - Available values to choose from.
    * - ``exclusive``
      - boolean
      -
      - Can it only be one value at once?
    * - ``joinChar``
      - string
      - ``' '``
      - Character to join the selected attributes for the command line if not exclusive.

The following parameters have no extra arguments:
``desc.File``,
``desc.BoolParam``,
``desc.StringParam``

Logging
#######

For ``desc.CommandLineNode`` the standard output will be sent to the log file.
For ``desc.Node`` the logging is handled through ``chunk.logManager`` and ``chunk.logger``.

.. code-block:: python

    class MyNode(desc.Node):
        def processChunk(self, chunk):
            try:
                chunk.logManager.start('debug')

                chunk.logManager.makeProgressBar(100, 'this is a progress bar')
                chunk.logManager.updateProgressBar(50) # progress bar half way

                chunk.logger.debug('this is a debug log')
                chunk.logger.info('this is an info log')
                chunk.logger.warning('this is a warning log')
                raise RuntimeError('this is an error log')
            except Exception as e:
                chunk.logger.error(e)
                raise RuntimeError()
            finally:
                chunk.logManager.end()
