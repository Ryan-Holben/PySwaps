import permutation
import swap_group
from math import factorial

class Permutohedron(object):
    """Represents a permutohedron; that is, a permutation group on `n` elements
       that is constructed by pairwise adjacent swaps of elements.  A focus is
       taken on the connections between those elements, and the levels built in
       the construction of the permutohedron.
    """
    def __init__(self, length, print_while_constructing=False):
        self.length = length
        fac = factorial(length)
        self.swap_group = swap_group.SwapGroup(length=length)
        starting_permutation = permutation.Permutation(length)
        self.rows = [[starting_permutation]]
        pool = [starting_permutation]
        if print_while_constructing:
            print self.rows[-1][0]
        while len(pool) < fac:
            row = self.rows[-1]
            new_row = []
            for p in row:
                for elt in self.swap_group.elements:
                    new_p = elt*p
                    if new_p not in pool:
                        new_row.append(new_p)
                        pool.append(new_p)
            if print_while_constructing:
                print " ".join([str(p) for p in new_row])
            self.rows.append(new_row)

    def __str__(self):
        strings = [" ".join([str(p) for p in row]) for row in self.rows]
        maxlen = max([len(row) for row in strings])
        format_str = "{:^" + str(maxlen) + "}"
        return "\n\n".join(format_str.format(row) for row in strings)

    def print_small_output(self):
        maxlen = max([2*len(row)-1 for row in self.rows])
        format_str = "{:^" + str(maxlen) + "}"
        print "\n".join(str(len(row)) + ":\t" + format_str.format((". "*len(row))[:-1]) for row in self.rows)

    def get_row_lengths(self):
        return [len(row) for row in self.rows]
