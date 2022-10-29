#!/bin/sh
for f in $(find . -type f -name "*.png")
do
echo "Processing $f ..."
mogrify $f
done

for f in $(find . -type f -name "*.jpg")
do
echo "Processing $f ..."
mogrify $f
done

for f in $(find . -type f -name "*.jpeg")
do
echo "Processing $f ..."
mogrify $f
done