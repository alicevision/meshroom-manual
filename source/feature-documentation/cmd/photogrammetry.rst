``meshroom_batch (formerly meshroom_photogrammetry)``
=====================================================

Launch the full photogrammetry or panorama HDR pipeline.

.. list-table:: arguments
    :header-rows: 1

    * - argument
      - description
    * - ``-i``, ``--input``
      - Input folder containing images or folders of images or file (.sfm or .json) with images paths and optionally predefined camera intrinsics.
    * - ``-I``, ``--inputRecursive``
      - Input folders containing all images recursively.
    * - ``-p``, ``--pipeline``
      - "photogrammetry" pipeline, "panotamaHdr" pipeline, "panotamaFisheyeHdr" pipeline or a Meshroom file containing a custom pipeline to run on input images. Requirements: the graph must contain one CameraInit node, and one Publish node if --output is set.
    * - ``--overrides``
      - Path to a JSON file containing the graph parameters overrides.
    * - ``--paramOverrides``
      - Override specific parameters directly from the command line (by node type or by node names).
    * - ``-o``, ``--output``
      - Output folder where results should be copied to. If not set, results will have to be retrieved directly from the cache folder.
    * - ``--cache``
      - Custom cache folder to write computation results. If not set, the default cache folder will be used.
    * - ``--save``
      - Save the configured Meshroom graph to a project file. It will setup the cache folder accordingly if not explicitly changed by --cache.
    * - ``--compute``
      - You can set it to <no/false/0> to disable the computation.
    * - ``--scale``
      - Downscale factor override for DepthMap estimation. By default (-1): use pipeline default value.
    * - ``--toNode``
      - Process the node(s) with its dependencies.
    * - ``--forceStatus``
      - Force computation if status is RUNNING or SUBMITTED.
    * - ``--forceCompute``
      - Compute in all cases even if already computed.
    * - ``--submit``
      - Submit on renderfarm instead of local computation.
    * - ``--submitter``
      - Execute job with a specific submitter.
