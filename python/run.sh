#!/bin/bash

python diff.py          ../data/file1 ../data/file2
echo -e '\n\n'
python diffPrimitive.py ../data/file1 ../data/file2
echo -e '\n\n'
diff                    ../data/file1 ../data/file2

echo -e '\n\n\n\n\n\n\n\n'

python diff.py          ../data/lao ../data/tzu
echo -e '\n\n'
python diffPrimitive.py ../data/lao ../data/tzu
echo -e '\n\n'
diff                    ../data/lao ../data/tzu
