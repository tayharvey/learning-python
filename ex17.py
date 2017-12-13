from sys import argv
from os.path import exists

script, from_file, to_file = argv

# we could do these two on one line - how?
open(from_file, 'w').write(open(to_file).read())
