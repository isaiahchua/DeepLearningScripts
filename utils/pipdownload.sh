#! /bin/bash

python -m pip download \
   --only-binary=:all: \
   --platform any \
   SomePackage
