import codecs
import re
import argparse
from sys import stdout

def read_data(txtfile):
    with codecs.open(txtfile, 'r', 'utf-8') as f:
        for line in f:

            t = line.rstrip()

            yield re.split('\s+', t)

def main():

    documents = [line for line in read_data(args['input'])]

    with open(args['output'], 'w', encoding='utf8') as fp:
        for i, d in enumerate(documents):

            stdout.write('Converting line: ')
            stdout.write('%8d\r' % i)
            stdout.flush()

            fp.write('%s\n' % ('# ' + ' '.join([item.rsplit('_', 1)[0] for item in d])))

            for token in d:
                line = token.rsplit('_', 1)
                line = ' '.join(line)
                fp.write('%s\n' % line)

            fp.write('\n')

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="Mac-morpho input file.")
ap.add_argument("-o", "--output", required=True, help="Conll output file.")
args = vars(ap.parse_args())

if __name__ == '__main__':
    main()