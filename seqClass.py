#!/usr/bin/env python import sys, re
#!/usr/bin/env python

# MY SCRIPT

import sys
import re
from argparse import ArgumentParser

parser = ArgumentParser(description="Classify a sequence as DNA or RNA and optionally search for a motif.")
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif to search for in the sequence")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# Convert sequence to uppercase
args.seq = args.seq.upper()

# Validate sequence
if re.fullmatch(r'^[ACGTU]+$', args.seq):
    if 'T' in args.seq and 'U' in args.seq:
        print("The sequence contains both T and U, which is invalid.")
    elif 'T' in args.seq:
        print("The sequence is DNA")
    elif 'U' in args.seq:
        print("The sequence is RNA")
    else:
        print("The sequence can be DNA or RNA")
else:
    print("The sequence is not DNA nor RNA")

# Motif search (if provided)
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end="")
    if re.search(args.motif, args.seq):
        print("FOUND IT")
    else:
        print("DIDN'T FIND IT")

