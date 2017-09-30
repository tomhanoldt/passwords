#!/usr/bin/env python
import sys

file2unique=sys.argv[1]

with open(file2unique) as result:
    uniqlines = set(result.readlines())
    with open(file2unique, 'w') as rmdup:
        rmdup.writelines(set(uniqlines))
