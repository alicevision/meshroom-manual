#!/usr/bin/env sh

# Originally from https://github.com/latex3/latex3

# This script is used for building LaTeX files using Travis
# A minimal current TL is installed adding only the packages that are
# required

# See if there is a cached version of TL available
export PATH=/tmp/texlive/bin/x86_64-linux:$PATH
if ! command -v texlua > /dev/null; then
  # Obtain TeX Live
  wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
  tar -xzf install-tl-unx.tar.gz
  cd install-tl-20*

  # Install a minimal system
  ./install-tl --profile=../ci/texlive/texlive.profile

  cd ..
fi

# Just including texlua so the cache check above works
tlmgr install luatex

# In the case you have to install packages manually, you can use an index of packages like
# http://ctan.mirrors.hoobly.com/systems/texlive/tlnet/archive/
# Or better, check https://www.ctan.org/pkg/some-package to see in which TeX Live package it is contained.

# Then you can add one package per line in the texlive_packages file
# We need to change the working directory before including a file
cd "$(dirname "${BASH_SOURCE[0]}")"
tlmgr install $(cat texlive_packages)

# Keep no backups (not required, simply makes cache bigger)
tlmgr option -- autobackup 0

# Update the TL install but add nothing new
tlmgr update --self --all --no-auto-install