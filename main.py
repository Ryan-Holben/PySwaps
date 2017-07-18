"""
Swaps.

Usage:
    swaps.py <length>


Conventions:
    1. Internally, permutations are represented as n-tuples, and they
       contain the numbers 0..n-1.  However, for display we will show the
       numbers 1..n.
    2. We use left multiplication, i.e.
          permutation_b = swap_element_1 * swap_element_0 * permutation_a
"""

from docopt import docopt

import swaps
from math import factorial

def get_centered_lines_str(strs, delim):
    maxlen = max(len(line) for line in strs)
    format_str = "{:^" + str(maxlen) + "}"
    return delim.join(format_str.format(line) for line in strs)

def main(length=4):
    # phd = swaps.permutohedron.Permutohedron(length = length)
    # print phd
    # phd.print_small_output()
    # print phd.get_row_lengths()

    strs = []
    for length in range(7):
        phd = swaps.permutohedron.Permutohedron(length = length)
        strs.append(", ".join(str(i) for i in phd.get_row_lengths()))
    print get_centered_lines_str(strs, delim="\n\n")

#
# for elt in g.elements:
#     print elt*p
#
# exit()
#
# print p.apply_swap_element(g["a"])
# print p.apply_swap_element(g["b"])
# print p.apply_swap_element(g["c"])

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Bop')
    # print(arguments)
    try:
        length = int(arguments["<length>"])
    except:
        print "Provide a valid length."
        exit()
    main(length)
