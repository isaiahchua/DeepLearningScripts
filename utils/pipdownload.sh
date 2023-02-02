#! /bin/bash

python -m pip download \
   --only-binary=:all: \
   --platform any \
   --dest /Users/isaiah/Downloads/ \
   --no-deps \
   SomePackage
