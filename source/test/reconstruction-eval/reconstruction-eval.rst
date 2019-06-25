Reconstruction: How long does it take?
======================================

You can calculate with 30sec. per image on a computer with i7@2,9GHz, GTX1070 8GB, 32GB Ram.

Performance: % of overall processing time with default pipeline:
~38% DepthMap / ~24% Meshing

With the 2019.1.0 release, the reconstruction time has been reduced by ~30% compared to the 2018.1 release. The Cache Folder file size has been reduced by 20%
Tested with the **Monstree Dataset**: (comparing only computing time, not quality)
Computing time in seconds: (total MR2018 260s / MR2019 185s)


https://web.archive.org/web/20181010161448/https://scanbox.xyz/blog/alicevision-opensource-photogrammetry/

.. image:: comparison.png

.. image:: time-node.png

For a Full Pipeline Evaluation including the "Tanks and Temples" evaluation benchmark read **D5.4: Deliver 3D reconstruction
benchmarks with dataset** available on  https://cordis.europa.eu/project/rcn/205980/results/en in Documents, reports.