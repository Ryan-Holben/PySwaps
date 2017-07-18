"""
    Convention:  Internally, permutations are represented as n-tuples, and they
    contain the numbers 0..n-1.  However, for display we will show the numbers
    1..n.
"""

import swaps

p = swaps.permutation.permutation(4)
s = swaps.swap_element.swap_element(name="a", length=4, i=1, j=2)
g = swaps.swap_group.swap_group(length=4)

for elt in g.elements:
    print elt*p

exit()

for i in range(0,4):
    for j in range(0, 4):
        print p.swap_by_index(i, j),
    print ""

print p.apply_swap_element(g["a"])
print p.apply_swap_element(g["b"])
print p.apply_swap_element(g["c"])
