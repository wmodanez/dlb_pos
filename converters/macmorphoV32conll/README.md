# Mac-Morpho converter

## Description
The script will convert the Brazilian [Portuguese Mac-Morpho](http://nilc.icmc.usp.br/macmorpho/) corpus with annotated PoS tags to a compatible Conll format.

## Files
Within the **input** folder there are the original [Mac-Morpho V3](http://nilc.icmc.usp.br/macmorpho/macmorpho-v3.tgz) files.

Within the **output** folder there are the converted files in the conell-compatible format.

## Usage
```bash
$ python convert.py -i input/macmorpho-dev.txt -o output/conll-dev.txt
$ python convert.py -i input/macmorpho-test.txt -o output/conll-test.txt
$ python convert.py -i input/macmorpho-train.txt -o output/conll-train.txt
```