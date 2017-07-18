from string import ascii_lowercase

import swap_element

class SwapGroup(object):
    """Encapsulates the subgroup of the permutation group of length 'length',
       where only adjacent pairwise swaps are taken.  (Important: the group will
       consist of `length`-1 swap_elements.)
    """

    def __init__(self, length):
        self.length = length
        self.elements = []
        for i in range(0, length-1):
            # Note: This fails for length > 26
            elt = swap_element.SwapElement(name=chr(ord("a")+i), length=length, i=i)
            self.elements.append(elt)

    def __str__(self):
        strings = []
        for elt in self.elements:
            strings.append(elt.name + " = " + str(elt))
        return "\n".join(strings)

    def __getitem__(self, name):
        if type(name) != str or len(name) != 1 or name not in ascii_lowercase:
            return None
        index = ord(name)-ord("a")
        if index < 0 or index > len(self.elements):
            return None
        return self.elements[index]
