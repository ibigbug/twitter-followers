import sys

input_file = sys.argv[1]
for l in open(input_file, 'r'):
    filename, value = l.split('=')
    with open(filename.strip(), 'w') as fd:
        fd.write(value.strip().replace('\'', ''))
