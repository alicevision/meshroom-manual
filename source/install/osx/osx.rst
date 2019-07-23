OSX
~~~

Originally published on 2018-08-17 by
`Ryan Baumann <https://ryanfb.github.io/>`_
on
`ryanfb.github.io <https://ryanfb.github.io/etc/2018/08/17/alicevision_and_meshroom_on_mac_os_x.html>`_

`AliceVision <https://alicevision.github.io/>`_
and its Meshroom program are an exciting new free and open-source pipeline for photogrammetry processing. Unfortunately, compiling and using either of these programs on Mac OS X is
`not exactly straightforward <https://github.com/alicevision/AliceVision/issues/444>`_
. As a result, I’ve compiled
`a Homebrew tap <http://github.com/ryanfb/homebrew-alicevision>`_
which includes the necessary formulae, and will use this post to outline how to use them to get up and running.
*Note that this is intended as a first step for Mac users wishing to experiment with and improve the AliceVision/Meshroom software, and as a result these instructions may become outdated with time.*

.. image:: homebrew.jpg

The following instructions assume a working
`Homebrew <https://brew.sh/>`_
install.

System Requirements
^^^^^^^^^^^^^^^^^^^

First off, your Mac will currently need an nVidia GPU with a CUDA compute capability of 2.0 or greater. This is probably a pretty small portion of all Macs sold, but you can check your GPU by looking in “About This Mac” from the Apple icon in the top left corner of the screen, under “Graphics”. If you have an nVidia GPU listed there, you can check its compute capability on
`the nVidia CUDA GPUs page <https://developer.nvidia.com/cuda-gpus>`_
.

Second, you’re going to need to install
`the latest CUDA toolkit <https://developer.nvidia.com/cuda-downloads>`_
. As of this writing, that’s CUDA 9.2, which is only officially compatible with OS X 10.13 (High Sierra), so you may also need to upgrade to the latest version of High Sierra if you haven’t already. Alongside this I would also suggest installing the latest nVidia CUDA GPU webdriver, which as of this writing is
`387.10.10.10.40.105 <https://www.nvidia.com/download/driverResults.aspx/136062/en-us>`_
.

Third,
`CUDA 9.2 is  <https://docs.nvidia.com/cuda/cuda-installation-guide-mac-os-x/index.html>`_
`only <https://docs.nvidia.com/cuda/cuda-installation-guide-mac-os-x/index.html>`_
` compatible with the version of  <https://docs.nvidia.com/cuda/cuda-installation-guide-mac-os-x/index.html>`_
`clang <https://docs.nvidia.com/cuda/cuda-installation-guide-mac-os-x/index.html>`_
` distributed with Xcode 9.2 <https://docs.nvidia.com/cuda/cuda-installation-guide-mac-os-x/index.html>`_
, and will refuse to compile against anything else. You may have an older or newer version of Xcode installed. As of this writing, if you fully update Xcode within a fully updated OS X install, you’ll have Xcode 9.4.1. To get back to Xcode 9.2, what you can do is go to
`Apple’s Developer Downloads page <https://developer.apple.com/download/more/>`_
(for which you’ll need a free Apple developer account), then search for “Xcode 9.2”, then install the Command Line Tools for Xcode 9.2 package for your OS version. After installing, run

*sudo xcode-select --switch /Library/Developer/CommandLineTools*
and then verify that

*clang --version*
* *
shows
*Apple LLVM version 9.0.0*

Once you’ve done all this, you can verify a working CUDA install by going to
*/Developer/NVIDIA/CUDA-9.2/samples/1_Utilities/deviceQuery*
and running
*sudo make && ./deviceQuery*
, which should output your GPU information. If it doesn’t build correctly, or
deviceQuery
errors or doesn’t list your GPU, you may need to look over the steps above and check that everything is up to date (you can also check the CUDA panel in System Preferences).
.. image:: homebrew-inst.jpg

Installation
^^^^^^^^^^^^

If you’ve followed all the above setup instructions and requirements, installing the AliceVision libraries/framework should be as easy as:

brew install ryanfb/alicevision/alicevision

Meshroom Installation & Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I haven’t yet created a Homebrew formula for the
`Meshroom package itself <https://github.com/alicevision/meshroom>`_
, as it’s all Python and doesn’t seem particularly difficult to install/use once AliceVision is installed and working correctly. Just follow the install instructions there (for my specific Python configuration/installation I used
pip

3
instead of
pip
and
python3
instead of
python
):

git clone --recursive git://github.com/alicevision/meshroom

cd meshroom

pip install -r requirements.txt

You can report an issue on
`https://github.com/ryanfb/homebrew-alicevision/issues <https://github.com/ryanfb/homebrew-alicevision/issues>`_


One gotcha I ran into is that the CUDA-linked AliceVision binaries invoked by Meshroom don’t automatically find the CUDA libraries on the
DYLD_LIBRARY_PATH
, and setting the
DYLD_LIBRARY_PATH
from the shell launching Meshroom doesn’t seem to get the variable passed into the shell environment Meshroom uses to spawn commands. Without this, you’ll get an error like:

dyld: Library not loaded: @rpath/libcudart.9.2.dylib

Referenced from: /usr/local/bin/aliceVision_depthMapEstimation

Reason: image not found

In order to get around this, you can symlink the CUDA libraries into
/usr/local/lib
(most of the other workarounds I found for permanently modifying the
DYLD_LIBRARY_PATH
seemed more confusing or fragile than this simpler approach):
`1 <https://ryanfb.github.io/etc/2018/08/17/alicevision_and_meshroom_on_mac_os_x.html#fn:dyldpath>`_

for i in /Developer/NVIDIA/CUDA-9.2/lib/*.a /Developer/NVIDIA/CUDA-9.2/lib/*.dylib; do ln -sv "$i" "/usr/local/lib/$(basename "$i")"; done

You can undo/uninstall this with:

for i in /Developer/NVIDIA/CUDA-9.2/lib/*.a /Developer/NVIDIA/CUDA-9.2/lib/*.dylib; do rm -v "/usr/local/lib/$(basename "$i")"; done

You may also want to download the voctree dataset:

curl 'https://gitlab.com/alicevision/trainedVocabularyTreeData/raw/master/vlfeat_K80L3.SIFT.tree' -o /usr/local/Cellar/alicevision/2.0.0/share/aliceVision/vlfeat_K80L3.SIFT.tree

Then launch with:

ALICEVISION_SENSOR_DB=/usr/local/Cellar/alicevision/2.0.0/share/aliceVision/cameraSensors.db ALICEVISION_VOCTREE=/usr/local/Cellar/alicevision/2.0.0/share/aliceVision/vlfeat_K80L3.SIFT.tree PYTHONPATH=$PWD python meshroom/ui

Import some photos, click “Start”, wait a while, and hopefully you should end up with a reconstructed and textured mesh
.
By default, the output will be in
MeshroomCache/Texturing/
(relative to where you saved the project file).

When you launch Meshroom
*without*
sudo, the temp path will be something like this:

.. image:: cache-folder.jpg

When starting with sudo, it will be /tmp/MeshroomCache by default

**Footnotes:**

#.  Previously, I suggested modifying
    meshroom/core/desc.py
    so that
    `the return value at the end of the  <https://github.com/alicevision/meshroom/blob/develop/meshroom/core/desc.py#L368>`_
    `buildCommandLine <https://github.com/alicevision/meshroom/blob/develop/meshroom/core/desc.py#L368>`_
    ` method <https://github.com/alicevision/meshroom/blob/develop/meshroom/core/desc.py#L368>`_
    instead reads:



``return 'DYLD_LIBRARY_PATH="/Developer/NVIDIA/CUDA-9.2/lib" ' + cmdPrefix + chunk.node.nodeDesc.commandLine.format(/**chunk.node._cmdVars) + cmdSuffix``

Baumann, Ryan. “AliceVision and Meshroom on Mac OS X.”
*Ryan Baumann - /etc*
(blog), 17 Aug 2018,
`https://ryanfb.github.io/etc/2018/08/17/alicevision_and_meshroom_on_mac_os_x.html <https://ryanfb.github.io/etc/2018/08/17/alicevision_and_meshroom_on_mac_os_x.html>`_
(accessed 10 Oct 2018).